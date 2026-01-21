import pygame as pg



class Storeitem:
    def __init__(self, type, price, size, window, x, y):
        self._type = type
        self._price = price
        self._size = size
        self._window = window
        self._x = x
        self._y = y


    def loop(self):
        pg.draw.rect(self._window, (140, 100, 135), (self._x,self._y, self._size, self._size))
