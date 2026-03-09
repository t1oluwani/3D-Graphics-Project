from OpenGL.GL import *
from render.utils import load_obj

tank_vertices, _, tank_lines = load_obj("models/tank_wireframe.obj")

def draw_tank(enemy_tank):
    
    glPushMatrix()

    glTranslatef(enemy_tank.x, enemy_tank.y - 0.25, enemy_tank.z)
    glRotatef(enemy_tank.angle, 0, 1, 0)
    glScalef(1.25, 1.25, 1.25)
    glColor3f(0, 1, 0)

    glBegin(GL_LINES)

    for line in tank_lines:
        for i in range(len(line) - 1):
            v1 = tank_vertices[line[i]]
            v2 = tank_vertices[line[i + 1]]

            glVertex3fv(v1)
            glVertex3fv(v2)

    glEnd()

    glPopMatrix()