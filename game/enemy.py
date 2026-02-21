import math

class Enemy:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.angle = 0.0  # degrees

    def move_forward(self, speed):
        radians = math.radians(self.angle)
        self.x -= math.sin(radians) * speed
        self.z += math.cos(radians) * speed

    def move_backward(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed
        
    def attack_player(self):
        # todo
        pass
