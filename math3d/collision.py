
def enemy_collision (player, enemy):
    # Simple collision check based on distance
    tolerance = 50
    dx = player.x - enemy.x
    dz = player.z - enemy.z
    distance = (dx**2 + dz**2) ** 0.5
    if distance < tolerance:
        print(f"Player position: ({player.x}, {player.y}, {player.z})")
        print(f"Enemy position: ({enemy.x}, {enemy.y}, {enemy.z})")
        print(f"Distance: {distance}, Tolerance: {tolerance}")
        print("Collision with enemy")

    return distance < tolerance

def object_collision(player, object):
    # Similar to enemy collision but with a static object
    tolerance = 1.5
    object_x, object_y, object_z = object["pos"]
    dx = player.x - object_x
    dz = player.z - object_z
    distance = (dx**2 + dz**2) ** 0.5
    print("Object Collision")
    return distance < tolerance
    
def shooting_collision(bullet, enemy):
    # Check if bullet is close enough to enemy to count as a hit
    tolerance = 0.5
    enemy_x, enemy_y, enemy_z = enemy["pos"]
    dx = bullet.x - enemy_x
    dz = bullet.z - enemy_z
    distance = (dx**2 + dz**2) ** 0.5
    print("Shooting Collision")
    return distance < tolerance