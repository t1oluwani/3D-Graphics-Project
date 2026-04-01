import random
from OpenGL.GL import *
from OpenGL.GLU import *

from game.enemy import spawn_enemy_at

class World:
    def __init__(self, player, size=2000):
        self.size = size
        self.objects = []
        self.enemies = []
        self.ref_angle = player.angle
        self.generate_world()

    def generate_world(self):        
        for _ in range(11):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(10):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})
        for _ in range(5):
            self.enemies.append(spawn_enemy_at(*self.get_random_pos()))

    def get_random_pos(self):
        while True:
            x = random.randint(-50, 50)
            z = random.randint(-50, 50)
            a = random.randint(0, 360)
            if abs(x) > 1 or abs(z) > 1:
                return (x, z, a)


