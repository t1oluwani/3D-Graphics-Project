import random
from OpenGL.GL import *
from OpenGL.GLU import *

from objects.enemy import spawn_enemy_at

difficulty_mapping = {
    "": 1,
    "easy": 1,
    "medium": 2,
    "hard": 3
}

class World:
    def __init__(self, player, level, max_level=5, size=2000):
        self.size = size
        self.objects = []
        self.enemies = []
        self.level = level
        self.difficulty = ""
        self.max_level = max_level
        self.ref_angle = player.angle
        
    def get_random_pos(self, enemy=False):
        player_safe_zone = 5 if enemy else 1 # differing safe zones for enemies vs objects 
            
        while True:
            x = random.randint(-50, 50) 
            z = random.randint(-50, 50)
            a = random.randint(0, 360)
            if abs(x) > player_safe_zone or abs(z) > player_safe_zone:
                return (x, z, a)
            
    def generate_world(self, difficulty):
        level_factor = (self.level-1)*2
        difficulty_factor = difficulty_mapping.get(difficulty, 1) + 2
                
        for _ in range(difficulty_factor*4 + level_factor*2):
            self.objects.append({'type': 'pyramid', 'pos': self.get_random_pos()})
        for _ in range(difficulty_factor*3 + level_factor*2):
            self.objects.append({'type': 'block', 'pos': self.get_random_pos()})
        for _ in range(difficulty_factor + level_factor):
            self.enemies.append(spawn_enemy_at(*self.get_random_pos()))
            
        # Debug lines (TODO: DELETE)
        print(f"Generating world for level {self.level} with difficulty '{difficulty}'...")
        print(f"Generated {len(self.objects)} objects and {len(self.enemies)} enemies.")
            
        self.init_enemy_count = len(self.enemies)
            
    def clear_world(self):
        self.objects = []
        self.enemies = []
            
    def update_level(self, player):
        self.level += 1
        self.clear_world()
        self.ref_angle = player.angle
        self.generate_world(self.difficulty)


