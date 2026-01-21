from random import *
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

from player import Player
from storeitem import Storeitem
from speeup import Speedup

fps = 24

page_w = 768
page_h = 576
clock = pg.time.Clock()


pg.init()


window = pg.display.set_mode((page_w, page_h))
pg.display.set_caption("super awesome game project")



points = 0
speed = 0.5


font = pg.font.Font('freesansbold.ttf', 32)



player = Player(0, 0, window, speed, speed, page_w, page_h)

#store items
speedshop = Speedup("speed", 5, 64, window, 50, page_h-114, 1.5)








logos = [player]

store = [speedshop]



running = True
while running:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill((150, 130, 150))


    #runs the classes
    player.drawn()




    if player._x+64 >= player._w or player._x < 0:
        points += 2
    if player._y+64 >= player._h or player._y <0:
        points += 2


    #score
    text = font.render(str(points), True, (0, 0, 0), (255, 255, 255))
    window.blit(text, (5, 5))
        
    #clickability
    for i in logos:
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if pos[0] >= i._x and pos[0] <= i._x+64 and pos[1] >= i._y and pos[1] <= i._y+64:
                i._x += i._speedx*1.5
                i._y += i._speedy*1.5
                points += 0.05
                points = round(points, 2)
        # if points >= 20:
        #     points -= 20
        #     player._speedx *= 1.1
        #     player._speedy *= 1.1

    #store
    for i in store:
        i.loop()
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if pos[0] >= i._x and pos[0] <= i._x+64 and pos[1] >= i._y and pos[1] <= i._y+64:
                if points >= i._price:
                    points -= i._price
                    i._price += i._price
                    if i._type == "speed":
                        for j in logos:
                            j._speedx *= 1.5
                            j._speedy *= 1.5


   
    pg.display.update()
    clock.tick(fps)
pg.quit()