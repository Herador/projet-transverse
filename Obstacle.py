import pygame


class obstacle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Perso-removebg-preview.png")
        #self.obstacle = pygame.sprite.Sprite()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200

    def update(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y