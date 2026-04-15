import math
import time

def simple_enemy(enemy, player, cooldown=5.0):
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    distance = math.sqrt(dx**2 + dz**2)

    if distance > 10.0:
        enemy.move_forward(enemy.speed)
    
    # Rotate towards the player
    target_angle = math.degrees(math.atan2(dx, dz))
    angle_diff = (target_angle - enemy.angle + 360) % 360
    if angle_diff > 180:
        enemy.rotate_left(min(5, 360 - angle_diff))
    else:
        enemy.rotate_right(min(5, angle_diff))

    # Shoot if within range (with a cooldown)
    if distance < 15.0:
        now = time.time()
        if not hasattr(enemy, "last_shot") or now - enemy.last_shot > cooldown:
            enemy.last_shot = now
            return enemy.shoot()

def hunter(enemy, player):
    pass

def sniper(enemy, player):
    pass

def guard(enemy, player):
    pass

