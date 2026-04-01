from OpenGL.GL import *

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
    s = 0.025

    glPushMatrix()
    glTranslatef(bullet.x, bullet.y, bullet.z)
    glRotatef(-bullet.angle, 0, 1, 0)
    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_LINES)

    # Bottom square
    glVertex3f(-s,-s,-s); glVertex3f(s,-s,-s)
    glVertex3f(s,-s,-s); glVertex3f(s,-s,s)
    glVertex3f(s,-s,s); glVertex3f(-s,-s,s)
    glVertex3f(-s,-s,s); glVertex3f(-s,-s,-s)

    # Top square
    glVertex3f(-s,s,-s); glVertex3f(s,s,-s)
    glVertex3f(s,s,-s); glVertex3f(s,s,s)
    glVertex3f(s,s,s); glVertex3f(-s,s,s)
    glVertex3f(-s,s,s); glVertex3f(-s,s,-s)

    # Vertical edges
    glVertex3f(-s,-s,-s); glVertex3f(-s,s,-s)
    glVertex3f(s,-s,-s); glVertex3f(s,s,-s)
    glVertex3f(s,-s,s); glVertex3f(s,s,s)
    glVertex3f(-s,-s,s); glVertex3f(-s,s,s)

    glEnd()
    glPopMatrix()
