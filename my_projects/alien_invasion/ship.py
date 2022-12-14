
import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""


    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # self.rect == ship position
        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen.
        # positioning the ship at the midbottom of the screen.
        # setting the location of the ship
        self.rect.midbottom = self.screen_rect.midbottom
        # midbottom of rectangle of ship == midbottom of rectangle of screen.
        # movement flag 

        # store a decimal value for the ship's current horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's x value, not the rect.
      # if self.moving_right is True and self.rect.right < self.screen_rect.right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 550:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # update rect object from self.x
        # update the position of the ship 
        self.rect.x = self.x
        self.rect.y = self.y


    def center_ship(self):
        """Recenter the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        


    def blitme(self):
        """Draw the picture of ship at it's current location."""
        self.screen.blit(self.image, self.rect)








