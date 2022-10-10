import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in the fleet."""


    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the alien image and set it's attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start new alien near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edge(self):
        """Return True if alien is at the edge of the screen."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

