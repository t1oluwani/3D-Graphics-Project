import pygame as pg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from objects import player
from objects import enemy
from objects.world import World
from objects.enemy import Enemy
from objects.player import Player

from math3d.raycasting import raycast_enemy
from render.hud import draw_hud
from render.terrain import draw_world
from render.objects import draw_bullet
from render.screen import draw_scope_regular, draw_scope_target

from math3d.collision import (
    bullet_hit,
    player_enemy_collision,
    player_object_collision,
    bullet_enemy_collision,
    bullet_object_collision,
)


def init_gl_state(width, height):
    # setup camera
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)

    # setup lens
    glLoadIdentity()
    gluPerspective(45.0, (width / height), 0.1, 50.0)


def create_window(width, height, title, game):
    pg.init()  # init pygame
    glutInit() # init glut 
    pg.display.set_caption(title)
    pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
    
    init_gl_state(width, height)  # setup opengl state
    display_w, display_h = pg.display.get_surface().get_size()

    running = True
    bullets = []

    while running and not game.game_over:
        events = pg.event.get()
        
        for event in events:
            if (event.type == pg.QUIT) or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False

            old_px, old_py, old_pz = game.player.x, game.player.y, game.player.z

            keys = pg.key.get_pressed()  # ensures holding down keys works

            if keys[pg.K_w]:
                game.player.move_forward()
            if keys[pg.K_s]:
                game.player.move_backward()
            if keys[pg.K_a]:
                game.player.rotate_left()
            if keys[pg.K_d]:
                game.player.rotate_right()
            if keys[pg.K_SPACE]:
                bullets.append(game.player.shoot())
            if keys[pg.K_ESCAPE]:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(-game.player.angle, 0, -1, 0)
        glTranslatef(-game.player.x, -game.player.y, -game.player.z)

        # Update and draw bullets
        for bullet in bullets:
            bullet.update(0.2)
            draw_bullet(bullet)

        # Draw the world (init pyramids, blocks, mountains, tanks, etc)
        draw_world(game.world)

        # Draw the scope in 2D
        scope_on_enemy = any(raycast_enemy(game.player, enemy) for enemy in game.world.enemies)

        if scope_on_enemy:
            draw_scope_target(display_w, display_h)
        else:
            draw_scope_regular(display_w, display_h)

        # Player collisions
        for enemy in game.world.enemies:
            if player_enemy_collision(game.player, enemy):
                game.player.x, game.player.y, game.player.z = old_px, old_py, old_pz
                break

            # Upon defeating an enemy
            if enemy.health <= 0:
                game.world.enemies.remove(enemy) 
                game.score += (100*(game.world.level))

        for obj in game.world.objects:
            if player_object_collision(game.player, obj):
                game.player.x, game.player.y, game.player.z = old_px, old_py, old_pz
                break

        # Bullet collisions
        bullets = [b for b in bullets if not bullet_hit(b, game.world)]
        
        # Level handling (TODO: congrats and next level screen)
        if not game.world.enemies:  # if all enemies defeated, move to next level
            game.world.update_level(game.player)

        draw_hud(game, display_w, display_h)
        pg.display.flip()
        pg.time.wait(10)
    pg.quit()
