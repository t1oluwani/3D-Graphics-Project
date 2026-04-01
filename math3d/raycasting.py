import math

def raycast_enemy(player, enemy, radius=1.25):
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

    return dist_sq < radius**2