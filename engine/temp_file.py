from OpenGL.GL import *
from OpenGL.GLU import *

REF_CUBE_POINTS = (
    ( 1, -1, -1), # 0
    ( 1,  1, -1), # 1
    (-1,  1, -1), # 2
    (-1, -1, -1), # 3
    ( 1, -1,  1), # 4
    ( 1,  1,  1), # 5
    (-1, -1,  1), # 6
    (-1,  1,  1), # 7
    )

REF_CUBE_EDGES = (
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

def draw_reference_cube():
    # Draw the cube as a wireframe
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    
    for edge in REF_CUBE_EDGES:
        # Edge Start
        edge_start = edge[0]
        start_point = REF_CUBE_POINTS[edge_start]
        glVertex3fv(start_point)
        
        # Edge End
        edge_end = edge[1]
        end_point = REF_CUBE_POINTS[edge_end]
        glVertex3fv(end_point)
    
    glEnd()
    
