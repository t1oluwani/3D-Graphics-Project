from OpenGL.GL import *

MOUNTAIN_POINTS = 4 * [20, 50, 30, 80, 40, 20, 60, 90, 40, 30, 70, 40]


def begin_draw_2d(width=500, height=500):
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


def load_obj(path):
    vertices = []
    faces = []
    lines = []

    with open(path, "r") as file:
        for line in file:
            if line.startswith("v "):
                parts = line.strip().split()
                vertex = tuple(map(float, parts[1:4]))
                vertices.append(vertex)

            elif line.startswith("f "):
                parts = line.strip().split()
                face = []
                for p in parts[1:]:
                    idx = int(p.split("/")[0]) - 1
                    face.append(idx)
                faces.append(face)

            elif line.startswith("l "):
                parts = line.strip().split()
                line_indices = [int(p) - 1 for p in parts[1:]]
                lines.append(line_indices)

    return vertices, faces, lines
