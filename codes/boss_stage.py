import game_framework
from pico2d import *
import game_world
from chasha import Chasha
from map import Map

chasha = None

def enter():
    global chasha
    chasha = Chasha()
    game_world.add_object(Map('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\codes\\map1.txt'), 0)
    game_world.add_object(chasha, 1)
    pass


def exit():
    global chasha
    game_world.remove_object(chasha)
    del chasha
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            game_framework.player.attack(event)
        else:
            game_framework.player.handle_event(event)
    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    game_framework.player.update()
    delay(0.05)
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
