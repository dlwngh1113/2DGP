from pico2d import *
import game_framework
import item_state
import start_state
from golem import Golem
from ghost import Ghost
import random
import arrow
from map import Map

name = "StageState"
image = None
timer = None
map = None
golem_swarm = []
ghost_swarm = []


def enter():
    global image, timer, map
    game_framework.player.stage_init()
    map = Map('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\codes\\map1.txt')
    timer = 1000
    pass


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def exit():
    global image, golem_swarm, ghost_swarm
    while len(golem_swarm) > 0:
        golem_swarm.pop()
    while len(ghost_swarm) > 0:
        ghost_swarm.pop()
    while len(game_framework.player.arrow_list) > 0:
        game_framework.player.arrow_list.pop()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            game_framework.player.attack(event)
        else:
            game_framework.player.handle_event(event)
    pass


def update():
    global golem_swarm, ghost_swarm, timer
    game_framework.player.update()
    for golem in golem_swarm:
        golem.update()
    for ghost in ghost_swarm:
        ghost.update()
    if timer == 0:
        if random.randint(0, 100) < 50:
            golem_swarm.insert(0, Golem())
        else:
            ghost_swarm.insert(0, Ghost())
        timer = 1000
    timer -= 100
    pass


def draw():
    global image, golem_swarm, ghost_swarm, map
    clear_canvas()
    map.draw()
    game_framework.player.draw()
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
