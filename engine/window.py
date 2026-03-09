import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

from game.player import Player
from game.world import World
from engine.render import draw_scope_regular, draw_scope_target, draw_world


def init_gl_state(width, height):
    # setup camera
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)

    # setup lens
    glLoadIdentity()
    gluPerspective(45.0, (width / height), 0.1, 50.0)


def create_window(width=1024, height=768, title="Atari Battlezone Window"):
    pg.init()  # init pygame
    pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
    init_gl_state(width, height)  # setup opengl state

    player = Player()
    world = World(player)
    running = True

    while running:
        events = pg.event.get()
        for event in events:
            if (event.type == pg.QUIT) or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False

            keys = pg.key.get_pressed()  # ensures holding down keys works

            if keys[pg.K_w]:
                player.move_forward(0.1)
            if keys[pg.K_s]:
                player.move_backward(0.1)
            if keys[pg.K_a]:
                player.rotate_left(5)
            if keys[pg.K_d]:
                player.rotate_right(5)
            if keys[pg.K_SPACE]:
                player.shoot()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(-player.angle, 0, -1, 0)
        glTranslatef(-player.x, -player.y, -player.z)

        # Draw the world
        draw_world(world)

        # Draw the scope in 2D
        width, height = pg.display.get_surface().get_size()
        draw_scope_regular(width, height)
        # draw_scope_target(width, height)

        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
