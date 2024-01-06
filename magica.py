import pygame
import math

magica_sprites = pygame.sprite.Group()


class ElementalWheel(pygame.sprite.Sprite):
    def __init__(self, image, coords):
        super().__init__(magica_sprites)
        self.sprite = image
        # self.image = pygame.transform.scale(image, size)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]

    def input(self):
        pass

    def animation(self):
        pass

    def move(self):
        pass

    def update(self):
        self.move()
        self.animation()
