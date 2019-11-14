import game_framework
import pico2d
import start_state
from player import Player

# fill here

pico2d.open_canvas(game_framework.Width, game_framework.Height)
game_framework.player = Player()
game_framework.run(start_state)
pico2d.close_canvas()
