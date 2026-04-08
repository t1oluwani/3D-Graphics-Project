import random
from OpenGL.GL import *
from OpenGL.GLU import *

from render.hud import draw_hud

class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.score = 0
        self.health = 100
        self.game_over = False
        
    def show_menu(self):
        #TODO
        pass
        
                
    def update(self):
        #TODO
        pass
        
    def start(self):
        while not self.game_over:
            draw_hud(self.score, self.health)
            self.update()
            
            
            


