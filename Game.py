import os
import pygame
from functions import load_image
from map import Map
from map import tile_sprites
from player import Player
from player import player_sprites


map_1 = [[0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 1, 1, 1, 0],
         [0, 0, 1, 0, 0]]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 480, 480
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    hero = Player(load_image('AnimationListCharacter_2.png'), 0, 0)
    move = hero.input()

    running = True
    counter = 0
    tile_sprites.draw(screen)
    player_sprites.draw(screen)

    Level_Map = Map(map_1, load_image('tileset_1.png'), 192, 92)
    Level_Map.generate()
    tile_sprites.draw(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        hero.update()
        tile_sprites.draw(screen)
        player_sprites.draw(screen)
        pygame.display.flip()
        counter += 1
        clock.tick(30)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
