import math

from objects.player import Player

class Bullet:
    def __init__(self, shooter):
        self.x = shooter.x
        self.y = shooter.y
        self.z = shooter.z
        self.angle = shooter.angle
        self.shooter = "player" if isinstance(shooter, Player) else "enemy"

    def update(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed
        
