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
# map_1 = [[1] * 2, [0] * 2] * 2

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

    ElementalWheel(load_image('Whill_1.png'), (width // 2 - 384, height // 2 - 384))
    fire = Elemental(load_image('Fire.png'), (width // 2 - 160, height // 2 - 290))
    water = Elemental(load_image('Water.png'), (width // 2 + 16, height // 2 - 290))
    earth = Elemental(load_image('Earth.png'), (width // 2 - 304, height // 2 - 170))
    wing = Elemental(load_image('Wing.png'), (width // 2 + 160, height // 2 - 170))
    # light = Elemental(load_image('Light.png'), (width // 2 + 16, height // 2 + 146))
    # life = Elemental(load_image('Life.png'), (width // 2 - 160, height // 2 + 146))
    # death = Elemental(load_image('Death.png'), (width // 2 + 160, height // 2 + 26))
    # star = Elemental(load_image('Star.png'), (width // 2 - 304, height // 2 + 26))

    elem_frame = Elemental(load_image('0.png'), (0, 0))
    mode_sprite = Mode(load_image('Mode_1.png'), (width - 54, height - 54))

    element_type = 1
    element_mode = 1
    cooldown = 0
    current_wave = 1

    hero_spell_damage = 1
    hero_spell_speed = 4
    hero_spell_mana = 10
    hero_spell_time = 2

    slow_timer = 0

    btn_color = (174, 186, 0)

    spell_types_spec = {1: ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
                        2: ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
                        3: ((2, 0.6, 2), (0, 0, 2), (1, 1, 1)),
                        4: ((0.5, 2.2, 0.5), (1, 1, 1), (1, 1, 1)),
                        5: ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
                        6: ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
                        7: ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
                        8: ((1, 1, 1), (1, 1, 1), (1, 1, 1))}

    # Enemy(load_image('Seller.png'), enemy_position[0], enemy_position[1], (96, 168), 3, 1, 2,
    #               load_image('Die_sprite.png'), False)

    enemy_sprite_image = load_image('Enemy_list.png')
    enemy_spec = {1: ([load_image('Enemy_list.png').subsurface((288, 0, 96, 96)),
                       load_image('Enemy_list.png').subsurface((384, 0, 96, 96))],
                      (96, 96), 3, 5, 3, load_image('Die_sprite.png')),
                  2: ([load_image('Enemy_list.png').subsurface((0, 0, 96, 192)),
                       load_image('Enemy_list.png').subsurface((96, 0, 96, 192)),
                       load_image('Enemy_list.png').subsurface((192, 0, 96, 192))],
                      (96, 168), 4, 6, 4, load_image('Die_sprite.png')),
                  3: ([load_image('Enemy_list.png').subsurface((0, 192, 96, 192)),
                       load_image('Enemy_list.png').subsurface((96, 192, 96, 192)),
                       load_image('Enemy_list.png').subsurface((192, 192, 96, 192))],
                      (96, 168), 3, 10, 4, load_image('Die_sprite.png')),
                  4: ([load_image('Enemy_list.png').subsurface((288, 192, 96, 96)),
                       load_image('Enemy_list.png').subsurface((384, 192, 96, 96))],
                      (96, 96), 5, 15, 5, load_image('Die_sprite.png')),
                  10: ([load_image('Enemy_list.png').subsurface((288, 0, 96, 96)),
                        load_image('Enemy_list.png').subsurface((384, 0, 96, 96))],
                       (240, 240), 3, 20, 50, load_image('Die_sprite.png')),
                  20: ([load_image('Enemy_list.png').subsurface((0, 0, 96, 192)),
                        load_image('Enemy_list.png').subsurface((96, 0, 96, 192)),
                        load_image('Enemy_list.png').subsurface((192, 0, 96, 192))],
                       (240, 480), 3, 30, 65, load_image('Die_sprite.png')),
                  30: ([load_image('Enemy_list.png').subsurface((0, 192, 96, 192)),
                        load_image('Enemy_list.png').subsurface((96, 192, 96, 192)),
                        load_image('Enemy_list.png').subsurface((192, 192, 96, 192))],
                       (240, 480), 3, 35, 70, load_image('Die_sprite.png')),
                  40: ([load_image('Enemy_list.png').subsurface((288, 192, 96, 96)),
                        load_image('Enemy_list.png').subsurface((384, 192, 96, 96))],
                       (240, 240), 3, 45, 75, load_image('Die_sprite.png'))}

    wave_dif = {1: ((1,), 5),
                10: ((10,), 1),
                2: ((1, 2), 8),
                20: ((20,), 1),
                3: ((1, 2, 3), 14),
                30: ((30,), 1),
                4: ((1, 2, 3, 4), 16),
                40: ((40,), 1),
                5: ((1, 2, 3, 4), 20)}


    def spawn_wave(col, en_type):
        enemies = []  # Создаем пустой список для хранения врагов
        pos = [[[0, width], [-96, 0]],
               [[0, width], [height - 96, height]],
               [[0, 96], [0, height]],
               [[width - 96, width], [0, height]]]
        x = random.choice(pos)[0][0], random.choice(pos)[0][1]
        y = random.choice(pos)[1][0], random.choice(pos)[1][1]
        enemy_positions = [[random.randint(min(x), max(x)), random.randint(min(y), max(y))] for _ in
                           range(col)]
        # enemy_positions = [[random.randint(pos[0][0], pos[0][1]),
        #                     random.randint(pos[1][0], pos[1][1])] for _ in
        #                    range(current_wave)]  # Позиции для каждого врага в волне
        for i in range(len(enemy_positions)):
            if i < len(enemy_positions):
                enemy_position = enemy_positions[i]
                # enemy = Enemy(load_image('Seller.png'), enemy_position[0], enemy_position[1], (96, 168), 3, 1, 2,
                #               load_image('Die_sprite.png'), False)
                enemy_type = enemy_spec[random.choice(en_type)]
            enemy = Enemy(enemy_type[0][0], enemy_type[0], enemy_position[0], enemy_position[1], enemy_type[1],
                          enemy_type[2], enemy_type[3], enemy_type[4], enemy_type[5])
            enemies.append(enemy)  # Добавляем врага в список
        return enemies  # Возвращаем список созданных врагов


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
            if pygame.mouse.get_pressed()[0] and not pause and cooldown == 0:
                if element_mode == 1:
                    cooldown = 10
                    mana_cell = hero_spell_mana * spell_types_spec[element_type][0][2]
                    hero_speed = hero_spell_speed * spell_types_spec[element_type][0][1]
                    hero_damage = hero_spell_damage * spell_types_spec[element_type][0][0]
                    if hero.mana > mana_cell:
                        spell = Spell(load_image('Spell_1.png'), stick.rect.center, pygame.mouse.get_pos(), (32, 32),
                                      element_type, element_mode, hero_speed, hero_damage, hero_spell_time)
                        hero.mana -= mana_cell
                if element_mode == 2:
                    cooldown = 20
                    mana_cell = hero_spell_mana * spell_types_spec[element_type][1][2]
                    hero_speed = 0
                    hero_damage = hero_spell_damage * spell_types_spec[element_type][1][0]
                    if hero.mana > mana_cell:
                        spell = Spell(load_image('Spell_1.png'),
                                      (pygame.mouse.get_pos()[0] - 48, pygame.mouse.get_pos()[1] - 48),
                                      pygame.mouse.get_pos(), (32, 32),
                                      element_type, element_mode, hero_speed, hero_damage, hero_spell_time)
                        hero.mana -= mana_cell
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
                # if len(enemy_sprites) == 0:
                if event.button == pygame.BUTTON_LEFT and button_rect.collidepoint(event.pos):
                    if current_wave % 10 == 0 and current_wave <= 40:
                        spawn_wave(wave_dif[current_wave][1], wave_dif[current_wave][0])
                    elif current_wave < 45:
                        spawn_wave(wave_dif[current_wave // 9 + 1][1] + current_wave // 2,
                                   wave_dif[current_wave // 9 + 1][0])
                    else:
                        spawn_wave(wave_dif[5][1] + current_wave // 2,
                                   wave_dif[5][0])
                    current_wave += 1

        if len(enemy_sprites) == 0:
            btn_color = (174, 186, 0)
        else:
            btn_color = (155, 155, 155)

        for spell in spell_sprites:
            if spell.rect.x > width or spell.rect.x < 0:
                spell_sprites.remove(spell)
            if spell.counter == 30 * spell.time:
                spell_sprites.remove(spell)

        screen.fill((255, 255, 255))

        if not pause and not magica:
            hero.update()
            stick.update(hero.rect.center)
            enemy_sprites.update([hero.rect.x, hero.rect.y], screen)
            spell_sprites.update()
            mode_sprite.image = load_image(f'Mode_{element_mode}.png')
            # Атака врага и нанесение урона врагу, смерть врага
            for enemy in enemy_sprites.sprites():
                # print(pygame.sprite.spritecollide(enemy, enemy_sprites.sprites(), False))

                col_enemys = pygame.sprite.spritecollide(enemy, enemy_sprites.sprites(), False)
                if len(col_enemys) > 1:
                    for i in range(len(col_enemys) - 1):
                        if i % 2 == 0:
                            col_enemys[i].enemy_collision(col_enemys[i + 1], 0.7)
                            col_enemys[i + 1].enemy_collision(col_enemys[i], 0.7)

                # if pygame.sprite.spritecollideany(enemy, elemental_sprites):
                #     enemy.collision(1)
                enemy.attack_player(hero, pygame.time.get_ticks())
                for spell in spell_sprites.sprites():
                    if spell.rect.x > width or spell.rect.x < 0:
                        spell_sprites.remove(spell)
                    if spell.counter == 30 * spell.time:
                        spell_sprites.remove(spell)
                    # if pygame.sprite.collide_rect(enemy, spell):
                    #     enemy.collision(4)
                    if spell.mode == 1:
                        if pygame.sprite.spritecollideany(enemy, spell_sprites):
                            pygame.sprite.groupcollide(enemy_sprites, spell_sprites, False, True)
                            enemy.taking_damage(spell.damage)
                    if spell.mode == 2:
                        if pygame.sprite.spritecollideany(enemy, spell_sprites):
                            if spell.type == 1:
                                if counter % 30 == 0:
                                    enemy.taking_damage(spell.damage)
                            if spell.type == 2:
                                if not enemy.slow:
                                    enemy.slow = True
                                    slow_timer = counter
                                    enemy.speed = 0.9
                                # if counter - slow_timer == 120:
                                #     enemy.slow = False
                                #     enemy.speed *= 200
                                # print(counter - slow_timer)
                            if spell.type == 4:
                                enemy.update(spell.rect, screen)
                            if spell.type == 3:
                                enemy.collision(1)

                if enemy.hp <= 0:
                    enemy.die()
                    if enemy.die_counter == 60:
                        enemy_sprites.remove(enemy)
                        if hero.energy <= 9:
                            hero.energy += 1
        tile_sprites.draw(screen)
        collision_tile_sprites.draw(screen)
        player_sprites.draw(screen)
        enemy_sprites.draw(screen)
        hero.draw_energy(screen, hp_bar_image, font)
        hero.draw_hp(screen, hp_bar_image, font)  # здоровье

        if cooldown:
            hero.draw_cd(screen, cooldown)
            cooldown -= 1

        hero.draw_mana(screen, hp_bar_image, font)
        stick_sprites.draw(screen)
        mode_sprites.draw(screen)
        spell_sprites.draw(screen)
        draw_wave_button(screen, font, current_wave, btn_color)

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
                        if n != 5:
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
