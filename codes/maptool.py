from pico2d import *
import math

open_canvas(550, 750)
map_list = []


def load():
    pass


def save():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            print('sibak')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            save()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load()
    pass


def draw():
    pass


def init():
    global map_list
    for i in range(15):
        line = []
        for j in range(11):
            line.append(0)
        map_list.append(line)
    pass


init()
while True:
    handle_events()
