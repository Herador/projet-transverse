import pygame

class obstacle(pygame.sprite.Sprite):
    # Classe représentant un obstacle dans le jeu.

    def __init__(self, position, size):

        # Initialise un obstacle avec sa position et sa taille.
        super().__init__()

        # Crée une surface rouge de la taille de l'obstacle.
        self.image = pygame.Surface((size, size))
        self.image.fill('red')

        # Récupère le rectangle englobant l'image.
        self.rect = self.image.get_rect(center = position)

    def update(self, x_shift):
        # Met à jour la position de l'obstacle en fonction du décalage horizontal.
        self.rect.x += x_shift

class drapeau(pygame.sprite.Sprite):
    def __init__(self, position, size):
        # Initialise un obstacle avec sa position et sa taille.
        super().__init__()

        # Initialise l'image du drapeau
        self.image = pygame.Surface((size,size))
        self.image.fill('black')
        # Récupère le rectangle englobant l'image.
        self.rect = self.image.get_rect(center=position)

    def update(self, x_shift):
        # Met à jour la position de l'obstacle en fonction du décalage horizontal.
        self.rect.x += x_shift

