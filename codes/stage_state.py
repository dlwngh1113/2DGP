from pico2d import *
import game_framework
import item_state
import start_state
from golem import Golem
from ghost import Ghost
import arrow

name = "StageState"
image = None
timer = None
golem_swarm = []
ghost_swarm = []


def enter():
    global image, timer
    start_state.player.stage_init()
    timer = 1000
    pass


def exit():
    global image, golem_swarm, ghost_swarm
    while len(golem_swarm) > 0:
        golem_swarm.pop()
    while len(ghost_swarm) > 0:
        ghost_swarm.pop()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            start_state.player.attack(event)
        else:
            start_state.player.handle_event(event)
    pass


def update():
    global golem_swarm, ghost_swarm, timer
    start_state.player.update()
    for golem in golem_swarm:
        golem.update()
    for ghost in ghost_swarm:
        ghost.update()
    if timer == 0:
        golem_swarm.insert(0, Golem())
        ghost_swarm.insert(0, Ghost())
        timer = 1000
    timer -= 100
    pass


def draw():
    global image, golem_swarm, ghost_swarm
    clear_canvas()
    # image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    start_state.player.draw()
    for golem in golem_swarm:
        golem.draw()
    for ghost in ghost_swarm:
        ghost.draw()
    delay(0.1)
    update_canvas()


def pause():
    pass


def resume():
    pass
