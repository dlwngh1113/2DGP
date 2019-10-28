from pico2d import *
import game_framework
import stage_state
import item_
from player import Player

name = "StartState"
image = None
player = None


def enter():
    global image, player
    image = load_image('main page.png')
    player = Player()
    pass


def exit():
    global image
    del (image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_state(item_)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_framework.push_state(stage_state)
    pass

def update():
    pass


def draw():
    global image, player
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    update_canvas()


def pause():
    pass


def resume():
    pass
