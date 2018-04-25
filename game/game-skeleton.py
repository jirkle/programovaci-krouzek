# látka: funkce, cykly, podmínky, tok kódu

import pygame
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import *

screen = None
running = False
size = 640, 400

def on_init():
    global running, screen
    pygame.init()
    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    running = True
 
def on_event(event):
    global running
    if event.type == pygame.QUIT:
        running = False

def on_update():
    pass

def on_draw():
    global screen
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60)) # x, y, width, height
    pygame.display.flip()
        
def on_cleanup():
    pygame.quit()
 
def on_execute():
    global running
    if on_init() == False:
        running = False

    while( running ):
        for event in pygame.event.get():
            on_event(event)
        on_update()
        on_draw()
    on_cleanup()
 
if __name__ == "__main__" :
    on_execute()