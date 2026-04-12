import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import *

from render.models import draw_tank_rotating
from render.utils import (
    begin_draw_2d,
    end_draw_2d,
    draw_text_centered,
    draw_text_stroke_centered,
)

def display_menu(display_w, display_h):
    menu_open = True
    selected = None

    while menu_open:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        begin_draw_2d(display_w, display_h)

        glColor3f(0.0, 1.0, 0.0)

        # Pre-Title
        draw_text_centered(
            30, "T1OLUWANI . . . PRESENTS", display_w, GLUT_BITMAP_HELVETICA_18
        )

        # Title
        glLineWidth(12.5)
        draw_text_stroke_centered(150, "BATTLEZONE", 0.50, display_w)

        # Rotating tank (a little above center of screen)
        draw_tank_rotating(display_w, display_h)
        
        glColor3f(0.0, 1.0, 0.0)
        glLineWidth(3.0)

        # Controls
        draw_text_centered(
            display_h * 0.66,
            "W/S: MOVE    A/D: ROTATE    SPACE: SHOOT    ESC: QUIT",
            display_w,
            GLUT_BITMAP_9_BY_15,
        )
        
        glLineWidth(1.5)
        
        # Difficulty options (bottom half)
        draw_text_centered(
            display_h * 0.74, "SELECT DIFFICULTY", display_w, GLUT_BITMAP_HELVETICA_12
        )

        draw_text_centered(
            display_h * 0.78,
            "1.  EASY (3 Levels | 100 HP)",
            display_w,
            GLUT_BITMAP_HELVETICA_12,
        )
        draw_text_centered(
            display_h * 0.82,
            "2.  NORMAL (5 Levels | 150 HP)",
            display_w,
            GLUT_BITMAP_HELVETICA_12,
        )
        draw_text_centered(
            display_h * 0.86,
            "3.  HARD (7 Levels | 200 HP)",
            display_w,
            GLUT_BITMAP_HELVETICA_12,
        )

        glLineWidth(1.0)
        glColor3f(0.0, 0.8, 0.0)
        
        # Divider line
        glBegin(GL_LINES)
        glVertex2f(display_w * 0.2, display_h * 0.90)
        glVertex2f(display_w * 0.8, display_h * 0.90)
        glEnd()

        # Copyright
        draw_text_centered(
            display_h * 0.93,
            "INSPIRED BY ATARI BATTLEZONE (1983)  |  © 2024 ALL RIGHTS RESERVED",
            display_w,
            GLUT_BITMAP_HELVETICA_12,
        )
        draw_text_centered(
            display_h * 0.96,
            "DEVELOPED BY TIOLUWANI AKINLOYE",
            display_w,
            GLUT_BITMAP_HELVETICA_12,
        )

        end_draw_2d()
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    selected = "easy"
                    menu_open = False
                if event.key == pg.K_2:
                    selected = "normal"
                    menu_open = False
                if event.key == pg.K_3:
                    selected = "hard"
                    menu_open = False
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

    return selected  # pass difficulty back to game
