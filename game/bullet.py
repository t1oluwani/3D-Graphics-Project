import math

class Bullet:
    def __init__(self, player):
        self.x = player.x
        self.y = player.y
        self.z = player.z
        self.angle = player.angle

    def update(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed
        
