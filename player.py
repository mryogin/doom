import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        """
        зная направление персонажа и его скорость, можем расчитать dx, dy координат,
        на которые он должен переместиться при нажатии кнопки управления персонажем

        Для кнопки W (вперед
        dx = +SPEED * cos(a) | dy = +SPEED * sin(a)
        Для кнопки S (назад)
        dx = -SPEED * cos(a) | dy = -SPEED * sin(a)
        Для кнопки A (влево)
        dx = +SPEED * cos(a) | dy = -SPEED * sin(a)
        Для кнопки D (вправо)
        dx = -SPEED * cos(a) | dy = +SPEED * sin(a)

        Чтобы скорость игрока не зависила от частоты кадров,
        надо получить дельту времени для каждого кадра
        """
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx +=  speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)


        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        #попали ли проверенные координаты в стену
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
#        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
#                    (self.x * 100 + WIDTH * math.cos(self.angle),
#                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property #свойства
    def pos(self):
        return self.x, self.y  #возвращает координаты местоположения персонажа

    @property
    def map_pos(self):
        return int(self.x), int(self.y) # возвращает на какой плитке карты находится персонаж

