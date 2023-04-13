import pygame
from setting import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()

        self.image = pygame.image.load("perso.png")
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2(0,0)

        # player mouvement
        self.speed = 10
        self.gravity = 0.8
        self.jump_speed = -16
        self.cooldown = 0
        self.vie = 1
        self.angle = 30
        self.angleradian = math.pi * self.angle / 180

        # temps sur touche
        self.tg = 0
        self.td = 0
        self.touche_appye_d =0
        self.touche_appye_g = 0


    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :
            if self.touche_appye_d ==1:
                self.touche_appye_d = pygame.time.get_ticks()
            else:
                self.td = pygame.time.get_ticks() - self.touche_appye_d

            self.td = self.td /1000
            self.rect.x += (self.speed * math.cos(self.angleradian)*self.td)
            self.rect.y -= (-1/2 * self.gravity * -(self.td)**2) +  (self.speed * math.sin(self.angleradian)*self.td)
            print(self.td)
            self.td = 0
            self.touche_appye_d = 0





        if keys[pygame.K_LEFT] :
            if self.touche_appye_g == 1:
                self.touche_appye_g = pygame.time.get_ticks()
            else:
                self.tg = pygame.time.get_ticks() - self.touche_appye_g
            self.tg = self.tg / 1000
            self.rect.x -= (self.speed * math.cos(self.angleradian) * self.tg)
            self.rect.y -= (-1 / 2 * self.gravity * -(self.tg) ** 2) + (self.speed * math.sin(self.angleradian) * self.tg)
            print(self.tg)
            self.tg = 0
        else:
            self.tg = 0
            self.touche_appye_g = 0

            #self.rect.y += self.jump_speed
            #self.rect.x -= self.speed




        '''if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_q]:
            self.direction.x = -1
        else:
            self.direction.x = 0



        if keys[pygame.K_z] and self.cooldown == 0:
            self.gravity = -0.8
            self.jump_speed = 16


        if keys[pygame.K_s] :
            self.gravity = 0.8
            self.cooldown = 120
            self.jump_speed = -16

    def cooldownTime(self):
        if self.cooldown > 0:
            self.cooldown -= 1'''

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y



    def jump(self):
        self.direction.y = self.jump_speed
        self.direction.x = self.speed


    def update(self):
        self.input()



