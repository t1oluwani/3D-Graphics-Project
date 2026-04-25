import math
import time

GUARD_PATROL_RADIUS = 8.0
SNIPER_MIN_DISTANCE = 20.0
SNIPER_MAX_DISTANCE = 35.0
HUNTER_CHARGE_DISTANCE = 5.0

def shot_attempt(enemy, distance, max_range, cooldown):
    if distance < max_range:
        now = time.time()
        if not hasattr(enemy, "last_shot") or now - enemy.last_shot > cooldown:
            enemy.last_shot = now
            return enemy.shoot()

def simple_enemy(enemy, player, cooldown):
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    distance = math.sqrt(dx**2 + dz**2)

    if distance > 10.0:
        enemy.move_forward(enemy.speed)

    enemy.rotate_towards(enemy, player.x, player.z)

    return shot_attempt(enemy, distance, 15.0, cooldown)

def hunter(enemy, player, cooldown):
    """Aggressively chases the player and closes distance to point blank."""
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    distance = math.sqrt(dx**2 + dz**2)

    enemy.rotate_towards(enemy, player.x, player.z, speed=8) 

    # Always charges unless point blank
    if distance > HUNTER_CHARGE_DISTANCE:
        enemy.move_forward(enemy.speed * 1.5)

    return shot_attempt(enemy, distance, 10.0, cooldown * 0.6)  # shoots more frequently


def sniper(enemy, player, cooldown):
    """Keeps distance and shoots from afar. Retreats if player gets too close."""
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    distance = math.sqrt(dx**2 + dz**2)

    enemy.rotate_towards(enemy, player.x, player.z, speed=3)

    if distance < SNIPER_MIN_DISTANCE:
        enemy.move_backward(enemy.speed * 1.5) # retreats
    elif distance > SNIPER_MAX_DISTANCE:
        enemy.move_forward(enemy.speed * 0.5) # inches closer
    # Otherwise snipe

    angle_diff = (math.degrees(math.atan2(dx, -dz)) - enemy.angle + 360) % 360
    if angle_diff > 180:
        angle_diff = 360 - angle_diff
    if angle_diff < 10:  # only fires when well aimed
        return shot_attempt(enemy, distance, SNIPER_MAX_DISTANCE, cooldown * 1.5)


def guard(enemy, player, cooldown):
    """Patrols a fixed area. Attacks when player enters range, returns after."""
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    player_distance = math.sqrt(dx**2 + dz**2)

    # Store spawn/home position
    if not hasattr(enemy, "home_x"):
        enemy.home_x = enemy.x
        enemy.home_z = enemy.z
        enemy.patrol_angle = 0

    if player_distance < GUARD_PATROL_RADIUS * 2:
        enemy.rotate_towards(enemy, player.x, player.z)
        if player_distance > 5.0:
            enemy.move_forward(enemy.speed)
        return shot_attempt(enemy, player_distance, 15.0, cooldown)
    else:
        # Player out of range — patrol home area
        home_dx = enemy.home_x - enemy.x
        home_dz = enemy.home_z - enemy.z
        home_distance = math.sqrt(home_dx**2 + home_dz**2)

        if home_distance > GUARD_PATROL_RADIUS:
            # Return towards home
            enemy.rotate_towards(enemy, enemy.home_x, enemy.home_z)
            enemy.move_forward(enemy.speed)
        else:
            # Circle patrol around home
            enemy.patrol_angle = (enemy.patrol_angle + 1) % 360
            patrol_x = enemy.home_x + math.sin(math.radians(enemy.patrol_angle)) * (GUARD_PATROL_RADIUS * 0.5)
            patrol_z = enemy.home_z + math.cos(math.radians(enemy.patrol_angle)) * (GUARD_PATROL_RADIUS * 0.5)
            enemy.rotate_towards(enemy, patrol_x, patrol_z)
            enemy.move_forward(enemy.speed * 0.7)