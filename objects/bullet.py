import math

class Bullet:
    def __init__(self, shooter, shooter_type):
        self.x = shooter.x
        self.y = shooter.y
        self.z = shooter.z
        self.angle = shooter.angle
        self.shooter = shooter_type

    def update(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed
        
