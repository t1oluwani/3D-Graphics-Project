from OpenGL.GL import *
from OpenGL.GLUT import (
    GLUT_BITMAP_HELVETICA_18,
    GLUT_BITMAP_HELVETICA_12,
    GLUT_BITMAP_9_BY_15,
    glutBitmapCharacter
)

from render.utils import begin_draw_2d, end_draw_2d

def draw_hud(game, dw, dh):
    curr_enemies = len(game.world.enemies)
    init_enemies = game.world.init_enemy_count
    
    begin_draw_2d(dw, dh)
    draw_level(game.world, dw)
    draw_difficulty(game.difficulty, dw)
    draw_score(game.score)
    draw_health(game.health)
    draw_enemy_count(curr_enemies, init_enemies)
    draw_minimap()
    end_draw_2d()
        
def draw_difficulty(difficulty, dw): 
    glColor3f(0.5, 0.7, 1.0)
    glRasterPos2f(dw-150, 25)
    for char in f'Difficulty: {difficulty.capitalize()}':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_level(world, dw):
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(dw-150, 50)
    for char in f'Level: {world.level} (up to {world.max_level})':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_score(score):
    glColor3f(0.0, 1.0, 0.0)
    glRasterPos2f(10, 25)
    for char in f'Score: {score}':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_health(health):
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2f(10, 50)
    for char in f'Health: {health}':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_enemy_count(curr, init):
    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2f(10, 75)
    for char in f'Enemies: {curr}/{init}':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        
def draw_minimap():
    #TODO: Implement minimap rendering
    pass