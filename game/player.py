import math

class Player:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = -5.0
        self.angle = 0.0  # degrees

    def move_forward(self, speed):
        radians = math.radians(self.angle)
        self.x -= math.sin(radians) * speed
        self.z += math.cos(radians) * speed

    def move_backward(self, speed):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed

    def rotate_right(self, amount):
        self.angle += amount
        self.angle %= 360

    def rotate_left(self, amount):
        self.angle -= amount
        self.angle %= 360

    def shoot(self):
        pass
