import math

def draw_player(x, y, z, angle):
    print(f"Drawing player at position ({x}, {y}, {z}) with angle {angle}")
    #todo
    
def draw_bullet(x, y, z):
    print(f"Drawing bullet at position ({x}, {y}, {z})")
    #todo

def player_shoot(x, y, z, angle):
    print(f"Player shoots from position ({x}, {y}, {z}) at angle {angle}")
    #todo

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
        player_shoot(self.x, self.y, self.z, self.angle)
