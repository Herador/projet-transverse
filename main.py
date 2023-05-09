import pygame, sys, time
from setting import *
from level import Level
from player import Player
from Menu import menu

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
tickRate = pygame.time.Clock()
level1 = Level(Lvl_1_map,screen)
Menu = menu()
start_time = 0
t = 0


while 1 and Player !=0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Menu.update(screen,level1)

    pygame.display.update()
    tickRate.tick(60)

