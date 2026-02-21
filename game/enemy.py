import math

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = -5
        self.angle = 0

    def move_forward(self, speed):
        self.x += math.sin(self.angle) * speed
        self.z += math.cos(self.angle) * speed

    def move_backward(self, speed):
        self.x -= math.sin(self.angle) * speed
        self.z -= math.cos(self.angle) * speed

        
    def attack_player(self):
        # todo
        pass
