import math

class Bullet:
    def __init__(self, shooter, shooter_type):
        self.x = shooter.x
        self.z = shooter.z
        self.angle = shooter.angle
        self.shooter = shooter_type

    def update(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        
        if self.shooter == "player":
            self.z -= math.cos(radians) * speed
        else:
            self.z += math.cos(radians) * speed
        
