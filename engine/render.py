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
    glLineWidth(2.0)

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
   
   
   
# RENDERING FUNCTIONS    
    
def draw_scope(width, height):
    # Switch to 2D mode
    begin_2d(width, height)

    cx = width // 2
    cy = height // 2
    bracket_width = 125   
    bracket_height = 25  
    vertical_gap = 60
    vertical_line = 100

    glColor3f(0.0, 1.0, 0.0) 
    glLineWidth(2.0)

    glBegin(GL_LINES)
    
    # --- Top Bracket ---
    # Vertical line
    glVertex2f(cx, cy + vertical_gap)
    glVertex2f(cx, cy + vertical_gap + vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    # Left vertical arm
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap + bracket_height)
    # Right vertical arm
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap + bracket_height)

    # --- Bottom Bracket ---
    # Vertical line
    glVertex2f(cx, cy - vertical_gap)
    glVertex2f(cx, cy - vertical_gap - vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    # Left vertical arm
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap - bracket_height)
    # Right vertical arm
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap - bracket_height)

    glEnd()

    # Switch back to 3D mode
    end_2d()

    

    
def draw_bullet(x, y, z):
    print(f"Drawing bullet at position ({x}, {y}, {z})")
    #todo

