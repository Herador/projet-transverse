import pygame
from Tiles import Tile
from setting import tile_size, screen_width, screen_height, obstacle_size
from player import Player
from Enemies import Pate_a_choux
from Enemies import Enemies
from objet import obstacle
from objet import drapeau
from Menu import menu

class Level:
    def __init__(self,level_data,surface):
        #Debut du niveau
        self.debut = False

        #configuration du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.shift = 0

        #debut/fin des niveaux:
        self.level = True



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

        #print(Position_x)
        #print(Position_y)

        #monstres = self.monstres.sprite
        #joueur

        if (Position_x < (screen_width / 2)-10) :
            self.shift = 10
            player.rect.x += 10
            #player.speed = 10


            #self.shift = player.speed
            #player.speed = 0
            #monstres.vitesse = 3

        elif (Position_x > (screen_width - (screen_width / 2)+10)) :
            self.shift = -10
            player.rect.x -= 10
            #player.speed = -10


            #self.shift= -player.speed
            #player.speed = 0
            #monstres.vitesse = -3

        else:
            self.shift = 0
            #player.speed = 0
            #monstres.vitesse = 3

        #monstre

    '''
    def scroll_y(self):
        player = self.player.sprite
        Position_y = player.rect.centery

        if (Position_y < (screen_height / 2)-10) :
            self.shift = 10
            player.rect.x += 10
            #player.speed = 10


            #self.shift = player.speed
            #player.speed = 0
            #monstres.vitesse = 3

        elif (Position_y > (screen_height - (screen_width / 2)+10)) :
            self.shift = -10
            player.rect.y -= 10
            #player.speed = -10


            #self.shift= -player.speed
            #player.speed = 0
            #monstres.vitesse = -3
    '''

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
                self.mort()

        for col in colision_p:
            if player.rect.colliderect(col.rect):
                Player.saut = False

        #fin du level
        for i in Drapeau:
            if player.rect.colliderect(i.rect):
                self.level = False



    def mort(self):
        pygame.quit()


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

        #enemie
        self.monstres.draw(self.display_surface)
        self.monstres.update()

