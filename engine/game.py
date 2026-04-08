from objects.game import Game
from objects.world import World
from objects.player import Player

def launch_game():
    player = Player()
    world = World(player, level=0)
    game = Game(player=player, world=world)
    
    # start_menu() <- this will eventually trigger the game loop, but for now we can just start the game directly
    game.start_game()
