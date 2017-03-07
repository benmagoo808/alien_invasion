import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """

    def __init__(self, ai_settings, screen):
        """ Initialize the alien and its starting position """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near the top of the left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Move the alien right """
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
