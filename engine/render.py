import math
from OpenGL.GL import *
from OpenGL.GLU import *

MOUNTAIN_POINTS = [20, 50, 30, 80, 40, 20, 60, 90, 40, 30, 70, 40]

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
    
    
def draw_horizon(player_angle):
    pass
    # print(f"Drawing horizon with player angle {player_angle}")
    # glPushMatrix()
    
    # # Rotate the mountains based on player looking around
    # glRotatef(-player_angle, 0, 1, 0)
    
    # glColor3f(0.0, 0.8, 0.0) # Slightly darker green for distance
    # glLineWidth(1.5)
    
    # glBegin(GL_LINE_LOOP)
    # num_points = len(MOUNTAIN_POINTS)
    # radius = 500
    
    # for i in range(num_points):
    #     angle_deg = i * (360 / num_points)
    #     angle_rad = math.radians(angle_deg)
        
    #     x = radius * math.cos(angle_rad)
    #     z = radius * math.sin(angle_rad)
    #     y = MOUNTAIN_POINTS[i]
        
    #     glVertex3f(x, y, z)
        
    # glEnd()
    # glPopMatrix()
    
def draw_floor(size):
    glColor3f(0.0, 0.1, 0.0)
    glLineWidth(1.0)
    glBegin(GL_QUADS)
    
    glVertex3f(-size, -1, -size)
    glVertex3f(size, -1, -size)
    glVertex3f(size, -1, size)
    glVertex3f(-size, -1, size)
    glEnd()

def draw_world(world):
    draw_horizon(world.ref_angle)
    draw_floor(world.size)

    # for obj in world.objects:
    #     x, z = obj['pos']
    #     if obj['type'] == 'pyramid':
    #         # draw_pyramid(x, z)
    #         pass
    #     else:
    #         # draw_block(x, z)
    #         pass

    
def draw_bullet(x, y, z):
    print(f"Drawing bullet at position ({x}, {y}, {z})")
    #todo

