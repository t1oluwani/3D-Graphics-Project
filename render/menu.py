import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import *

def display_menu():
    waiting = True
    while waiting:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

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

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    waiting = False  # start game
                if event.key == pg.K_2:
                    pg.quit()
                    exit()
    