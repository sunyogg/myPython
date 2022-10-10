
import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from time import sleep

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior."""


    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()

        # create settings instance that will store all the settings
        self.settings = Settings()
        # create a window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        # create a instance that will store game stats.
        # create ship instance to create and draw a ship on screen.
        self.ship = Ship(self)
        # create bullet instance to create and draw and update bullet on screen.
        self.bullets = pygame.sprite.Group()
        # create a group to that store aliens and draw and update on screen
        self.aliens = pygame.sprite.Group()
        # method that will create fleet. Don't know why we don't have this method inside run_game.
        self._create_fleet()
        self.stats = GameStats(self)
        # make the play button 
        self.play_button = Button(self,"Play")
        self.sb = Scoreboard(self)
        
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            #self._game_over()
            self._update_screen()


    # watch for keyboard and mouse events.
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos) 


    def _check_keydown_events(self,event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True 
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 


    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False


    def _check_play_button(self,mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # only restart the game when button is clicked and game is unactive
        if button_clicked and not self.stats.game_active:
            # Reset the game's settings
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()

            # Get rid of remaining alien and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet of alien and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed: 
            # limiting the number of bullet allowed.
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update the postiion of bullet, and get rid of old bullets. """
        # update bullets position.
        self.bullets.update()
        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # check if any bullet collided with a alien.
        self.check_bullet_alien_collision()


    def check_bullet_alien_collision(self):
        """Respond to bullet alien collision."""
        # remove any bullet and alien that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # collisions is dictionary containing bullet as key and alien as value
            # sometimes value can be a list when two bullet hits the same alien
            # or when one bullet hits more than 1 alien (when bullet width is more.)
            for aliens in collisions.values():
                # aliens is a list 
                # self.stats.score += self.settings.alien_points * len(aliens)
                for alien in aliens:
                    # alien is a single element in the list aliens.
                    self.stats.score += self.settings.alien_points
                    self.sb.prep_score()
                    self.sb.check_highscore()

        if not self.aliens:
            # when all the aliens are killed with bullet.
            self.bullets.empty()
            self._create_fleet() 
            self.settings.increase_speed()
            sleep(0.5)
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _check_fleet_edges(self):
        """Respond appropriately if any alien have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                # using break because we only need to check the edge for that 
                # first alien that touches the edge of the screen.
                break
        

    def _change_fleet_direction(self):
        """Drop the entire fleet and the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        """Check if the fleet is at an edge, 
            then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update() #####
        # look for alien ship collsions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens,):
            self._ship_hit()
        # look for aliens hittings the screen.
        self._check_alien_bottom()


    def _check_alien_bottom(self):
        """Check if any alien has reached bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if ship got hit by alien.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to ship being hit by an alien."""
        if self.settings.ship_limit > 0:
            # Decrement ships_left and update score
            self.settings.ship_limit -= 1
            self.sb.prep_ship()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(0.5)
        if self.settings.ship_limit == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # create an alien and find the number of alien in a row.
        # spacing between each alien is equal to width of one alien
        alien = Alien(self)
        # availabe space for aliens in a row
        alien_width, alien_height = alien.rect.size
        available_space_x = (self.settings.screen_width) - (2 * alien_width)
        # number of aliens in a single row.
        number_aliens_x = available_space_x // (2 * alien_width) # == 6
        ## Determine number rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height) - ( 3 *  alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        ## create the first row of aliens
        for row_number in range(number_rows):
            # This loop changes the y coordinate of the alien.
            for alien_number in range(number_aliens_x):
                # This loop changes the x coordinate of the alien.
                self._create_alien(alien_number,row_number)



    def _create_alien(self,alien_number,row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien_width = 60
        # alien_number = 0,1,2,3,4,5
        # as the loop restarts the calculation is done from x = 0, for every
        # other alien
        alien.x = alien_width + 2 * alien_width * alien_number
        # alien.x = coordinate of places where alien are going to place
        # placing alien.rect in those places  
        alien.rect.x = alien.x
        # come to the next row, before restarting the loop
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        # adding alien with specified coordinates to the aliens group so that
        # they can be printed on the screen.
        self.aliens.add(alien)
        # the loop will restart after reaching till here
        # print(alien.rect.y, "--" ,alien.rect.x)
        # since the row number only changes after 9 number_alien_x, what it
        # really means is that, in row number =1, 9 aliens are printing, then after
        # 9 aliens, row number becomes 2, so in the row 2, 9 aliens are printed,
        # then after 9 aliens again row number changes to become 3, so 9 aliens are
        # printed in the row 3, this loop keeps on working until range of main loop
        # reacher the final value of row number.


    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # Draw bullet in the screen after firing a bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the aliens in the screen that are present in aliens group
        self.aliens.draw(self.screen) 

        # Draw the score information
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        
         
        # make the most recently drawn screen visible.
        pygame.display.flip()




if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    


