import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_scope(width, height):
    # Switch to 2D mode
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, width, height, 0, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)

    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)

    cx = width // 2
    cy = height // 2
    size = 50

    glBegin(GL_LINES)

    # Horizontal
    glVertex2f(cx - size, cy)
    glVertex2f(cx + size, cy)

    # Vertical
    glVertex2f(cx, cy - size)
    glVertex2f(cx, cy + size)

    glEnd()

    glEnable(GL_DEPTH_TEST)

    # Restore 3D mode
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    

def draw_turret(x, y, z):
    #todo
    pass
    


