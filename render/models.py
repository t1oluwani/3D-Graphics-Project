from OpenGL.GL import *
from render.utils import load_obj

tank_vertices, _, tank_lines = load_obj("models/tank_wireframe.obj")

tank_rotation = 0.0

def draw_tank_3d(enemy_tank):

    glPushMatrix()

    glTranslatef(enemy_tank.x, enemy_tank.y - 0.25, enemy_tank.z)
    glRotatef(enemy_tank.angle + 90, 0, 1, 0)
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


def draw_tank_2d(display_w, display_h):

    glPushMatrix()

    glTranslatef(display_w // 2, display_h // 2, 0)
    glRotatef(180, 0, 1, 0)
    glScalef(100, -100, 1)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)

    glBegin(GL_LINES)

    for line in tank_lines:
        for i in range(len(line) - 1):
            v1 = tank_vertices[line[i]]
            v2 = tank_vertices[line[i + 1]]

            glVertex2f(v1[0], v1[1])
            glVertex2f(v2[0], v2[1])

    glEnd()

    glPopMatrix()


def draw_tank_flattened_3d(display_w, display_h):
    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    glOrtho(
        -display_w // 2, display_w // 2, display_h // 2, -display_h // 2, -1000, 1000
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0, 0, 0)
    glRotatef(30, 1, 0, 0)  # tilt towards screen
    glRotatef(200, 0, 1, 0)  # horizontal turn
    glScalef(100, -100, 100)  # scale all 3 axes

    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)

    glBegin(GL_LINES)

    for line in tank_lines:
        for i in range(len(line) - 1):
            v1 = tank_vertices[line[i]]
            v2 = tank_vertices[line[i + 1]]

            glVertex3f(v1[0], v1[1], v1[2])
            glVertex3f(v2[0], v2[1], v2[2])

    glEnd()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def draw_tank_rotating(display_w, display_h):
    global tank_rotation
    tank_rotation += 0.5

    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    glOrtho(-display_w // 2, display_w // 2, display_h // 2, -display_h // 2, -1000, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0, 0, 0)
    glRotatef(30, 1, 0, 0)            # tilt towards screen (fixed)
    glRotatef(tank_rotation, 0, 1, 0) # horizontal spin (animated)
    glScalef(100, -100, 100)

    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)

    glBegin(GL_LINES)
    for line in tank_lines:
        for i in range(len(line) - 1):
            v1 = tank_vertices[line[i]]
            v2 = tank_vertices[line[i + 1]]
            glVertex3f(v1[0], v1[1], v1[2])
            glVertex3f(v2[0], v2[1], v2[2])
    glEnd()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()