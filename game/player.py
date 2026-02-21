import math

class Player:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = -5.0
        self.angle = 0.0

    def move_forward(self, speed):
        self.x += math.sin(self.angle) * speed
        self.z += math.cos(self.angle) * speed

    def move_backward(self, speed):
        self.x -= math.sin(self.angle) * speed
        self.z -= math.cos(self.angle) * speed
    
    def rotate_right(self, amount):
        self.angle += amount
        
    def rotate_left(self, amount):
        self.angle -= amount

    def shoot(self):
        # todo
        pass