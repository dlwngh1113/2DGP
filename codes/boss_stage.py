import game_framework
from pico2d import *
import game_world
import start_state
import dead_state

from chasha import Chasha
from map import Map


boss = []

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global boss
    boss.append(Chasha(3))
    game_world.add_object(Map('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\codes\\map1.txt'), 0)
    pass


def exit():
    global boss
    while len(boss) > 0:
        boss.pop()
    while len(game_framework.player.arrow_list):
        game_framework.player.arrow_list.pop()
    game_world.clear()
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
    global boss
    for game_object in game_world.all_objects():
        game_object.update()
    for bosses in boss:
        bosses.update()
        if not game_framework.player.Isinvincible:
            if collide(bosses, game_framework.player):
                game_framework.player.life -= bosses.atk
                game_framework.player.invincible_time = get_time()
                game_framework.player.Isinvincible = True
        for arrow in game_framework.player.arrow_list:
            if collide(arrow, bosses):
                bosses.life -= game_framework.player.atk
                game_framework.player.arrow_list.remove(arrow)
                if bosses.life <= 0:
                    if bosses.level > 1:
                        boss.append(Chasha(bosses.level - 1, bosses.x, bosses.y))
                        boss.append(Chasha(bosses.level - 1, bosses.x, bosses.y))
                        game_framework.player.money += bosses.money
                        print(game_framework.player.money)
                        boss.remove(bosses)
                    else:
                        game_framework.player.money += bosses.money
                        print(game_framework.player.money)
                        boss.remove(bosses)
    if len(boss) <= 0:
        game_framework.change_state(start_state)
    if game_framework.player.life <= 0:
        game_framework.change_state(dead_state)
    game_framework.player.update()
    delay(0.05)
    pass


def draw():
    global boss
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    game_framework.player.draw()
    for bosses in boss:
        draw_rectangle(*bosses.get_bb())
        bosses.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass
