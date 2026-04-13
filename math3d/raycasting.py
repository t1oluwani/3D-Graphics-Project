import math

ENEMY_RADIUS = 1.25  # hit detection radius
OBSTACLE_RADIUS = 1.25  # interference detection radius

def raycast_enemy(player, enemy, obstacles):
    # Raycast from a player to enemy, true if hit.
    
    # Ray origin
    ox, oz = player.x, player.z

    # Ray direction from player's angle
    radians = math.radians(player.angle)
    dx = math.sin(radians)
    dz = -math.cos(radians)

    # Vector from ray origin to enemy center
    ex = enemy.x - ox
    ez = enemy.z - oz

    # Project enemy onto ray
    t = ex * dx + ez * dz

    if t < 0:
        return False  # enemy is behind player

    # Closest point on ray to enemy center
    closest_x = ox + dx * t - enemy.x
    closest_z = oz + dz * t - enemy.z
    dist_sq = closest_x**2 + closest_z**2
    
     # Check if any obstacle blocks the ray before reaching the enemy
    for obs in obstacles:
        ox2 = obs['pos'][0] - ox
        oz2 = obs['pos'][1] - oz

        # Project obstacle onto ray
        t_obs = ox2 * dx + oz2 * dz

        if t_obs < 0 or t_obs >= t:
            continue  # obstacle is behind player or beyond the enemy

        # Closest point on ray to obstacle center
        cx = ox + dx * t_obs - obs['pos'][0]
        cz = oz + dz * t_obs - obs['pos'][1]
        obs_dist_sq = cx**2 + cz**2

        if obs_dist_sq < OBSTACLE_RADIUS**2:
            return False  # obstacle blocks the ray

    return dist_sq < ENEMY_RADIUS**2

def dev_raycast_enemy(player, enemy):
    # Raycast from a player to enemy, true if hit (goes through walls for development/debug purposes).
    
    # Ray origin
    ox, oz = player.x, player.z

    # Ray direction from player's angle
    radians = math.radians(player.angle)
    dx = math.sin(radians)
    dz = -math.cos(radians)

    # Vector from ray origin to enemy center
    ex = enemy.x - ox
    ez = enemy.z - oz

    # Project enemy onto ray
    t = ex * dx + ez * dz

    if t < 0:
        return False  # enemy is behind player

    # Closest point on ray to enemy center
    closest_x = ox + dx * t - enemy.x
    closest_z = oz + dz * t - enemy.z
    dist_sq = closest_x**2 + closest_z**2

    return dist_sq < ENEMY_RADIUS**2