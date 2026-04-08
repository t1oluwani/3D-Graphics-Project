from OpenGL.GL import *
from OpenGL.GLU import *

from engine.window import create_window

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
        
    def start_game(self):
        while not self.game_over:
            create_window(width=1024, height=768, title="Mock Atari Battlezone Window", game=self)
            # self.update()
            
            
            


