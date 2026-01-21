import pygame as pg
from storeitem import Storeitem

icon = pg.image.load("assets/temp_boost.png")

class Pointboost(Storeitem):
    def __init__(self, type, price, size, window, x, y, boost):
        super().__init__(type, price, size, window, x, y)
        self._boost = boost

    def loop(self):
        self._window.blit(icon, pg.rect.Rect(self._x,self._y, 30, 30))