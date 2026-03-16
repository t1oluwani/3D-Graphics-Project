import pygame as pg

from OpenGL.GL import *
from OpenGL.GLU import *

from game.world import World
from game.enemy import Enemy
from game.player import Player

from render.models import draw_tank
from render.terrain import draw_world
from render.objects import draw_bullet
from render.screen import draw_scope, draw_scope_target


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
    display_w, display_h = pg.display.get_surface().get_size()


    player = Player()
    world = World(player)
    enemy = Enemy(0, 0, -5, 0)
    running = True
    bullets = []

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
                bullets.append(player.shoot())
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(-player.angle, 0, -1, 0)
        glTranslatef(-player.x, -player.y, -player.z)
        
        # Update and draw bullets
        for bullet in bullets:
            bullet.update(0.2)
            draw_bullet(bullet)

        # Draw the world (init pyramids, blocks, mountains, tanks, etc)
        draw_world(world)
        
        # Draw the scope in 2D
        draw_scope(display_w, display_h)
        
        # for enemy in world.enemies:
        #     if is_scope_on_enemy(scope_x, scope_y, enemy):
        #         draw_scope_target(display_w, display_h)
        #     else:
        #         draw_scope(display_w, display_h)
        
        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
