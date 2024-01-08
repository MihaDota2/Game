import pygame

enemy_sprites = pygame.sprite.Group()
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, size, speed, damage, hp, die_im, slow):
        super().__init__(enemy_sprites)
        self.sprite = image
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.last_attack_time = pygame.time.get_ticks()
        self.attack_radius = 20

        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.damage_counter = 0
        self.die_counter = 0
        self.die_image = die_im
        self.image_copy = self.image

        self.slow = False

    def input(self):
        pass

    def attack_player(self, player, current_time):
        # Расчет расстояния до игрока
        distance = pygame.math.Vector2(self.rect.center) - pygame.math.Vector2(player.rect.center)
        if distance.length() <= self.attack_radius:
            # Проверка, прошло ли 5 секунд с последней атаки
            if current_time - self.last_attack_time > 3000:  # 5000 миллисекунд = 5 секунд
                player.hp -= 0  # Нанесение урона игроку
                self.last_attack_time = current_time  # Обновление времени последней атаки

    def taking_damage(self, damage):
        self.damage_counter = 30
        self.hp -= damage

    def die(self):
        self.die_counter += 1
        self.speed = 0
        self.image = pygame.transform.scale(self.die_image, (66, 48))

    def animation(self):
        pass
        # if self.damage_counter:
        #     pass
        #     colorImage = pygame.Surface(self.image_copy.get_size()).convert_alpha()
        #     colorImage.fill((255, 0, 0))
        #     self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        #     self.damage_counter -= 1
        #     print(salf.damage_counter)
        # else:
        #     colorImage = pygame.Surface(self.image_copy.get_size()).convert_alpha()
        #     colorImage.fill((0, 0, 0))
        #     self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def move(self, coords):
        x = coords[0] - self.rect.x
        y = coords[1] - self.rect.y
        vector_x = (1 if x > 0 else -1)
        vector_y = (1 if y > 0 else -1)
        self.vector_x = vector_x
        self.vector_y = vector_y
        if x != 0 and y != 0 and abs(x) > self.speed and abs(y) > self.speed:
            if max(abs(x), abs(y)) == abs(x):
                self.rect.x += self.speed * vector_x
                self.rect.y += self.speed * vector_y * (abs(y) / abs(x))
            else:
                self.rect.x += self.speed * vector_x * (abs(x) / abs(y))
                self.rect.y += self.speed * vector_y
        if abs(x) < self.speed:
            self.rect.y += self.speed * vector_y
        if abs(y) < self.speed:
            self.rect.x += self.speed * vector_x

    def collision(self, k):
        # move = self.input()
        self.rect.top -= self.vector_y * self.speed * k
        self.rect.left -= self.vector_x * self.speed * k

    def enemy_collision(self, object, k):
        speed = object.speed
        vector = [object.vector_x, object.vector_y]
        coords = [object.rect.x, object.rect.y]
        x = coords[0] - self.rect.x
        y = coords[1] - self.rect.y
        vector_x = (1 if x > 0 else -1)
        vector_y = (1 if y > 0 else -1)

        self.rect.left -= vector_x * self.speed * k
        self.rect.top -= vector_y * self.speed * k

        print(speed, vector, coords)

        # v = random.choice([-1, 1])
        #
        # # move = self.input()
        # self.rect.top -= v * self.vector_y * self.speed * k
        # self.rect.left -= v * self.vector_x * self.speed * k


    # def collision(self):
    #     move = self.input()
    #     if move:
    #         self.rect.top += move[0][1] * self.speed
    #         self.rect.left += move[0][0] * self.speed
    #         self.rect.top += move[-1][1] * self.speed
    #         self.rect.left += move[-1][0] * self.speed

    def update(self, coords):
        self.move(coords)
        self.animation()
