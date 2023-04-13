import pygame
import math
import time

class Enemies(pygame.sprite.Sprite):

    def __init__(self,position,png):
        super().__init__()

        self.image = pygame.image.load(png)
        self.rect = self.image.get_rect(topleft = position)
        self.vitesse = 2

        self.direction = pygame.math.Vector2(0,0)


    def mouvement(self):
        self.direction.x = self.vitesse


    def update(self):
        self.mouvement()
        self.rect.x += self.direction.x


class Pate_a_choux(pygame.sprite.Sprite):

    def __init__(self,position,png):
        super().__init__()

        self.image = pygame.image.load(png)
        self.rect = self.image.get_rect(topleft=position)

        self.gravite = 0.8
        self.vitesse = 3
        self.angle = 30
        self.angleradian = math.pi * self.angle/180
        self.t = 0


    def mouvement(self):
        self.vh = self.vitesse * math.cos(self.angleradian)
        self.vv = self.vitesse * math.sin(self.angleradian) - self.gravite * self.t
        self.t += 0.01

    def update(self):
        self.mouvement()
        self.rect.x += self.vh
        self.rect.y -= self.vv



