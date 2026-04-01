def player_enemy_collision(player, enemy):
    # Simple collision check based on distance
    dx = player.x - enemy.x
    dz = player.z - enemy.z

    tolerance = 2
    distance = (dx**2 + dz**2) ** 0.5

    return distance < tolerance


def player_object_collision(player, object):
    # Similar to enemy collision but with a static object
    object_x, object_z, _ = object["pos"]

    dx = player.x - object_x
    dz = player.z - object_z

    tolerance = 1.75
    distance = (dx**2 + dz**2) ** 0.5

    return distance < tolerance


def bullet_enemy_collision(bullet, enemy):
    # Check if bullet is close enough to enemy to count as a hit
    dx = bullet.x - enemy.x
    dz = bullet.z - enemy.z

    tolerance = 1.75  # tighter tolerance for hitbox
    distance = (dx**2 + dz**2) ** 0.5

    return distance < tolerance


def bullet_object_collision(bullet, object):
    # Check if bullet is close enough to object to count as a hit
    object_x, object_z, _ = object["pos"]

    dx = bullet.x - object_x
    dz = bullet.z - object_z

    tolerance = 1.5  # tighter tolerance for objects
    distance = (dx**2 + dz**2) ** 0.5

    return distance < tolerance


def bullet_hit(bullet, world):
    for enemy in world.enemies:
        if bullet_enemy_collision(bullet, enemy):
            enemy.health -= 20
            return True
    for obj in world.objects:
        if bullet_object_collision(bullet, obj):
            return True
    return False
