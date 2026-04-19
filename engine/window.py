import pygame as pg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math3d.raycasting import raycast

from render.hud import draw_hud
from render.displays import display_menu
from render.terrain import draw_world
from render.objects import draw_bullet
from render.screen import draw_scope_regular, draw_scope_target, draw_damage_indicator

from math3d.collision import (
    bullet_hit,
    player_enemy_collision,
    player_object_collision,
)

def init_gl_state(width, height):
    # setup camera
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)

    # setup lens
    glLoadIdentity()
    gluPerspective(40.0, (width / height), 0.1, 500.0)

def append_bullet(bullet, bullets):
    if bullet is not None:
        bullets.append(bullet)


# Main game loop and window operations
def create_window(width, height, title, game):
    pg.init()  # init pygame
    glutInit()  # init glut
    pg.display.set_caption(title)
    pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)

    display_w, display_h = (
        pg.display.get_surface().get_size()
    )  # get actual display size (handles resizing)

    difficulty = display_menu(
        display_w, display_h
    )  # show menu and get difficulty choice
    game.set_difficulty(difficulty)

    init_gl_state(width, height)  # setup opengl state

    running = True
    bullets = []

    while running and not game.game_over():
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    append_bullet(game.player.shoot(), bullets)
                if event.key == pg.K_ESCAPE:
                    running = False

        old_px, old_pz = game.player.x, game.player.z

        keys = pg.key.get_pressed()  # ensures holding down keys works

        if keys[pg.K_w]:
            game.player.move_forward()
        if keys[pg.K_s]:
            game.player.move_backward()
        if keys[pg.K_a]:
            game.player.rotate_left()
        if keys[pg.K_d]:
            game.player.rotate_right()
        if keys[pg.K_q]:
            game.player.rotate_left(0.1)
        if keys[pg.K_e]:
            game.player.rotate_right(0.1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Apply player position and angle
        glRotatef(-game.player.angle, 0, -1, 0)
        glTranslatef(-game.player.x, 0, -game.player.z)
        
        draw_damage_indicator(game, display_w, display_h)

        # Update and draw bullets
        for bullet in bullets:
            bullet.update(0.5)
            draw_bullet(bullet)

        # Draw the world (init pyramids, blocks, mountains, tanks, etc)
        draw_world(game.world)

        # Draw the scope in 2D
        scope_on_enemy = any(
            raycast(game.player, enemy, game.world.objects)
            for enemy in game.world.enemies
        )

        if scope_on_enemy:
            draw_scope_target(display_w, display_h)
        else:
            draw_scope_regular(display_w, display_h)

        # Enemy updates and collisions
        for enemy in game.world.enemies:
            append_bullet(enemy.update(game.player), bullets)  # enemy moves and shoots

            if player_enemy_collision(game.player, enemy):
                game.player.x, game.player.z = old_px, old_pz
                break

        for obj in game.world.objects:
            if player_object_collision(game.player, obj):
                game.player.x, game.player.z = old_px, old_pz
                break

        # Bullet collisions
        bullets = [b for b in bullets if not bullet_hit(b, game)]

        # Level handling (TODO: congrats and next level screen)
        if not game.world.enemies:  # if all enemies defeated, move to next level
            game.next_level()

        draw_hud(game, display_w, display_h)
        pg.display.flip()
        pg.time.wait(10)
    pg.quit()


# Working TODO List:
# - Add red outline when player gets shot  
# - Increase dmg per level
# - Enable enemy collisions (objects, player, other enemies) + minor dmg on direct contact  
# - Implement pathfinding (avoid obstacles) -> Implement AI system (H, P, S, D)
# - Add map boundaries static vals → config vars 