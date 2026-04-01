import math
from game.bullet import Bullet

DEFAULT_HEALTH = 100

def patrol():
    pass

def attack():
    pass

def spawn_enemy_at(x, z, angle):
    return Enemy(x, 0, z, angle)
    
class Enemy:
    def __init__(self, x, y, z, angle, level=1):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.health = DEFAULT_HEALTH * level

    def move_forward(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z += math.cos(radians) * speed

    def move_backward(self, speed):
        radians = math.radians(self.angle)
        self.x -= math.sin(radians) * speed
        self.z -= math.cos(radians) * speed
        
    def rotate_right(self, amount):
        self.angle += amount
        self.angle %= 360

    def rotate_left(self, amount):
        self.angle -= amount
        self.angle %= 360
        
    def shoot(self):
        return Bullet(self)
    
    def enemy_ai(self, player):
        pass
        # Simple AI: Move towards the player and shoot if in range
        # dx = player.x - self.x
        # dz = player.z - self.z
        # distance = math.sqrt(dx**2 + dz**2)

        # if distance > 1.0:
        #     self.move_forward(0.05)
        
        # # Rotate towards the player
        # target_angle = math.degrees(math.atan2(dx, dz))
        # angle_diff = (target_angle - self.angle + 360) % 360
        # if angle_diff > 180:
        #     self.rotate_left(min(5, 360 - angle_diff))
        # else:
        #     self.rotate_right(min(5, angle_diff))

        # # Shoot if within range
        # if distance < 3.0:
        #     return self.shoot()
        
        # return None
