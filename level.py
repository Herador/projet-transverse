import time

import pygame
from Tiles import Tile
from setting import tile_size, screen_width, screen_height, obstacle_size
from player import Player
from Enemies import Pate_a_choux
from Enemies import Enemies
from objet import obstacle
from objet import drapeau

class Level:
    def __init__(self,level_data,surface):
        #Debut du niveau

        #configuration du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.shift = 0

        #debut/fin des niveaux:
        self.game_over = True

        #nombre vie du joueur
        self.vie = 5



        #----------------------------------------------------------------
        #menu
        # boulen pour savoir si les bouton du menu sont activé
        self.Lancement = True
        self.Level1 = False
        # initialisation du fond blanc
        self.baniere = pygame.image.load("fond.png")

        # initialisation du bouton jouer
        self.bouton_jouer = pygame.image.load("start_btn.png")
        self.bouton_jouer_rect = self.bouton_jouer.get_rect()

        # initialisation des bouton pour acceder aux niveau

        self.bouton_level1 = pygame.image.load("Level1_V1.png")
        self.bouton_level1_rect = self.bouton_level1.get_rect()

        # initialisation du bouton exit
        self.bouton_exit = pygame.image.load("exit_btn.png")
        self.bouton_exit_rect = self.bouton_exit.get_rect()

        # initialisation de l'ecran de  mort
        self.ecran_de_mort = pygame.image.load("fond.png")
        self.ecran_game_over = pygame.image.load("game-over.png")
        self.bouton_restart = pygame.image.load("Restart.png")
        self.bouton_restart_rect = self.bouton_restart.get_rect()

    def lancement(self,surface):

        surface.blit(self.baniere,(0,0))
        surface.blit(self.bouton_jouer,(0,0))
        surface.blit(self.bouton_exit,(400,400))
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.bouton_jouer_rect.collidepoint(mouse_pos):
                self.Lancement = False
                self.Level1 = True




    def setup_level(self,layout):
        self.Tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monstres = pygame.sprite.GroupSingle()
        self.obstacles = pygame.sprite.Group()
        self.drapeau = pygame.sprite.Group()


        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x,y),tile_size)
                    self.Tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if col == 'B':
                    monstres_sprite = Enemies((x,y),"BaguetteBaguette.png")
                    self.monstres.add(monstres_sprite)
                if col == 'C':
                    monstres_sprite = Pate_a_choux((x,y), "pate_a_choux_v0.png")
                    self.monstres.add(monstres_sprite)
                if col == 'O':
                    obs = obstacle((x, y), obstacle_size)
                    self.obstacles.add(obs)
                if col == 'D':
                    Drapeau = drapeau((x,y),obstacle_size)
                    self.drapeau.add(Drapeau)

    def scroll_x(self):
        player = self.player.sprite
        Position_x = player.rect.centerx



        if (Position_x < (screen_width / 6)):
            self.shift = 1000
            player.rect.x += 1000


        elif (Position_x > (screen_width - (screen_width / 6))):
            self.shift = -1000
            player.rect.x -= 1000


        else:
            self.shift = 0


    def horizontal_collision(self,surface):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        enemies = self.monstres.sprites()
        obstacles = self.obstacles.sprites()
        colision_p = self.Tiles.sprites()
        Drapeau = self.drapeau.sprites()

        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = -10

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 10



                if abs(player.rect.bottom - sprite.rect.top) < 25 and player.direction.y < 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.direction.x = 0
                    player.saut = False
                    player.stop_traj = False
                if abs(player.rect.top - sprite.rect.bottom)<25 and player.direction.y > 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


        #vie du joueur
        for ob in obstacles:
            if player.rect.colliderect(ob.rect):
                self.game_over = False
                self.Level1 = False
        for col in colision_p:
            if player.rect.colliderect(col.rect):
                Player.saut = False



    def gameover(self,surface):
        if self.game_over == False:
            surface.fill('black')
            surface.blit(self.ecran_game_over,(500,100))

            surface.blit(self.bouton_restart,(550,300))
            rect_x,rect_y,rect_height,rect_width = 550,300,126,240
            rect =(550,300,126,240)
            pygame.draw.rect(surface, (250,250,250), (rect_x, rect_y, rect_width, rect_height))
            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                    print(mouse_y)
                    print(mouse_x)
                    self.game_over = True
                    self.Level1 = True


    def run(self):
        #level
        self.Tiles.update(self.shift)
        self.Tiles.draw(self.display_surface)
        self.scroll_x()

        #obsacle
        self.obstacles.update(self.shift)
        self.obstacles.draw(self.display_surface)

        #drapeau
        self.drapeau.update(self.shift)
        self.drapeau.draw(self.display_surface)
        #Capacity


        #player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)

        #game over
        self.gameover(self.display_surface)

        #enemie
        self.monstres.draw(self.display_surface)
        self.monstres.update()



    def update(self,surface,level):
        if self.Lancement:
            self.lancement(surface)
        if self.game_over == False:
            self.gameover(surface)
        if self.Level1:
            surface.fill('blue')
            level.run()
