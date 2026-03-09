from OpenGL.GL import *
from render.utils import begin_draw_2d, end_draw_2d

bracket_width = 120
bracket_height = 30
vertical_gap = 60
vertical_line = 120
slant = 30

def draw_scope(width, height):
    cx = width // 2
    cy = height // 2

    begin_draw_2d(width, height)
    glColor3f(0.0, 0.9, 0.0)
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
    end_draw_2d()


def draw_scope_target(width, height):
    cx = width // 2
    cy = height // 2
    
    begin_draw_2d(width, height)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)

    # --- Top Bracket ---
    # Vertical line
    glVertex2f(cx, cy + vertical_gap - bracket_height)
    glVertex2f(cx, cy + vertical_gap + vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    # Left slanted arm
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx - bracket_width // 2 + slant, cy - vertical_gap + bracket_height)
    # Right slanted arm
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2 - slant, cy - vertical_gap + bracket_height)

    # --- Bottom Bracket ---
    # Vertical line
    glVertex2f(cx, cy - vertical_gap + bracket_height)
    glVertex2f(cx, cy - vertical_gap - vertical_line)
    # Horizontal bar
    glVertex2f(cx - bracket_width // 2, cy - vertical_gap)
    glVertex2f(cx + bracket_width // 2, cy - vertical_gap)
    # Left slanted arm
    glVertex2f(cx - bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx - bracket_width // 2 + slant, cy + vertical_gap - bracket_height)
    # Right slanted arm
    glVertex2f(cx + bracket_width // 2, cy + vertical_gap)
    glVertex2f(cx + bracket_width // 2 - slant, cy + vertical_gap - bracket_height)

    glEnd()
    end_draw_2d()