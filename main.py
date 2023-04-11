import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *


class Game:
    def __init__(self):
        pg.init()  #инициализация игровых модулей
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES) #экран для рендеринга
        self.clock = pg.time.Clock()  # создаем экземпляр класса часов
        self.delta_time = 1 #получаем дельту времени чтобы персонаж двигался плавно независимо от ФПС
        self.new_game()

    def new_game (self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRender(self)
        self.raycasting = RayCasting(self)


    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip() #отображаем экран
        self.delta_time = self.clock.tick(FPS) #получаем дельту времени
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
#        self.screen.fill('black') #на каждой итерации окрашиваем экран в черный цвет
        self.object_renderer.draw()
#        self.map.draw()
#        self.player.draw()

    def check_events(self):
        """Если из игры вышли или нажали Escape, то мягко выйти из игры"""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    def run(self):
        """
        основной цикл игры
        тут вызываем основное метод рисования
        """
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
