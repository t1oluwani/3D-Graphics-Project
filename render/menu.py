import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import *

from render.utils import begin_draw_2d, end_draw_2d

def display_menu(display_w, display_h):
    menu_open = True
    
    while menu_open:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        begin_draw_2d(display_w, display_h)

        glColor3f(0.0, 1.0, 0.0)
        glRasterPos2f(10, 25)
        for char in 'Mock Atari Battlezone':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 50)
        for char in '1. Start Game':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 75)
        for char in '2. Exit':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        end_draw_2d()
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    menu_open = False
                if event.key == pg.K_2:
                    pg.quit()
                    exit()
    