

from math3d.collision import check_collision

def pathfind_step(enemy, target, obstacles, enemies, speed=None):
    if speed is None:
        speed = enemy.speed

    dx = target.x - enemy.x
    dz = target.z - enemy.z
    enemy.rotate_towards(dx, dz)

    blocked = False

    for obj in obstacles:
        if check_collision(enemy, obj, 1.5):
            blocked = True
            avoid_dx = enemy.x - obj["pos"][0]
            avoid_dz = enemy.z - obj["pos"][1]
            enemy.rotate_towards(avoid_dx, avoid_dz)
            break

    if not blocked:
        for other in enemies:
            if other != enemy and check_collision(enemy, other, 1.5):
                blocked = True
                # Steer away from other enemy
                avoid_dx = enemy.x - other.x
                avoid_dz = enemy.z - other.z
                enemy.rotate_towards(avoid_dx, avoid_dz)
                break

    enemy.move_forward(speed)