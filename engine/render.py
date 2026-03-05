import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

# HELPER FUNCTIONS
def begin_2d(width, height):
    # Switch to projection matrix
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    glOrtho(0, width, height, 0, -1, 1)
    glLineWidth(4.0)

    # Switch to modelview
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Disable depth
    glDisable(GL_DEPTH_TEST)
    
def end_2d():
    # Restore depth
    glEnable(GL_DEPTH_TEST)

    # Restore 3D mode
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    
    
def draw_scope(width, height):
    # Switch to 2D mode
    begin_2d(width, height)

    cx = width // 2
    cy = height // 2
    size = 50

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)

    # Horizontal
    glVertex2f(cx - size, cy)
    glVertex2f(cx + size, cy)

    # Vertical
    glVertex2f(cx, cy - size)
    glVertex2f(cx, cy + size)

    glEnd()

    # Switch back to 3D mode
    end_2d()
    

def draw_turret(x, y, z):
    #todo
    pass
    
def draw_player(x, y, z, angle):
    print(f"Drawing player at position ({x}, {y}, {z}) with angle {angle}")
    #todo
    
def draw_bullet(x, y, z):
    print(f"Drawing bullet at position ({x}, {y}, {z})")
    #todo

