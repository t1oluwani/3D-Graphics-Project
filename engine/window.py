# import math
# import ctypes
import pygame as pg
# import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
# import numpy as np
# import sys
CUBE_POINTS = (
    ( 1, -1, -1), # 0
    ( 1,  1, -1), # 1
    (-1,  1, -1), # 2
    (-1, -1, -1), # 3
    ( 1, -1,  1), # 4
    ( 1,  1,  1), # 5
    (-1, -1,  1), # 6
    (-1,  1,  1), # 7
    )

CUBE_EDGES = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
)

def drawcube():
    #Draw the cube using the open GL immidiate mode
    #todo: optionally put setup code here
    allpoints = list(zip(CUBE_POINTS))     #NOTE to TA's  -this is part of possibly over-complex code, see below

    # Draw the cube as a wireframe
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    
    #tGL_LINES expects pairs of 3D endpoints, call glVertex3fv() twice for each line segment
    #todo: pull out each pair of 3D endpoints and give the 3D point as a tuple (x,y,z) with the glVertex3fv() call
    #todo: make your code, with a loop, that calls glVertex3fv() twice for every line segment
    
    for edge in CUBE_EDGES:
        # Edge Start
        edge_start = edge[0]
        start_point = CUBE_POINTS[edge_start]
        glVertex3fv(start_point)
        
        # Edge End
        edge_end = edge[1]
        end_point = CUBE_POINTS[edge_end]
        glVertex3fv(end_point)
    
    glEnd()

def init_gl_state():     
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glFrontFace(GL_CW) #  clockwise polys face out
    
    # setup the camera
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, (640 / 480.0), 0.1, 50.0)  # setup lens
    glTranslatef(0.0, 0.0, -5.0)  # move back
    glRotatef(25, 1, 0, 0)  # orbit higher
    
def create_window(width=1024, height=768, title="Atari Battlezone Window"):
    pg.init() # init pygame and set up opengl display
    
    pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
    
    init_gl_state()
    
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if (event.type==pg.QUIT) or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
                running = False
            if (event.type==pg.KEYDOWN and (event.key==pg.K_UP or event.key==pg.K_w)):
                ...# move foward
            if (event.type==pg.KEYDOWN and (event.key==pg.K_DOWN or event.key==pg.K_s)):
                ...# move backward
            if (event.type==pg.KEYDOWN and (event.key==pg.K_LEFT or event.key==pg.K_a)):
                ...# rotate left
            if (event.type==pg.KEYDOWN and (event.key==pg.K_RIGHT or event.key==pg.K_d)):
                ...# rotate right
            
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # orbit camera around by 1 degree
        glRotatef(1, 0, 1, 0)
        drawcube()

        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
            





create_window()