import pygame
from setting import *
import math


class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        self.image = pygame.image.load("perso.png")
        self.rect = self.image.get_rect(topleft=position)

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
        self.angle = 40
        self.angleradian = math.pi * self.angle / 180
        self.t = 0

    def input(self):
        """keysup = pygame.KEYUP
        keysdown = pygame.KEYDOWN"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angleradian = math.pi-math.pi * self.angle / 180
        else :
            self.angleradian = math.pi * self.angle / 180

        if keys[pygame.K_LEFT]:
            self.angleradian = math.pi - math.pi * self.angle / 180
        if keys[pygame.K_RIGHT]:
            self.angleradian = math.pi * self.angle / 180

        if keys[pygame.K_SPACE] and self.saut == False:
            self.saut = True
            self.positionInit = self.rect.y

        if self.positionInit < self.rect.y:
            self.saut = False
            self.direction.x, self.direction.y, self.t = 0, 0, 0

        if self.saut:
            self.direction.x = (self.speed * math.cos(self.angleradian) * self.t)
            self.direction.y = (self.jump_speed * math.sin(self.angleradian) * self.t) - (self.gravity * self.t ** 2 / 2)
            #print(self.t, "/", self.direction.x, self.direction.y)
            self.t += 1

        """else:
            if self.start_time != 0 :
                while self.direction.y <= 0:
                    self.direction.x = (self.speed * math.cos(self.angleradian) * self.t)
                    self.direction.y = (self.jump_speed * math.sin(self.angleradian) * self.t) - (self.gravity * self.t ** 2 / 2)
                    print(self.direction.x,self.direction.y)
                    self.t += 1
                self.start_time = 0"""

        """for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_time = pygame.time.get_ticks()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.end_time = pygame.time.get_ticks()
                    self.t = self.end_time - self.start_time"""
        """if keys[pygame.K_SPACE] :
            if self.touche_appye_d ==1:
                self.touche_appye_d = pygame.time.get_ticks()
            else:
                self.td = pygame.time.get_ticks() - self.touche_appye_d

            self.t = self.t /1000
            self.rect.x += (self.speed * math.cos(self.angleradian)*self.t)
            self.rect.y -= (-1/2 * self.gravity * -(self.td)**2) +  (self.speed * math.sin(self.angleradian)*self.t)
            print(self.t)
            self.t = 0
            self.touche_appye_d = 0"""

        # self.rect.y += self.jump_speed
        # self.rect.x -= self.speed

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

    """def jump(self):
        self.direction.y = self.jump_speed
        self.direction.x = self.speed"""

    def update(self):
        self.input()
        self.rect.x += self.direction.x
        self.rect.y -= self.direction.y
