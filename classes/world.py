from OpenGL.GL import *
from OpenGL.GLU import *

import random

class World:
    def __init__(self, player, size=2000):
        self.size = size
        self.objects = []
        self.ref_angle = player.angle
        self.generate_world()

    def generate_world(self):        
        for _ in range(11):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(10):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})

    def get_random_pos(self):
        while True:
            x = random.randint(-self.size, self.size)
            z = random.randint(-self.size, self.size)
            if abs(x) > 100 or abs(z) > 100:
                return (x, z)


