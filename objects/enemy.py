import math
from objects.bullet import Bullet
from game_ai.enemy_behaviors import simple_enemy, hunter, sniper, guard

DEFAULT_HEALTH = 100

def spawn_enemy_at(x, z, angle, level, type):
    return Enemy(x, 0, z, angle, level, type)
    
class Enemy:
    def __init__(self, x, y, z, angle, level, type=""):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.speed = 0.03 + (level - 1) * 0.015
        self.level = level
        self.health = DEFAULT_HEALTH + (level - 1) * 20  
        self.type = type
        
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

    def rotate_towards(self, tx, tz):
        dx = tx - self.x
        dz = tz - self.z

        target_angle = math.degrees(math.atan2(dx, dz))
        angle_diff = (target_angle - self.angle + 360) % 360
        
        if angle_diff > 180:
            self.rotate_left(min(5, 360 - angle_diff))
        else:
            self.rotate_right(min(5, angle_diff))
        return angle_diff
        
    def update(self, player):
        cooldown = 5.0 - (self.level - 1) * 0.5
        
        match self.type:
            case "hunter":
                return hunter(self, player, cooldown)
            case "sniper":
                return sniper(self, player, cooldown)
            case "guard":
                return guard(self, player, cooldown)
            case _:
                return simple_enemy(self, player, cooldown)
        
    def shoot(self):
        return Bullet(self, "enemy")
    
    def take_damage(self, amount, game):
        self.health -= amount
        
        if self.health <= 0:
            game.world.enemies.remove(self)
            game.score += 100 * (game.world.level)

