import pygame
from tile import Tile
from tile import CollisionTile


class Map:
    # tileset = (image, width, height)
    def __init__(self, map, image, width, height):
        self.map = map
        self.image = image
        self.width = width
        self.height = height

        self.col_tiles = {0: False, 1: True}

        self.display_surface = pygame.display.get_surface()
        # self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

    def tiles(self):
        image_tiles = []
        for y in range(0, self.height, 96):
            for x in range(0, self.width, 96):
                image_tiles.append(self.image.subsurface((x, y, 96, 96)))
        return image_tiles

    def generate(self):
        image_tiles = self.tiles()
        x, y = 0, 0
        for t_y in self.map:
            for t_x in t_y:
                if self.col_tiles[t_x]:
                    Tile(image_tiles[t_x], x, y)
                else:
                    CollisionTile(image_tiles[t_x], x, y)
                x += 96
            x = 0
            y += 96

    # def run(self):
    #     self.visible_sprites.custom_draw(self.player)
    #     self.visible_sprites.update()

# class YSortCameraGroup(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#         self.half_width = self.display_surface.get_size()[0] // 2
#         self.half_height = self.display_surface.get_size()[1] // 2
#         self.offset = pygame.math.Vector2()
#
#     def custom_draw(self, player):
#         self.offset.x = player.rect.centerx - self.half_width
#         self.offset.y = player.rect.centery - self.half_height
#
#         for sprite in self.sprites():
#             offset_pos = sprite.rect.topleft - self.offset
#             self.display_surface.blit(sprite.image, offset_pos)
