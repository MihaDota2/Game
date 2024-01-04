import os
import pygame
from functions import load_image
from map import Map
from tile import tile_sprites
from tile import collision_tile_sprites
from player import Player
from player import player_sprites
from enemy import Enemy
from enemy import enemy_sprites

map_1 = [[1] * 15] * 10

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1440, 960
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    hero = Player(load_image('AnimationListCharacter_3.png'), width // 2 - 48, height // 2 - 96)
    move = hero.input()

    running = True
    counter = 0
    tile_sprites.draw(screen)
    player_sprites.draw(screen)

    Level_Map = Map(map_1, load_image('tileset_1.png'), 192, 92)
    Level_Map.generate()

    tile_sprites.draw(screen)
    # collision_tile_sprites.draw(screen)
    enemy = Enemy(load_image('Seller.png'), 0, 0, (96, 168), 3, 1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        hero.update()
        enemy.update([hero.rect.x, hero.rect.y])

        tile_sprites.draw(screen)
        collision_tile_sprites.draw(screen)

        player_sprites.draw(screen)
        enemy_sprites.draw(screen)
        pygame.display.flip()
        counter += 1
        clock.tick(30)

        if (pygame.sprite.spritecollideany(hero, collision_tile_sprites) or hero.rect.top < 0 or hero.rect.top > 792
                or hero.rect.left < 0 or hero.rect.right > 1440):
            hero.collision()
        # if pygame.sprite.spritecollideany(hero, enemy_sprites):
        #     print(1)

        # elif pygame.sprite.spritecollideany(hero, tile_sprites):
        #     print(len(tile_sprites))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pygame.quit()

# Проверка_2
