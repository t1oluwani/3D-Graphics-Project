import random
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.enemy import spawn_enemy_at

class World:
    def __init__(self, player, level, size=2000):
        self.size = size
        self.objects = []
        self.enemies = []
        self.level = level
        self.ref_angle = player.angle
        self.generate_world()

    def generate_world(self):
        difficulty_factor = self.level*2
                
        for _ in range(11 + difficulty_factor):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(10 + difficulty_factor):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})
        for _ in range(5 + difficulty_factor):
            self.enemies.append(spawn_enemy_at(*self.get_random_pos()))
            
    def clear_world(self):
        self.objects = []
        self.enemies = []

    def get_random_pos(self):
        while True:
            x = random.randint(-50, 50)
            z = random.randint(-50, 50)
            a = random.randint(0, 360)
            if abs(x) > 1 or abs(z) > 1:
                return (x, z, a)
            
    def update_level(self, player):
        self.level += 1
        self.clear_world()
        self.ref_angle = player.angle
        self.generate_world()


