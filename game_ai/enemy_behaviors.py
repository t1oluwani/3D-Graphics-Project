import math
import time

CLOSE_RANGE = 15
STANDARD_RANGE = 25
SNIPER_RANGE = 75

GUARD_PATROL_RADIUS = 8.0
HUNTER_CHARGE_DISTANCE = 10.0

def get_distance(enemy, player):
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    return math.sqrt(dx**2 + dz**2), dx, dz

def shot_attempt(enemy, distance, range, cooldown):
    if distance < range:
        now = time.time()
        if not hasattr(enemy, "last_shot") or now - enemy.last_shot > cooldown:
            enemy.last_shot = now
            return enemy.shoot()

def simple_enemy(enemy, player, cooldown):
    """Basic enemy that moves towards the player and shoots when in range."""
    d_delta, dx, dz = get_distance(enemy, player)
    enemy.rotate_towards(dx, dz)


    if d_delta > 10.0:
        enemy.move_forward(enemy.speed)


    return shot_attempt(enemy, d_delta, 15.0, cooldown)


def hunter(enemy, player, cooldown):
    """Aggressively chases the player and closes distance to point blank."""
    d_delta, dx, dz = get_distance(enemy, player)
    enemy.rotate_towards(dx, dz)

    # Always charges unless point blank
    if d_delta > HUNTER_CHARGE_DISTANCE:
        enemy.move_forward(enemy.speed)
    elif d_delta > 3:
        enemy.move_forward(enemy.speed * 2)

    return shot_attempt(
        enemy,
        d_delta,
        range=CLOSE_RANGE,  # closer range
        cooldown=(cooldown * 0.75),  # faster shooting
    )

def sniper(enemy, player, cooldown):
    """Keeps distance and shoots from afar. Retreats if player gets too close."""
    d_delta, dx, dz = get_distance(enemy, player)
    enemy.rotate_towards(dx, dz)

    if d_delta < SNIPER_RANGE:
        enemy.move_backward(enemy.speed * 1.5)  # retreats
    elif d_delta > SNIPER_RANGE:
        enemy.move_forward(enemy.speed * 0.5)  # inches closer
    # Otherwise snipe

    return shot_attempt(
        enemy, 
        d_delta, 
        range=SNIPER_RANGE,  # longer range
        cooldown=(cooldown * 1.5) # slower shooting
    )


def guard(enemy, player, cooldown):
    """Patrols a fixed area. Attacks when player enters range, returns after."""
    d_delta, dx, dz = get_distance(enemy, player)

    # Store spawn/home position
    if not hasattr(enemy, "home_x"):
        enemy.home_x = enemy.x
        enemy.home_z = enemy.z
        enemy.patrol_angle = 0

    if d_delta < GUARD_PATROL_RADIUS * 2:
        enemy.rotate_towards(dx, dz)
        if d_delta > 5.0:
            enemy.move_forward(enemy.speed)
        return shot_attempt(enemy, d_delta, 15.0, cooldown)
    else:
        # Player out of range — patrol home area
        home_dx = enemy.home_x - enemy.x
        home_dz = enemy.home_z - enemy.z
        home_distance = math.sqrt(home_dx**2 + home_dz**2)

        if home_distance > GUARD_PATROL_RADIUS:
            # Return towards home
            enemy.rotate_towards(enemy.home_x, enemy.home_z)
            enemy.move_forward(enemy.speed)
        else:
            # Circle patrol around home
            enemy.patrol_angle = (enemy.patrol_angle + 1) % 360
            patrol_x = enemy.home_x + math.sin(math.radians(enemy.patrol_angle)) * (
                GUARD_PATROL_RADIUS * 0.5
            )
            patrol_z = enemy.home_z + math.cos(math.radians(enemy.patrol_angle)) * (
                GUARD_PATROL_RADIUS * 0.5
            )
            enemy.rotate_towards(patrol_x, patrol_z)
            enemy.move_forward(enemy.speed * 0.7)
