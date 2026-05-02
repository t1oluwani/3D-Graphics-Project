from engine.configs import EOW_BOUNDARY

def get_position(entity):
    if hasattr(entity, "x") and hasattr(entity, "z"):
        # entities (coordinates stored as attributes)
        return entity.x, entity.z
    elif isinstance(entity, dict) and "pos" in entity:
        # objects (coordinates stored in a dict)
        x, z, _ = entity["pos"]
        return x, z

def check_collision(a, b, tolerance):
    ax, az = get_position(a)
    bx, bz = get_position(b)

    dx = ax - bx
    dz = az - bz

    distance = (dx**2 + dz**2) ** 0.5
    return distance < tolerance

def check_EoW_collision(entity):
    x, z = get_position(entity)
    return (x**2 + z**2) > (EOW_BOUNDARY ** 2)

def is_shooter_player(bullet):
    return bullet.shooter == "player"

def is_shooter_enemy(bullet):
    return bullet.shooter == "enemy"

def bullet_hit(bullet, game):
    player = game.world.player

     # Bullet hits player (only if shot by enemy)
    if is_shooter_enemy(bullet) and check_collision(bullet, player, 1.75):
        game.take_damage(5)
        return True

    # Bullet hits enemies (only if shot by player)
    if is_shooter_player(bullet):
        for enemy in game.world.enemies:
            if check_collision(bullet, enemy, 1.75):
                enemy.take_damage(20, game)
                return True

    # Bullet hits objects
    for obj in game.world.objects:
        if check_collision(bullet, obj, 1.5):
            return True

    return False
