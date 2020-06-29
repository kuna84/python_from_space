import pygame

class Ship():

    def __init__(self, screen):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        self.screen = screen

        # Wczytaie obrazu statku kosmicznego i pobranioe jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Nowy statek pojawi sie na dole po środku
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    
