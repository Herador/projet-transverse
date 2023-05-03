# Importation des modules et fichiers nécessaires
import pygame, sys, time
from setting import *
from level import Level
from player import Player
from obstacle import obstacle


# Initialisation de Pygame
pygame.init()

# Création de la fenêtre d'affichage
screen = pygame.display.set_mode((screen_width, screen_height))

# Initialisation de l'horloge pour contrôler le taux de rafraîchissement
tickRate = pygame.time.Clock()

# Initialisation du niveau et des variables de temps
level = Level(Lvl_1_map, screen)
start_time = 0
t = 0

# Création d'une instance de la classe Player
player = Player((100, 200))

def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            player.vie -= 1
            obstacles.remove(obstacle)
            print("Il vous reste", player.vie, "vies.")
            if player.vie == 0:
                pygame.quit()
                sys.exit()

# Boucle principale du jeu
while True:

    # Gestion des événements Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quitter le jeu si on appuie sur la croix de fermeture de la fenêtre
            pygame.quit()
            sys.exit()

        # Obtention des touches enfoncées
        keys = pygame.key.get_pressed()

    # Remplissage de l'écran avec une couleur bleue
    screen.fill('blue')

    # Exécution du niveau
    level.run()

    # Mise à jour de l'affichage
    pygame.display.update()

    # Contrôle du taux de rafraîchissement
    tickRate.tick(60)

    # Vérifie les collisions avec les obstacles
    check_collision(player,obstacle)
