import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import *

from render.models import draw_tank_2d
from render.utils import begin_draw_2d, end_draw_2d

def display_menu(display_w, display_h):
    menu_open = True
    
    while menu_open:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        begin_draw_2d(display_w, display_h)

        glColor3f(0.0, 1.0, 0.0)
        
        # Title
        glRasterPos2f(10, 25)
        for char in "Tio's Battlezone":
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
        # Tank Drawing
        draw_tank_2d(display_w, display_h)
        
        # Control Instructions
        glRasterPos2f(10, 50)
        for char in 'Controls: W/S to Move, A/D to Rotate, SPACE to Shoot':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
        glRasterPos2f(10, 70)
        for char in 'Shoot tanks to score points and advance levels. Avoid taking damage to survive!':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
        
        # Game options
        glRasterPos2f(10, 150)
        for char in '1. Start Game (Easy)':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 175)
        for char in '2. Start Game (Normal)':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 200)
        for char in '3. Start Game (Hard)':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 225)
        for char in 'Press 1, 2, or 3 to Start':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(10, 275)
        for char in 'Press ESC to Quit':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
            
        # Copyright
        glRasterPos2f(10, display_h - 80)
        for char in 'This is a 3D graphics project inspired by the original Battlezone game.':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
        glRasterPos2f(10, display_h - 60)
        for char in 'Original game copyright © 1983 Atari. All rights reserved.':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
        glRasterPos2f(10, display_h - 40)
        for char in 'Code and New Assets © 2024. All rights reserved.':
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

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
    