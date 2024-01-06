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
from stick import Stick
from stick import stick_sprites
from spell import Spell
from spell import spell_sprites
from functions import function_sprites
from functions import Pause

map_1 = [[1] * 15] * 10
#здоровье
pygame.font.init()  # Инициализация модуля шрифтов
font = pygame.font.Font(None, 36)  # Создание объекта шрифта

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1440, 960
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    hero = Player(load_image('AnimationListCharacter_3.png'), width // 2 - 48, height // 2 - 96)
    # Загрузка изображения полоски здоровья
    hp_bar_image = load_image('hp.png', color_key=-1)
    move = hero.input()

    running = True
    pause = False
    magica = False
    counter = 0
    tile_sprites.draw(screen)
    player_sprites.draw(screen)

    Level_Map = Map(map_1, load_image('tileset_1.png'), 192, 92)
    Level_Map.generate()

    tile_sprites.draw(screen)
    # collision_tile_sprites.draw(screen)
    enemy = Enemy(load_image('Seller.png'), 0, 0, (96, 168), 3, 1)
    stick = Stick(load_image('Stick_2.png'), 500, 500)
    spell = Spell(load_image('Spell_1.png'), (200, 200), pygame.mouse.get_pos(), (0, 0),
                  1, 1, 1, 2)
    pause_btn = Pause(load_image('pause_button.png'), (width // 2 - 192, height // 2 - 192))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(stick.rect.center)
                spell = Spell(load_image('Spell_1.png'), stick.rect.center, pygame.mouse.get_pos(), (32, 32),
                              1, 12, 1, 3)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if not pause:
                    magica = not magica

        for spell in spell_sprites:
            if spell.rect.x > width or spell.rect.x < 0:
                spell_sprites.remove(spell)
                print(len(spell_sprites))
            if spell.counter == 30 * spell.time:
                spell_sprites.remove(spell)

        screen.fill((255, 255, 255))

        if not pause and not magica:
            hero.update()
            stick.update(hero.rect.center)
            enemy.update([hero.rect.x, hero.rect.y])
            spell_sprites.update()

        tile_sprites.draw(screen)
        collision_tile_sprites.draw(screen)
        player_sprites.draw(screen)
        hero.draw_hp(screen, hp_bar_image, font) # здоровье
        hero.draw_mana(screen, hp_bar_image, font)
        # enemy_sprites.draw(screen)
        stick_sprites.draw(screen)
        current_time = pygame.time.get_ticks()
        #Атака врага
        for enemy in enemy_sprites:
            enemy.attack_player(hero, current_time)
        spell_sprites.draw(screen)
        if pause:
            function_sprites.draw(screen)

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
