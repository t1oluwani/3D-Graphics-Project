from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pyramid(x, z):
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1.5)
    glBegin(GL_LINE_LOOP)

    glVertex3f(x - 1, -1, z - 1)
    glVertex3f(x + 1, -1, z - 1)
    glVertex3f(x + 1, -1, z + 1)
    glVertex3f(x - 1, -1, z + 1)

    glEnd()

    glBegin(GL_LINES)
    for dx, dz in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        glVertex3f(x + dx, -1, z + dz)
        glVertex3f(x, 1.5, z)
    glEnd()


def draw_block(x, z):
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1.5)
    glBegin(GL_LINE_LOOP)

    glVertex3f(x - 1, -1, z - 1)
    glVertex3f(x + 1, -1, z - 1)
    glVertex3f(x + 1, -1, z + 1)
    glVertex3f(x - 1, -1, z + 1)

    glEnd()

    glBegin(GL_LINE_LOOP)

    glVertex3f(x - 1, 1, z - 1)
    glVertex3f(x + 1, 1, z - 1)
    glVertex3f(x + 1, 1, z + 1)
    glVertex3f(x - 1, 1, z + 1)

    glEnd()

    glBegin(GL_LINES)
    for dx, dz in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        glVertex3f(x + dx, -1, z + dz)
        glVertex3f(x + dx, 1, z + dz)
    glEnd()


def draw_bullet(bullet):
    radius = 0.125

    glPushMatrix()
    glTranslatef(bullet.x, 0, bullet.z)
    glColor3f(0.0, 1.0, 0.0)

    quad = gluNewQuadric()
    gluSphere(quad, radius, 16, 16)  # (quadric, radius, slices, stacks)
    gluDeleteQuadric(quad)

    glPopMatrix()
