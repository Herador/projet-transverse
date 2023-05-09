import pygame, sys
from setting import *
import math
from objet import obstacle
from level import tile_size
class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load("perso.png")
        self.rect = self.image.get_rect(center = position)

        self.direction = pygame.math.Vector2(0, 0)

        # paramètre du joueur
        self.speed = 1
        self.gravity = 1
        self.jump_speed = 10
        self.cooldown = 0
        self.vie = 1

        # donnée du saut
        self.saut = False
        self.positionInit = 0
        self.angle = 20
        self.angleradian = math.pi * self.angle / 180
        self.t = 0
        self.espace = False
        self.stop_traj = False

        # donné du temps pour modifié l'angle
        self.start_time = 0
        self.end_time = 0
        self.temps = 0

        #gauche/droite
        self.g = False
        self.d = True

        #monte/descente angle
        self.Monte_A = True
        self.Descente_A = False
    def input(self):
        keys = pygame.key.get_pressed()
        if self.saut== False:
            self.angle = 20

        if keys[pygame.K_LEFT]:
            self.d = False
            self.g = True

        if keys[pygame.K_RIGHT]:
            self.d = True
            self.g = False


        if keys[pygame.K_SPACE] and self.saut == False:
            self.stop_traj = True
            if self.start_time == 0:
                self.start_time = pygame.time.get_ticks()
        else:
            if self.start_time != 0:
                self.end_time = pygame.time.get_ticks()
                self.temps = self.end_time - self.start_time
                self.temps = self.temps / 100
                self.saut = True
                self.espace = True
                self.positionInit = self.rect.y

        if self.stop_traj == False:
            self.saut = False
            self.direction.x, self.direction.y, self.t = 0, 0, 0

        if self.saut and self.espace:
            for i in range(int(self.temps)):
                if self.Monte_A:
                    self.angle += 5
                if self.angle > 35:
                    self.Descente_A = True
                    self.Monte_A = False
                if self.Descente_A:
                    self.angle -= 5
                if self.angle < 20:
                    self.Monte_A = True
                    self.Descente_A = False
                print(self.angle)
            '''            if self.temps>0:
                            self.angle = 20
                        elif self.temps>2:
                            self.angle = 25
                        elif self.temps>4:
                            self.angle = 30
                        elif self.temps> 6 :
                            self.angle = 35'''

            if self.g:
                self.angleradian = math.pi - math.pi * self.angle / 180
            else:
                self.angleradian = math.pi * self.angle / 180

            self.direction.x = (self.speed * math.cos(self.angleradian) * self.t)
            self.direction.y = (self.jump_speed * math.sin(self.angleradian) * self.t) - (self.gravity * self.t ** 2 / 2)

            self.t += 0.5
            self.temps = 0
            self.start_time = 0
            self.end_time = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()

        self.rect.x += self.direction.x
        self.rect.y -= self.direction.y

