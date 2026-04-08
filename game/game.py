import random
from OpenGL.GL import *
from OpenGL.GLU import *

class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.score = 0
        self.health = 100
        self.game_over = False
        
    def start(self):
        while not self.game_over:
            ...
            
            


