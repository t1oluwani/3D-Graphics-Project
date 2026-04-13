from objects.game import Game
from objects.world import World
from objects.player import Player

def launch_game():
    player = Player()
    world = World(player, level=1)
    game = Game(player=player, world=world)
    
    game.start_game()
