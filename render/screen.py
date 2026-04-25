import time
from OpenGL.GL import *

from render.utils import begin_draw_2d, end_draw_2d

bracket_width = 120
bracket_height = 30
vertical_gap = 60
vertical_line = 120
slant = 30


def draw_scope_regular(width, height):
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

def draw_damage_indicator(game, width, height):
    if game.damage_flash_start is not None:
        elapsed = time.time() - game.damage_flash_start
        duration = 0.6

        if elapsed < duration:
            alpha = (1.0 - elapsed / duration) * 0.7
            draw_red_borders(width, height, thickness=35, alpha=alpha)
        else:
            game.damage_flash_start = None


def draw_red_borders(width, height, thickness=50, alpha=0.25):
    begin_draw_2d(width, height)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glColor4f(1.0, 0.0, 0.0, alpha)

    glBegin(GL_QUADS)

    # Top bar
    glVertex2f(0, 0)
    glVertex2f(width, 0)
    glVertex2f(width, thickness)
    glVertex2f(0, thickness)

    # Bottom bar
    glVertex2f(0, height - thickness)
    glVertex2f(width, height - thickness)
    glVertex2f(width, height)
    glVertex2f(0, height)

    # Left bar
    glVertex2f(0, thickness)
    glVertex2f(thickness, thickness)
    glVertex2f(thickness, height - thickness)
    glVertex2f(0, height - thickness)

    # Right bar
    glVertex2f(width - thickness, thickness)
    glVertex2f(width, thickness)
    glVertex2f(width, height - thickness)
    glVertex2f(width - thickness, height - thickness)

    glEnd()

    glDisable(GL_BLEND)
    end_draw_2d()