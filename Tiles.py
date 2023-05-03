import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()

        # Crée une surface jaune pour représenter une tuile
        self.image = pygame.Surface((size, size))
        self.image.fill('yellow')

        # Crée un rectangle avec la position et la taille de l'image
        self.rect = self.image.get_rect(center = position)

    def update(self, x_shift):
        # Modifie la position horizontale de la tuile en fonction de x_shift
        self.rect.x += x_shift
