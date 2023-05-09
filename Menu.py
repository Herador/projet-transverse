import pygame
from setting import *
import time

class menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #boulen pour savoir si les bouton du menu sont activé
        self.Lancement =  True
        self.Level1 = False
        #initialisation du fond blanc
        self.baniere = pygame.image.load("fond.png")

        #initialisation du bouton jouer
        self.bouton_jouer = pygame.image.load("start_btn.png")
        self.bouton_jouer_rect = self.bouton_jouer.get_rect()

        #initialisation des bouton pour acceder aux niveau

        self.bouton_level1 = pygame.image.load("Level1_V1.png")
        self.bouton_level1_rect = self.bouton_level1.get_rect()

        # initialisation du bouton exit
        self.bouton_exit = pygame.image.load("exit_btn.png")
        self.bouton_exit_rect = self.bouton_exit.get_rect()

    def lancement(self,surface):

        surface.blit(self.baniere,(0,0))
        surface.blit(self.bouton_jouer,(0,0))
        surface.blit(self.bouton_exit,(400,400))
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.bouton_jouer_rect.collidepoint(mouse_pos):
                self.Lancement = False
                self.Level1 = True
            #if self.bouton_exit_rect.collidepoint(mouse_pos):
                #pygame.quit()






    #def aide(self):


    #def quitter(self):


    #def retour(self):



    def update(self,surface,level):
        if self.Lancement:
            self.lancement(surface)

        if self.Level1:
            surface.fill('blue')
            level.run()