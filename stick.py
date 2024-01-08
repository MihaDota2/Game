import pygame
import math

stick_sprites = pygame.sprite.Group()


class Stick(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(stick_sprites)
        self.sprite = image
        # self.image = pygame.transform.scale(image, size)
        self.image = image
        self.image_copy = pygame.transform.scale(image, (110, 110))
        # self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

        # self.speed = speed
        # self.damage = damage

    def input(self):
        pass

    def rotate(self, center):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        new_image = pygame.transform.rotate(self.image_copy, angle - 45)
        # self.rect = new_image.get_rect(center=self.rect.center)
        self.rect = new_image.get_rect(center=center)

        self.rect.y += 24
        self.image = new_image

    def animation(self):
        pass

    def move(self, coords):
        pass

    def update(self, center):
        self.rotate(center)
        # self.move(coords)
        # self.animation()
