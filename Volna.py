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
from magica import ElementalWheel
from magica import magica_sprites
from magica import Elemental
from magica import elemental_sprites
from magica import Mode
from magica import mode_sprites
from PIL import Image

from enemy import Enemy

pygame.init()




def draw_wave_button(screen, font, wave_number):
    button_text = f"Вызвать новую волну {wave_number}"
    button_rect = pygame.Rect(screen.get_width() - 300, 10, 290, 30)
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
    text_surface = font.render(button_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
