from OpenGL.GL import *
from render.utils import begin_draw_2d, end_draw_2d

bracket_width = 120
bracket_height = 30
vertical_gap = 60
vertical_line = 120
slant = 30

import math

def project_to_screen(x, y, z, player, dw, dh):
    fx, fy = 800, 800

    dx = x - player.x
    dy = y - player.y
    dz = z - player.z

    yaw = math.radians(player.angle)
    sin_yaw = math.sin(yaw)
    cos_yaw = math.cos(yaw)

    cam_x = dx * cos_yaw + dz * sin_yaw
    cam_z = -dx * sin_yaw + dz * cos_yaw
    cam_y = dy

    if cam_z <= 0:
        return None

    cx = dw / 2
    cy = dh / 2

    screen_x = fx * (cam_x / cam_z) + cx
    screen_y = fy * (cam_y / cam_z) + cy

    return int(screen_x), int(screen_y)

def is_scope_on_enemy(player, enemy, display_h, display_w):
    tolerance = 100
    enemy_x, enemy_y, enemy_z = enemy["pos"]
    result = project_to_screen(enemy_x, enemy_y, enemy_z, player, display_w, display_h)
    
    if result is None:
        return False  # enemy behind camera

    enemy_screen_x, enemy_screen_y = result
    crosshair_x = display_w // 2
    crosshair_y = display_h // 2
    x_match = abs(enemy_screen_x - crosshair_x) < tolerance
    y_match = abs(enemy_screen_y - crosshair_y) < tolerance

    return x_match and y_match

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
