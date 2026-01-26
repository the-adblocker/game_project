from random import *
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

from player import Player
from storeitem import Storeitem
from speeup import Speedup
from pointboost import Pointboost
from more import More

fps = 24

page_w = 768
page_h = 576
clock = pg.time.Clock()
bg = pg.image.load("assets/temp_bg.png")

pg.init()


window = pg.display.set_mode((page_w, page_h))
pg.display.set_caption("super awesome game project")



points = 0
speed = 0.5
bounce = 2

font = pg.font.Font('freesansbold.ttf', 32)



player = Player(0, 0, window, speed, speed, page_w, page_h, 2)

#store items
speedshop = Speedup("speed", 5, 64, window, 50, page_h-114, 1.5)
pointboostshop = Pointboost("boost", 10, 64, window, 164, page_h-114, 1.5)
moreshop = More("more", 50, 64, window, 164+50+64, page_h-114)








logos = [player]

store = [speedshop, pointboostshop, moreshop]



running = True
while running:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill((150, 130, 150))


    window.blit(bg, pg.rect.Rect(0, 0, 30, 30))
    







    #score
    text = font.render(str(points), True, (0, 0, 0), (255, 255, 255))
    window.blit(text, (5, 5))
        
    #clickability
    for i in logos:
        i.drawn()
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if pos[0] >= i._x and pos[0] <= i._x+64 and pos[1] >= i._y and pos[1] <= i._y+64:
                i._x += i._speedx*1.5
                i._y += i._speedy*1.5
                points += bounce/40
                points = round(points, 2)
        if i._x+64 >= i._w or i._x < 0:
            points += bounce
            i._spr = randint(1,10)
        if i._y+64 >= i._h or i._y <0:
            points += bounce
            i._spr = randint(1,10)
        # if points >= 20:
        #     points -= 20
        #     player._speedx *= 1.1
        #     player._speedy *= 1.1

    #store
    for i in store:
        i.loop()
        #shop prices
        shoptxt = font.render(str(i._price), True, (0, 0, 0), (255, 255, 255))
        window.blit(shoptxt, (i._x, i._y-35))
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if pos[0] >= i._x and pos[0] <= i._x+64 and pos[1] >= i._y and pos[1] <= i._y+64:
                if points >= i._price:
                    points -= i._price
                    i._price += i._price
                    if i._type == "speed":
                        speed *= 1.1
                        for j in logos:
                            j._speedx *= 1.5
                            j._speedy *= 1.5

                    elif i._type == "boost":
                        bounce += 2
                    elif i._type == "more":
                        logos.append(Player(1, 1, window, speed*(1+(0.1*randint(-9, 9))), speed*(1+(0.1*randint(-9, 9))), page_w, page_h, 2))



   
    pg.display.update()
    clock.tick(fps)
pg.quit()