import game_framework
from pico2d import *
from map import Map
import game_world
import start_state

image = None
timer = 0.0

def enter():
    global image, timer
    game_framework.player.money -= int(game_framework.player.money * 0.1)
    image = load_image('image_resources\\you died.png')
    game_world.add_object(Map('map1.txt'), 0)
    timer = get_time()
    pass

def exit():
    global image
    game_world.clear()
    del image
    pass


def handle_events():
    pass


def update():
    if get_time() - timer > 4.0:
        game_framework.change_state(start_state)
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    image.draw(300, 500, 400, 200)
    update_canvas()


def pause():
    pass


def resume():
    pass
