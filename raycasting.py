import pygame as pg
import math
from settings import *

"""
Надо направить заданное количество лучей в определенное поле зрения персонажа
Для каждого луча надо вычислить точку пересечения с препятствием
Представляем поле как сетку
Пересечение с вертикальными и горизонтальными линиями надо расчитывать как два отдельных случая:
Если пересечение с вертикалями, то луч вдоль оси ч перемещается равными отрезками dx, нам надо высчитать dy
Если пересечение с горизонталями, то обратно-пропорционально мы знаем dy, но надо вычислить dx
На основе dx и dy мы можем расчитать глубину и определить расстояние до стены для каждого луча
"""
class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos #координаты игрока на карте
        x_map, y_map = self.game.player.map_pos #координаты его плитки
        #вычесть половину значения поля зрения из угла игрока
        #так мы вычисляем угол первого луча и прибавляем 0.0001 чтобы можно было делить на ноль
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        #теперь расчитаем углы каждого луча
        for ray in range (NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            #verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a #расстояние от одной левой точки клетки до правой точки клетки
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            if  depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # remove fisheye effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projection
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # draw walls
            color = [255 / (1 + depth ** 5 * 0.00002)]*3
            pg.draw.rect(self.game.screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            ray_angle += DELTA_ANGLE




    def update(self):
        self.ray_cast()