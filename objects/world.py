import random
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.enemy import spawn_enemy_at

class World:
    def __init__(self, player, level, max_level=1, size=2000):
        self.size = size
        self.objects = []
        self.enemies = []
        self.level = level
        self.max_level = max_level
        self.ref_angle = player.angle
        self.generate_world()

    def get_random_pos(self):
        player_safe_zone = 5  # objects won't spawn within this distance of the player
        
        while True:
            x = random.randint(-50, 50) 
            z = random.randint(-50, 50)
            a = random.randint(0, 360)
            if abs(x) > player_safe_zone or abs(z) > player_safe_zone:  # ensure objects don't spawn too close to the player
                return (x, z, a)
            
    def generate_world(self):
        difficulty_factor = (self.level-1)*2
                
        for _ in range(12 + difficulty_factor*2):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(9 + difficulty_factor*2):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})
        for _ in range(3 + difficulty_factor):
            self.enemies.append(spawn_enemy_at(*self.get_random_pos()))
            
        self.init_enemy_count = len(self.enemies)
            
    def clear_world(self):
        self.objects = []
        self.enemies = []
            
    def update_level(self, player):
        self.level += 1
        self.clear_world()
        self.ref_angle = player.angle
        self.generate_world()


