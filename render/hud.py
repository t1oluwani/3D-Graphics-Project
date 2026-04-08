from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_hud(score, health):
    draw_score(score)
    draw_health(health)
    draw_minimap()
    
def draw_score(score):
    pass
    # glColor3f(1.0, 1.0, 1.0)
    # glRasterPos2f(-0.95, 0.9)
    # for char in f'Score: {score}':
    #     glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
        
def draw_health(health):
    pass
    # glColor3f(1.0, 0.0, 0.0)
    # glRasterPos2f(-0.95, 0.8)
    # for char in f'Health: {health}':
    #     glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_minimap():
    #TODO: Implement minimap rendering
    pass