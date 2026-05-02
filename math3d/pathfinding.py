import math

from math3d.collision import check_collision
from math3d.raycasting import raycast

def pathfind_step(enemy, target, obstacles, enemies, speed=None):
    if speed is None:
        speed = enemy.speed

    tolerance=1.5

    dx = target.x - enemy.x
    dz = target.z - enemy.z
    target_dist = math.sqrt(dx**2 + dz**2) or 0.001

    avoid_x, avoid_z = 0.0, 0.0

    for obj in obstacles:
        ox = enemy.x - obj["pos"][0]
        oz = enemy.z - obj["pos"][1]
        dist = math.sqrt(ox**2 + oz**2) or 0.001
        if dist < tolerance:
            strength = (tolerance - dist) / tolerance
            avoid_x += (ox / dist) * strength
            avoid_z += (oz / dist) * strength
            # Push enemy out of the object immediately
            overlap = tolerance - dist
            enemy.x += (ox / dist) * overlap
            enemy.z += (oz / dist) * overlap

    for other in enemies:
        if other != enemy:
            ox = enemy.x - other.x
            oz = enemy.z - other.z
            dist = math.sqrt(ox**2 + oz**2) or 0.001
            if dist < tolerance:
                strength = (tolerance - dist) / tolerance
                avoid_x += (ox / dist) * strength
                avoid_z += (oz / dist) * strength
                overlap = tolerance - dist
                enemy.x += (ox / dist) * overlap
                enemy.z += (oz / dist) * overlap

    if avoid_x != 0.0 or avoid_z != 0.0:
        target_weight = 0.4
        blend_x = (dx / target_dist) * target_weight + avoid_x
        blend_z = (dz / target_dist) * target_weight + avoid_z
        enemy.rotate_towards(blend_x, blend_z)
    else:
        enemy.rotate_towards(dx, dz)

    enemy.move_forward(speed)