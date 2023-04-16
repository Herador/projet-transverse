import pygame
from Tiles import Tile
from setting import tile_size, screen_width, screen_height
from player import Player
from Enemies import Pate_a_choux
from Enemies import Enemies

class Level:
    def __init__(self,level_data,surface):

        #configuration du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.shift = 0

    def setup_level(self,layout):
        self.Tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monstres = pygame.sprite.GroupSingle()


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

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        enemies = self.monstres.sprites()


        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        #vie du joueur
        '''for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                self.mort()'''


    def vertical_collision(self):
        player = self.player.sprite
        #player.apply_gravity()




        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def mort(self):
        pygame.quit()


    def run(self):
        #level
        self.Tiles.update(self.shift)
        self.Tiles.draw(self.display_surface)
        self.scroll_x()

        #Capacity


        #player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)

        #enemie
        self.monstres.draw(self.display_surface)
        self.monstres.update()

