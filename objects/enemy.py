import math
from objects.bullet import Bullet
from game_ai.enemy_behaviors import simple_enemy, hunter, sniper, guard

DEFAULT_HEALTH = 100

def attack():
    pass

def spawn_enemy_at(x, z, angle, level):
    return Enemy(x, 0, z, angle, level)
    
class Enemy:
    def __init__(self, x, y, z, angle, level):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.health = DEFAULT_HEALTH + (level - 1) * 20  
        # self.type = ...

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
        
    def update(self, player):
        return simple_enemy(self, player)
        
    def shoot(self):
        return Bullet(self)
    
    def take_damage(self, amount):
        self.health -= amount

