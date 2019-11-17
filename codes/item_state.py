from pico2d import *
import game_framework
import start_state
from button import Button

image = None
money_font = None
atk_font = None
cost_font = None
cost = None
reinforce_button = Button(250, 100, 180, 70)


def enter():
    global image, money_font, atk_font, cost_font, cost, reinforce_button
    money_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf')
    atk_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf', 40)
    cost_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf')
    cost = game_framework.player.atk * 10
    image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\item page.png')
    reinforce_button = Button(250, 100, 180, 70)


def exit():
    global image, money_font, atk_font, cost_font, cost, reinforce_button
    del money_font
    del atk_font
    del cost_font
    del cost
    del image
    del reinforce_button


def collide(button, event):
    left_a, bottom_a, right_a, top_a = button.get_bb()

    if left_a < event.x < right_a: return False
    if bottom_a < event.y < top_a: return False

    return True


def draw():
    global image, money_font, atk_font, cost
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2,
                    game_framework.Height / 2)
    money_font.draw(325, 725, str(game_framework.player.money), (255, 255, 51))
    atk_font.draw(250, 225, 'atk = ' + str(game_framework.player.atk), (255, 0, 0))
    cost_font.draw(325, 150, str(cost))
    reinforce_button.draw()
    update_canvas()


def update():
    global cost
    cost = game_framework.player.atk * 10
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
            game_framework.player.money += 100000
        elif collide(reinforce_button, event):
            if game_framework.player.money > cost:
                game_framework.player.reinforce(cost)


def pause():
    pass


def resume():
    pass
