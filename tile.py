import pygame

tile_sprites = pygame.sprite.Group()
collision_tile_sprites = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(tile_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class CollisionTile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(collision_tile_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # def update(self, pos=()):
    #     if pos.collidepoint(pygame.mouse.get_pos()):
    #         self.image = load_image("boom.png")
