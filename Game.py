import os
import random

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
from magica import ElementalWheel
from magica import magica_sprites
from magica import Elemental
from magica import elemental_sprites
from magica import Mode
from magica import mode_sprites
from Volna import draw_wave_button

map_1 = [[1] * 15] * 10
# здоровье
pygame.font.init()  # Инициализация модуля шрифтов
font = pygame.font.Font(None, 36)  # Создание объекта шрифта

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1440, 960
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    button_rect = pygame.Rect(screen.get_width() - 300, 10, 290, 30)

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
    # enemy0 = Enemy(load_image('Seller.png'), 0, 0, (96, 168), 3, 1, 2, load_image('Star.png'))
    # enemy1 = Enemy(load_image('Seller.png'), 96, 0, (96, 168), 3, 1, 2, load_image('Star.png'))
    # enemy2 = Enemy(load_image('Seller.png'), 12, 0, (96, 168), 3, 1, 2, load_image('Star.png'))
    # enemy3 = Enemy(load_image('Seller.png'), 24, 0, (96, 168), 3, 1, 2, load_image('Star.png'))

    stick = Stick(load_image('Stick_2.png'), 500, 500)
    spell = Spell(load_image('Spell_1.png'), (0, 0), pygame.mouse.get_pos(), (0, 0),
                  1, 1, 1, 1, 0)
    pause_btn = Pause(load_image('pause_button.png'), (width // 2 - 192, height // 2 - 192))

    ElementalWheel(load_image('Elemental_Whell_1.png'), (width // 2 - 384, height // 2 - 384))
    fire = Elemental(load_image('Fire.png'), (width // 2 - 160, height // 2 - 290))
    water = Elemental(load_image('Water.png'), (width // 2 + 16, height // 2 - 290))
    earth = Elemental(load_image('Earth.png'), (width // 2 - 304, height // 2 - 170))
    wing = Elemental(load_image('Wing.png'), (width // 2 + 160, height // 2 - 170))
    light = Elemental(load_image('Light.png'), (width // 2 + 16, height // 2 + 146))
    life = Elemental(load_image('Life.png'), (width // 2 - 160, height // 2 + 146))
    death = Elemental(load_image('Death.png'), (width // 2 + 160, height // 2 + 26))
    star = Elemental(load_image('Star.png'), (width // 2 - 304, height // 2 + 26))
    elem_frame = Elemental(load_image('0.png'), (0, 0))
    mode_sprite = Mode(load_image('Mode_1.png'), (width - 54, height - 54))

    element_type = 1
    element_mode = 1
    cooldown = 0
    current_wave = 1


    def spawn_wave(current_wave):
        enemies = []  # Создаем пустой список для хранения врагов
        pos = random.choice([[[0, width], [0, 96]], [[0, width], [height - 96, height]], [[width - 96, width], [0, 96]],
                             [[width - 96, width], [height - 96, height]]])
        enemy_positions = [[random.randint(pos[0][0], pos[0][1]),
                            random.randint(pos[1][0], pos[1][1])] for _ in
                           range(current_wave * 2 + 1)]  # Позиции для каждого врага в волне
        print(enemy_positions)
        for i in range(len(enemy_positions)):
            if i < len(enemy_positions):
                enemy_position = enemy_positions[i]
            enemy = Enemy(load_image('Seller.png'), enemy_position[0], enemy_position[1], (96, 168), 3, 1, 2,
                          load_image('Star.png'))
            enemies.append(enemy)  # Добавляем врага в список
        return enemies  # Возвращаем список созданных врагов


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
            if pygame.mouse.get_pressed()[0] and not pause and cooldown == 0:
                cooldown = 10
                if hero.mana > 20:
                    spell = Spell(load_image('Spell_1.png'), stick.rect.center, pygame.mouse.get_pos(), (32, 32),
                                  element_type, element_mode, 12, 1, 3)
                    hero.mana -= 20
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if not pause:
                    magica = not magica

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                element_mode = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                element_mode = 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                element_mode = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and button_rect.collidepoint(event.pos):
                    spawn_wave(current_wave)
                    current_wave += 1

        for spell in spell_sprites:
            if spell.rect.x > width or spell.rect.x < 0:
                spell_sprites.remove(spell)
            if spell.counter == 30 * spell.time:
                spell_sprites.remove(spell)

        screen.fill((255, 255, 255))

        if not pause and not magica:
            hero.update()
            stick.update(hero.rect.center)
            enemy_sprites.update([hero.rect.x, hero.rect.y])
            spell_sprites.update()
            mode_sprite.image = load_image(f'Mode_{element_mode}.png')
            # Атака врага и нанесение урона врагу, смерть врага
            for enemy in enemy_sprites.sprites():
                enemy.attack_player(hero, pygame.time.get_ticks())
                for spell in spell_sprites.sprites():
                    if spell.rect.x > width or spell.rect.x < 0:
                        spell_sprites.remove(spell)
                    if spell.counter == 30 * spell.time:
                        spell_sprites.remove(spell)
                    if pygame.sprite.spritecollideany(enemy, spell_sprites):
                        enemy.taking_damage(spell.damage)
                        pygame.sprite.groupcollide(enemy_sprites, spell_sprites, False, True)
                if enemy.hp <= 0:
                    enemy.die()
                    if enemy.die_counter == 60:
                        enemy_sprites.remove(enemy)

        tile_sprites.draw(screen)
        collision_tile_sprites.draw(screen)
        player_sprites.draw(screen)
        enemy_sprites.draw(screen)
        hero.draw_hp(screen, hp_bar_image, font)  # здоровье

        if cooldown:
            hero.draw_cd(screen, cooldown)
            cooldown -= 1

        hero.draw_mana(screen, hp_bar_image, font)
        stick_sprites.draw(screen)
        mode_sprites.draw(screen)
        spell_sprites.draw(screen)
        draw_wave_button(screen, font, current_wave)

        if magica:
            n = 0
            magica_sprites.draw(screen)
            elemental_sprites.draw(screen)
            for elem in elemental_sprites:
                n += 1
                if n == 9:
                    n = 0
                if elem.rect.collidepoint(pygame.mouse.get_pos()):
                    elem_frame.image = load_image('Frame.png')
                    elem_frame.rect = elem.rect
                    if n != 0 and pygame.mouse.get_pressed()[0]:
                        element_type = n
                        magica = False
                else:
                    elem_frame.image = load_image('0.png')

        if pause:
            function_sprites.draw(screen)

        pygame.display.flip()

        counter += 1
        clock.tick(30)

        if (pygame.sprite.spritecollideany(hero, collision_tile_sprites) or hero.rect.top < 0 or hero.rect.top > 792
                or hero.rect.left < 0 or hero.rect.right > 1440):
            hero.collision()

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pygame.quit()
