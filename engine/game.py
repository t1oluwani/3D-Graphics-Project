from objects.game import Game
from objects.world import World
from objects.player import Player

from engine.window import create_window

def launch_game():
    player = Player()
    world = World(player, level=0)
    game = Game(player=player, world=world)
    
    # start_menu()
    create_window(width=1024, height=768, title="Atari Battlezone Window", game=game)