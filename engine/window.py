import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

from game.player import Player

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
    # Draw the cube as a wireframe
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    
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

def init_gl_state(width, height):    
    # setup camera
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    # setup lens
    glLoadIdentity()
    gluPerspective(45.0, (width / height), 0.1, 50.0)  
    
def create_window(width=1024, height=768, title="Atari Battlezone Window"):
    pg.init() # init pygame 
    window = pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
    init_gl_state(width, height) # setup opengl state
    
    player = Player()   
    running = True
    
    while running:
        events = pg.event.get()
        for event in events:
            if (event.type==pg.QUIT) or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
                running = False
                
            if (event.type==pg.KEYDOWN and (event.key==pg.K_UP or event.key==pg.K_w)):
                player.move_forward(1)
            if (event.type==pg.KEYDOWN and (event.key==pg.K_DOWN or event.key==pg.K_s)):
                player.move_backward(1)
            if (event.type==pg.KEYDOWN and (event.key==pg.K_LEFT or event.key==pg.K_a)):
                player.rotate_left(0.5)
            if (event.type==pg.KEYDOWN and (event.key==pg.K_RIGHT or event.key==pg.K_d)):
                player.rotate_right(0.5)
                            
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(player.angle, 0, 1, 0)
        glTranslatef(player.x, player.y, player.z)
        
        drawcube()

        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
            
