import pygame as pg
from storeitem import Storeitem

icon = pg.image.load("assets/temp_speed.png")

class Speedup(Storeitem):
    def __init__(self, type, price, size, window, x, y, boost):
        super().__init__(type, price, size, window, x, y)
        self._boost = boost
    
    def loop(self):
        self._window.blit(icon, pg.rect.Rect(self._x,self._y, 30, 30))
        #pg.draw.rect(self._window, (140, 100, 135), (self._x,self._y, self._size, self._size))
