import pygame
from functions import load_image

player_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(player_sprites)
        self.sprite = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.flag_right = True

        self.speed = 5

    def input(self):
        move_map = {pygame.K_w: (0, 1),
                    pygame.K_s: (0, -1),
                    pygame.K_a: (1, 0),
                    pygame.K_d: (-1, 0)}

        pressed = pygame.key.get_pressed()
        move = [move_map[key] for key in move_map if pressed[key]]
        return move

    def animation(self):
        move = self.input()
        self.counter += 1
        if move:
            if self.counter > 9:
                self.counter = 0
            image_spriteR = [self.sprite.subsurface((0, 0, 96, 192)),
                             self.sprite.subsurface((96, 0, 96, 192)),
                             self.sprite.subsurface((192, 0, 96, 192))]

            image_spriteL = [self.sprite.subsurface((0, 192, 96, 192)),
                             self.sprite.subsurface((96, 192, 96, 192)),
                             self.sprite.subsurface((192, 192, 96, 192))]
            if move[0][0] == 1 or move[-1][0] == 1:
                self.image = image_spriteL[self.counter // 3 - 1]
            elif move[0][0] == -1 or move[-1][0] == -1:
                self.image = image_spriteR[self.counter // 3 - 1]
            else:
                if self.flag_right:
                    self.image = image_spriteR[self.counter // 3 - 1]
                else:
                    self.image = image_spriteL[self.counter // 3 - 1]
        else:
            if self.counter > 20:
                self.counter = 0
            image_spriteR = [self.sprite.subsurface((288, 0, 96, 192)),
                            self.sprite.subsurface((384, 0, 96, 192))]
            image_spriteL = [self.sprite.subsurface((288, 192, 96, 192)),
                            self.sprite.subsurface((384, 192, 96, 192))]
            if self.flag_right:
                image_sprite = image_spriteR
            else:
                image_sprite = image_spriteL
            self.image = image_sprite[self.counter // 10 - 1]

    def move(self):
        move = self.input()
        if move:
            if move[0] != move[-1]:
                move = [(move[0][0] + move[-1][0], move[0][1] + move[-1][1])]
            move_vectorL = move[0][0] * self.speed
            move_vectorT = move[0][1] * self.speed
            self.rect.top -= move_vectorT
            self.rect.left -= move_vectorL
            # print(self.flag_right, move)
            if move[0][0] == 1:
                self.flag_right = False
            elif move[0][0] == -1:
                self.flag_right = True

    def update(self):
        self.move()
        self.animation()
