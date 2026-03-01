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
                
            keys = pg.key.get_pressed()
                
            if keys[pg.K_UP] or keys[pg.K_w]:
                player.move_forward(0.1)
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                player.move_backward(0.1)
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                player.rotate_left(5)
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                player.rotate_right(5)
            if keys[pg.K_SPACE]:
                player.shoot()
                            
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(player.angle, 0, 1, 0)
        glTranslatef(player.x, player.y, player.z)
        
        # Draw the scope in 2D
        width, height = pg.display.get_surface().get_size()
        draw_scope(width, height)
        
        drawcube()
        
        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
            
