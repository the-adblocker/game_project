import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

dvd_logo = pg.image.load("assets/temp_dvd.png")


class Player:
    def __init__(self, x, y, window, speedx, speedy, width, heigth):
        self._x = x
        self._y = y
        self._window = window
        self._speedx = speedx
        self._speedy = speedy
        self._w = width
        self._h = heigth
        

    def drawn(self):
        self._window.blit(dvd_logo, pg.rect.Rect(self._x,self._y, 30, 30))
        #pg.draw.rect(self._window, (210, 20, 0), (self._x,self._y, 64, 64))
        self._x += self._speedx
        self._y += self._speedy

        #bounce
        if self._x+64 >= self._w or self._x < 0:
            self._speedx -= self._speedx * 2
        if self._y+64 >= self._h or self._y <0:
            self._speedy -= self._speedy *2



            
        # if pg.key.get_pressed()[K_UP]:
        #     self._y -= self._speed
        # if pg.key.get_pressed()[K_DOWN]:
        #     self._y += self._speed
        # if pg.key.get_pressed()[K_RIGHT]:
        #     self._x += self._speed
        # if pg.key.get_pressed()[K_LEFT]:
        #     self._x -= self._speed