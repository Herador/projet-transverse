import pygame, sys, time
from setting import *
from level import Level
from player import Player

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((screen_width,screen_height))
tickRate = pygame.time.Clock()
level1 = Level(Lvl_2_map,Lvl_1_map,Lvl_Tuto_map,screen)
start_time = 0
t = 0


while 1 and Player !=0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #level1.run()
    level1.update(screen,level1)
    pygame.display.update()
    tickRate.tick(level1.tick)

