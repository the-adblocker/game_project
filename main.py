from random import *
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

from player import Player

fps = 24

page_w = 768
page_h = 576
clock = pg.time.Clock()


pg.init()


window = pg.display.set_mode((page_w, page_h))
pg.display.set_caption("super awesome game project")



points = 0
speed = 0.5


player = Player(0, 0, window, speed, speed, page_w, page_h)





font = pg.font.Font('freesansbold.ttf', 32)







running = True
while running:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill((150, 130, 150))

    player.drawn()

    if player._x+64 >= player._w or player._x < 0:
        points += 2
    if player._y+64 >= player._h or player._y <0:
        points += 2


    #score
    text = font.render(str(points), True, (0, 0, 0), (255, 255, 255))
    window.blit(text, (5, 5))
        
    #clickability
    if event.type == pg.MOUSEBUTTONUP:
        pos = pg.mouse.get_pos()
        if pos[0] >= player._x and pos[0] <= player._x+64 and pos[1] >= player._y and pos[1] <= player._y+64:
            player._x += player._speedx*3
            player._y += player._speedy*3
            points += 0.1
            points = round(points, 2)
    if points >= 20:
        points -= 20
        player._speedx *= 1.1
        player._speedy *= 1.1
   
    pg.display.update()
    clock.tick(fps)
pg.quit()