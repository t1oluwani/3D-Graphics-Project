import math
from OpenGL.GL import *
from objects.enemy import Enemy

from render.models import draw_tank
from render.utils import MOUNTAIN_POINTS
from render.objects import draw_block, draw_pyramid

def draw_mountains(player_angle):
    glPushMatrix()

    glRotatef(-player_angle, 0, 1, 0)
    glColor3f(0.0, 0.8, 0.0)
    glLineWidth(2)

    radius = 40
    height_scale = 0.1
    num_points = len(MOUNTAIN_POINTS)

    glBegin(GL_LINE_LOOP)

    for i in range(num_points):
        angle = math.radians(i * (360 / num_points))
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        y = MOUNTAIN_POINTS[i] * height_scale

        glVertex3f(x, y, z)

    glEnd()
    glPopMatrix()


def draw_floor(size):
    glColor3f(0.0, 0.1, 0.0)
    glLineWidth(1.0)
    glBegin(GL_QUADS)

    glVertex3f(-size, -1, -size)
    glVertex3f(size, -1, -size)
    glVertex3f(size, -1, size)
    glVertex3f(-size, -1, size)
    glEnd()
    
    
def draw_world(world):
    draw_floor(world.size)
    draw_mountains(world.ref_angle)

    # Draw objects in the world
    for obj in world.objects:
        x, z, _ = obj["pos"]
        if obj["type"] == "pyramid":
            draw_pyramid(x, z)
        else:
            draw_block(x, z)
            
    # Draw enemies in the world
    for enemy in world.enemies:
        draw_tank(enemy)