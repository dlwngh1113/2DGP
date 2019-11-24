from pico2d import *
import game_framework
import game_world
from golem import Golem
from ghost import Ghost
import random
from map import Map
import dead_state
import boss_stage
import start_state

name = "StageState"
monsters = []


def enter():
    game_framework.player.stage_init()
    game_world.add_object(Map('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\codes\\map1.txt'), 0)
    for i in range(10):
        if random.randint(0, 100) < 50:
            monsters.append(Golem())
        else:
            monsters.append(Ghost())
    game_world.add_objects(monsters, 1)
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
    global monsters
    while len(monsters) > 0:
        monsters.pop()
    game_world.clear()
    while len(game_framework.player.arrow_list) > 0:
        game_framework.player.arrow_list.pop()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(start_state)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            game_framework.player.attack(event)
        else:
            game_framework.player.handle_event(event)
    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    game_framework.player.update()
    for monster in monsters:
        for arrow in game_framework.player.arrow_list:
            if collide(monster, arrow):
                game_framework.player.arrow_list.remove(arrow)
                monster.life -= game_framework.player.atk
                if monster.life <= 0:
                    monsters.remove(monster)
                    game_world.remove_object(monster)
                    game_framework.player.money += monster.money
                    print(game_framework.player.money)
    if not game_framework.player.Isinvincible:
        for monster in monsters:
            if collide(monster, game_framework.player):
                game_framework.player.invincible_time = get_time()
                game_framework.player.life -= monster.atk
                game_framework.player.Isinvincible = True
    if len(monsters) == 0:
        game_framework.change_state(boss_stage)
    if game_framework.player.life <= 0:
        game_framework.change_state(dead_state)
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    game_framework.player.draw()
    delay(0.05)
    update_canvas()


def pause():
    pass


def resume():
    pass
