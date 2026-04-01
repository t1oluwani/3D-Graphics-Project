import math
from game.bullet import Bullet

MOVEMENT_SPEED = 0.1
ROTATION_AMOUNT = 1.5

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.angle = 0  # degrees

    def move_forward(self, speed=MOVEMENT_SPEED):
        radians = math.radians(self.angle)
        self.x += math.sin(radians) * speed
        self.z -= math.cos(radians) * speed

    def move_backward(self, speed=MOVEMENT_SPEED):
        radians = math.radians(self.angle)
        self.x -= math.sin(radians) * speed
        self.z += math.cos(radians) * speed

    def rotate_right(self, amount=ROTATION_AMOUNT):
        self.angle += amount
        self.angle %= 360

    def rotate_left(self, amount=ROTATION_AMOUNT):
        self.angle -= amount
        self.angle %= 360

    def shoot(self):
        return Bullet(self)
