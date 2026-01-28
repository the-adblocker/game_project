import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

dvd_logo = pg.image.load("assets/temp_dvd.png")
dvd_logo2 = pg.image.load("assets/temp_dvd2.png")
dvd_logo3 = pg.image.load("assets/temp_dvd3.png")
dvd_logo4 = pg.image.load("assets/temp_dvd4.png")
dvd_logo5 = pg.image.load("assets/temp_dvd5.png")
dvd_logo6 = pg.image.load("assets/temp_dvd6.png")
dvd_logo7 = pg.image.load("assets/temp_dvd7.png")
everyman = pg.image.load("assets/everyman.png")


class Player:
    def __init__(self, x, y, window, speedx, speedy, width, heigth, randspr):
        self._x = x
        self._y = y
        self._window = window
        self._speedx = speedx
        self._speedy = speedy
        self._w = width
        self._h = heigth
        self._spr = randspr

    def drawn(self):
        if self._spr == 1:
            self._window.blit(everyman, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 5:
            self._window.blit(dvd_logo2, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 9:
            self._window.blit(dvd_logo3, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 13:
            self._window.blit(dvd_logo4, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 17:
            self._window.blit(dvd_logo5, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 21:
            self._window.blit(dvd_logo6, pg.rect.Rect(self._x,self._y, 30, 30))
        elif self._spr <= 25:
            self._window.blit(dvd_logo7, pg.rect.Rect(self._x,self._y, 30, 30))
        else:
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