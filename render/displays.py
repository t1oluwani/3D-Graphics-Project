import pygame as pg
from OpenGL.GL import *
from OpenGL.GLUT import (
    GLUT_BITMAP_HELVETICA_18,
    GLUT_BITMAP_HELVETICA_12,
    GLUT_BITMAP_9_BY_15
)

from render.models import draw_tank_rotating
from render.utils import (
    begin_draw_2d,
    end_draw_2d,
    draw_text_centered,
    draw_text_stroke_centered,
)

FONT_LARGE = GLUT_BITMAP_HELVETICA_18
FONT_SMALL = GLUT_BITMAP_HELVETICA_12
FONT_UNIQUE = GLUT_BITMAP_9_BY_15


def display_menu(display_w, display_h):
    menu_open = True
    selected = None

    while menu_open:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        begin_draw_2d(display_w, display_h)

        glColor3f(0.0, 1.0, 0.0)

        # Pre-Title
        draw_text_centered(50, "T1OLUWANI . . . PRESENTS", display_w, FONT_LARGE)

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
            FONT_UNIQUE,
        )

        glLineWidth(1.5)

        # Difficulty options (bottom half) - extra space is for spacing
        draw_text_centered(display_h * 0.74, "SELECT DIFFICULTY   ", display_w, FONT_SMALL)

        draw_text_centered(
            display_h * 0.78,
            "1.  EASY (3 Levels | 100 HP)",
            display_w,
            FONT_SMALL,
        )
        draw_text_centered(
            display_h * 0.82,
            "2.  NORMAL (5 Levels | 150 HP)",
            display_w,
            FONT_SMALL,
        )
        draw_text_centered(
            display_h * 0.86,
            "3.  HARD (7 Levels | 200 HP)",
            display_w,
            FONT_SMALL,
        )

        glLineWidth(1.0)
        glColor3f(0.5, 0.7, 1.0)

        # Divider line
        glBegin(GL_LINES)
        glVertex2f(display_w * 0.2, display_h * 0.90)
        glVertex2f(display_w * 0.8, display_h * 0.90)
        glEnd()
        
        # Copyright
        draw_text_centered(
            display_h * 0.93,
            "INSPIRED BY ATARI BATTLEZONE (1983)  |  © 2026 ALL RIGHTS RESERVED",
            display_w,
            FONT_SMALL,
        )
        draw_text_centered(
            display_h * 0.96,
            "DEVELOPED BY TIOLUWANI AKINLOYE",
            display_w,
            FONT_SMALL,
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


def display_game_over(display_w, display_h, win=False):
    game_over_screen = True
    y_val = display_h * 0.40
    size = 0.75
    size_mini = 0.50

    while game_over_screen:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        begin_draw_2d(display_w, display_h)

        glLineWidth(15)

        if win:
            glColor3f(0.0, 1.0, 0.0)
            draw_text_stroke_centered(y_val, "CONGRATS!", size, display_w)
            glLineWidth(5)
            glColor3f(1.0, 1.0, 1.0)
            draw_text_stroke_centered(y_val + 125, "YOU WIN!", size_mini, display_w)
        else:
            glColor3f(1.0, 0.0, 0.0)
            draw_text_stroke_centered(y_val, "GAME OVER!", size, display_w)
            glLineWidth(5)
            glColor3f(1.0, 1.0, 1.0)
            draw_text_stroke_centered(y_val + 125, "YOU LOSE!", size_mini, display_w)

        draw_text_centered(
            display_h * 0.85,
            "PRESS 'ESC' TO QUIT",
            display_w,
            FONT_LARGE,
        )

        end_draw_2d()
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
