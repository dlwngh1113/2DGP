import game_framework
from pico2d import *
import game_world
from chasha import Chasha
from map import Map

boss = None


def enter():
    global boss
    boss = Chasha()
    game_world.add_object(Map('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\codes\\map1.txt'), 0)
    pass


def exit():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    game_framework.player.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass
