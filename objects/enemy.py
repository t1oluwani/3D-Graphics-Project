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
        
    def update(self, player):
        match self.type:
            case "hunter":
                return hunter(self, player)
            case "sniper":
                return sniper(self, player)
            case "guard":
                return guard(self, player)
            case _:
                return simple_enemy(self, player)
        
    def shoot(self):
        return Bullet(self)
    
    def take_damage(self, amount, game):
        self.health -= amount
        
        if self.health <= 0:
            game.world.enemies.remove(self)
            game.score += 100 * (game.world.level)

