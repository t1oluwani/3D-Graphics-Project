import math, time
from math3d.raycasting import raycast
from math3d.pathfinding import pathfind_step

CLOSE_RANGE = 15
STANDARD_RANGE = 35
SNIPER_RANGE = 75
START_CHARGE_DISTANCE = 10.0
END_CHARGE_DISTANCE = 3.0
PATROL_RADIUS = 8.0

def get_distance(enemy, player):
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    return math.sqrt(dx**2 + dz**2), dx, dz


def shot_attempt(enemy, distance, range, cooldown):
    if not raycast(enemy, enemy.world.player, enemy.world.objects)  and distance < range:
        now = time.time()
        if not hasattr(enemy, "last_shot") or now - enemy.last_shot > cooldown:
            enemy.last_shot = now
            return enemy.shoot()


def simple_enemy(enemy, player, cooldown):
    """Basic enemy that moves towards the player and shoots when in range."""
    d_delta, dx, dz = get_distance(enemy, player)
    enemy.rotate_towards(dx, dz)

    if d_delta > 10.0:
        pathfind_step(enemy, player, enemy.world.objects, enemy.world.enemies)

    return shot_attempt(enemy, d_delta, 15.0, cooldown)

def hunter(enemy, player, cooldown):
    """Aggressively chases the player and closes distance to near point blank."""
    d_delta, dx, dz = get_distance(enemy, player)
    enemy.rotate_towards(dx, dz)

    # charges faster when at close range
    if d_delta > START_CHARGE_DISTANCE:
        pathfind_step(enemy, player, enemy.world.objects, enemy.world.enemies)
    elif d_delta > END_CHARGE_DISTANCE:
        pathfind_step(enemy, player, enemy.world.objects, enemy.world.enemies, speed=enemy.speed * 2)

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
        pathfind_step(enemy, player, enemy.world.objects, enemy.world.enemies, speed=enemy.speed * 0.5)  # inches closer
    # Otherwise snipe

    return shot_attempt(
        enemy,
        d_delta,
        range=SNIPER_RANGE,  # longer range
        cooldown=(cooldown * 1.5),  # slower shooting
    )

def guard(enemy, player, cooldown):
    d_delta, dx, dz = get_distance(enemy, player)
    if not hasattr(enemy, "home_x"):
        enemy.home_x = enemy.x
        enemy.home_z = enemy.z
        enemy.patrol_angle = enemy.angle
        enemy.state = "patrol"

    # State: attack
    if d_delta < PATROL_RADIUS * 4:
        enemy.state = "attack"
        enemy.rotate_towards(dx, dz)
        if d_delta > 5.0:
            pathfind_step(enemy, player, enemy.world.objects, enemy.world.enemies)
        return shot_attempt(
            enemy,
            d_delta,
            range=STANDARD_RANGE,
            cooldown=cooldown
        )

    # State: return home
    home_dx = enemy.home_x - enemy.x
    home_dz = enemy.home_z - enemy.z
    home_distance = math.sqrt(home_dx**2 + home_dz**2)

    if home_distance > PATROL_RADIUS and enemy.state != "patrol":
        enemy.state = "returning"

        # Create a temporary target object to reuse pathfind_step
        class HomeTarget:
            x = enemy.home_x
            z = enemy.home_z
        pathfind_step(enemy, HomeTarget(), enemy.world.objects, enemy.world.enemies)
    else:
        # State: patrol
        enemy.state = "patrol"
        enemy.patrol_angle = (enemy.patrol_angle + 0.2) % 360
        enemy.angle = enemy.patrol_angle
        enemy.move_forward(enemy.speed)
