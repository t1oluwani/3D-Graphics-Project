import math 
import time

from OpenGL.GL import *
from OpenGL.GLU import *

from engine.window import create_window
from render.displays import display_game_over
from engine.configs import SCREEN_WIDTH, SCREEN_HEIGHT

difficulty_settings = {  # later add enemy count and ratio (there are going to be 3 enemy ai types, patrol, aggressive/chase, and hider/sniper)
    "easy": {"numeric": 1, "max_level": 3, "health": 100, "enemy_speed": 0.025},
    "normal": {"numeric": 2, "max_level": 5, "health": 200, "enemy_speed": 0.50},
    "hard": {"numeric": 3, "max_level": 7, "health": 300, "enemy_speed": 0.075},
}

class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.score = 0
        self.health = 100
        self.difficulty = ""
        self.game_over_loss = False
        self.game_over_win = False
        self.damage_flash_start = None

    def set_difficulty(self, difficulty):
        settings = difficulty_settings.get(difficulty, difficulty_settings["easy"])
        numeric_difficulty = settings["numeric"]
        self.difficulty = difficulty
        self.health = settings["health"]
        self.world.max_level = settings["max_level"]
        self.world.difficulty = numeric_difficulty
        self.world.generate_world(numeric_difficulty)

    def start_game(self):
        create_window(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title="Mock Atari Battlezone Window",
            game=self,
        )

    def next_level(self):
        if self.world.level >= self.world.max_level:
            display_game_over(win=True)
            # self.game_over_win = True
            print("Congratulations! You've completed all levels!")
            return
        self.world.update_level(self.player)

    def take_damage(self, amount):
        self.damage_flash_start = time.time()
        self.health -= amount * (self.world.level * 0.5 + 0.5)
        if self.health <= 0:
            display_game_over(win=False)
            print("Game Over! You've been defeated.")

    def game_over(self):
        return self.game_over_loss or self.game_over_win
    
