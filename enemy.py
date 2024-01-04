import pygame

enemy_sprites = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, size, speed, damage):
        super().__init__(enemy_sprites)
        self.sprite = image
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

        self.speed = speed
        self.damage = damage

    def input(self):
        pass

    def animation(self):
        pass

    def move(self, coords):
        x = coords[0] - self.rect.x
        y = coords[1] - self.rect.y
        vector_x = (1 if x > 0 else -1)
        vector_y = (1 if y > 0 else -1)
        if x != 0:
            self.rect.x += self.speed * vector_x
        if y != 0:
            self.rect.y += self.speed * vector_y

    def collision(self):
        pass
        # move = self.input()
        # if move:
        #     self.rect.top += move[0][1] * self.speed
        #     self.rect.left += move[0][0] * self.speed
        #     self.rect.top += move[-1][1] * self.speed
        #     self.rect.left += move[-1][0] * self.speed

    # def not_move(self):

    def update(self, coords):
        self.move(coords)
        self.animation()
