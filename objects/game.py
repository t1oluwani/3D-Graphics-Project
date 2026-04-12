from OpenGL.GL import *
from OpenGL.GLU import *

from engine.window import create_window

class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.score = 0
        self.health = 100
        self.game_over_loss = False
        self.game_over_win = False
        
    def start_game(self):
        create_window(width=1024, height=768, title="Mock Atari Battlezone Window", game=self)
        
    def next_level(self):
        if self.world.level >= self.world.max_level:
            self.game_over_win = True
            print("Congratulations! You've completed all levels!")
            return
        self.world.update_level(self.player)
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game_over_loss = True
            print("Game Over! You've been defeated.")
        
    def game_over(self):
        return self.game_over_loss or self.game_over_win
            
            
            


