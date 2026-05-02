from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
    
    # Enable blending 
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


def end_draw_2d():
    # Disable blending
    glDisable(GL_BLEND)
    
    # Restore depth
    glEnable(GL_DEPTH_TEST)

    # Restore 3D mode
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

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

def draw_text_centered(y, text, display_w, font=GLUT_BITMAP_HELVETICA_18):
    char_width = 7
    if font == GLUT_BITMAP_HELVETICA_18: char_width = 11
    if font == GLUT_BITMAP_HELVETICA_12: char_width = 7
    if font == GLUT_BITMAP_9_BY_15: char_width = 9
    text_width = len(text) * char_width
    x = (display_w - text_width) // 2
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(font, ord(char))
        
def draw_text_stroke_centered(y, text, size, display_w):
    char_width = 104.76 * size
    text_width = len(text) * char_width
    x = (display_w - text_width) // 2
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, -size, 1)
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(char))
    glPopMatrix()