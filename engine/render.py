import math
from OpenGL.GL import *
from OpenGL.GLU import *

MOUNTAIN_POINTS = 4 * [20, 50, 30, 80, 40, 20, 60, 90, 40, 30, 70, 40]

# HELPER FUNCTIONS


def begin_2d(width, height):
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


def end_2d():
    # Restore depth
    glEnable(GL_DEPTH_TEST)

    # Restore 3D mode
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


# RENDERING FUNCTIONS


def draw_scope(width, height):
    # Switch to 2D mode
    begin_2d(width, height)

    cx = width // 2
    cy = height // 2
    bracket_width = 125
    bracket_height = 25
    vertical_gap = 60
    vertical_line = 100

    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)

    glBegin(GL_LINES)

    # --- Top Bracket ---
    # Vertical line
    glVertex2f(cx, cy + vertical_gap)
    glVertex2f(cx, cy + vertical_gap + vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    # Left vertical arm
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap + bracket_height)
    # Right vertical arm
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap + bracket_height)

    # --- Bottom Bracket ---
    # Vertical line
    glVertex2f(cx, cy - vertical_gap)
    glVertex2f(cx, cy - vertical_gap - vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    # Left vertical arm
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap - bracket_height)
    # Right vertical arm
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap - bracket_height)

    glEnd()

    # Switch back to 3D mode
    end_2d()


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


def draw_world(world):
    draw_floor(world.size)
    draw_mountains(world.ref_angle)

    for obj in world.objects:
        x, z = obj["pos"]
        if obj["type"] == "pyramid":
            draw_pyramid(x, z)
        else:
            draw_block(x, z)


def draw_bullet(x, y, z):
    print(f"Drawing bullet at position ({x}, {y}, {z})")
    # todo
