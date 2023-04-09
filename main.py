import pygame as pg
import sys
from settings import *


class Game:
    def __init__(self):
        pg.init()  #инициализация игровых модулей
        self.screen = pg.display.set_mode(RES) #экран для рендеринга
        self.clock = pg.time.Clock()  # создаем экземпляр класса часов

    def new_game (self):
        pass

    def update(self):
        pg.display.flip() #отображаем экран
        self.clock.tick(FPS) #отображаем фпс
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black') #на каждой итерации окрашиваем экран в черный цвет

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
