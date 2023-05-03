import pygame
from Tiles import Tile
from setting import tile_size, screen_width, screen_height, obstacle_size
from player import Player
from Enemies import Pate_a_choux
from Enemies import Enemies
from obstacle import obstacle

class Level:
    def __init__(self, level_data, surface):
        #configuration du niveau
        self.display_surface = surface
        self.setup_level(level_data)
        self.shift = 0

    def setup_level(self, layout):
        self.Tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monstres = pygame.sprite.GroupSingle()
        self.obstacles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x,y), tile_size)
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
                    obs = obstacle((x,y), obstacle_size)
                    self.obstacles.add(obs)

    def scroll_x(self):
        player = self.player.sprite
        Position_x = player.rect.centerx
        #joueur
        if (Position_x < (screen_width / 2)-10) :
            self.shift = 10
            player.rect.x += 10
        elif (Position_x > (screen_width - (screen_width / 2)+10)) :
            self.shift = -10
            player.rect.x -= 10
        else:
            self.shift = 0

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

        for sprite in self.obstacles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite

        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for sprite in self.obstacles.sprites():
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

        self.obstacles.update(self.shift)
        self.obstacles.draw(self.display_surface)

        #Capacity


        #player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)

        #enemie
        self.monstres.draw(self.display_surface)
        self.monstres.update()

