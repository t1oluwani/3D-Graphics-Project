import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.enemy import spawn_enemy_at
from engine.configs import EOW_BOUNDARY
class World:
    def __init__(self, player, level, size=2000):
        self.size = size
        self.objects = []
        self.enemies = []
        self.level = level
        self.difficulty = 0
        self.max_level = 0
        self.player = player
        self.ref_angle = player.angle
        
    def get_random_pos(self, enemy=False):
        player_safe_zone = 3 if enemy else 0.5 # differing safe zones for enemies vs objects 
            
        while True:
            # x = random.randint(-EOW_BOUNDARY, EOW_BOUNDARY) 
            # z = random.randint(-EOW_BOUNDARY, EOW_BOUNDARY)
            # a = random.randint(0, 360)
            # if abs(x) > player_safe_zone or abs(z) > player_safe_zone:
            #     return (x, z, a)
            
            r = EOW_BOUNDARY * (random.random() ** 0.5)
            theta = random.uniform(0, 2 * math.pi)

            x = r * math.cos(theta)
            z = r * math.sin(theta)
            a = random.randint(0, 360)

            if (x**2 + z**2) > player_safe_zone**2:
                return (x, z, a)
            
            
    def generate_world(self, difficulty):
        level_factor = (self.level-1)*2
        difficulty_factor = difficulty + 2
                
        for _ in range(difficulty_factor*4 + level_factor*2):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(difficulty_factor*3 + level_factor*2):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})
        for _ in range(difficulty_factor + level_factor):
            self.enemies.append(spawn_enemy_at(*self.get_random_pos(), self.level))
            
        self.init_enemy_count = len(self.enemies)
            
    def clear_world(self):
        self.objects = []
        self.enemies = []
            
    def update_level(self, player):
        self.level += 1
        self.clear_world()
        self.ref_angle = player.angle
        self.generate_world(self.difficulty)


