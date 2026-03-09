from OpenGL.GL import *

MOUNTAIN_POINTS = 4 * [20, 50, 30, 80, 40, 20, 60, 90, 40, 30, 70, 40]


def begin_draw_2d(width, height):
    # Switch to projection matrix
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    glOrtho(0, width, height, 0, -1, 1)
    glLineWidth(2.0)

    # Switch to modelview
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Disable depth
    glDisable(GL_DEPTH_TEST)


def end_draw_2d():
    # Restore depth
    glEnable(GL_DEPTH_TEST)

    # Restore 3D mode
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)