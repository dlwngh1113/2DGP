from pico2d import *
import game_framework
import start_state

image = None
money_font = None
atk_font = None
cost_font = None
cost = None


def enter():
    global image, money_font, atk_font, cost_font, cost
    money_font = Font('gothic.ttf')
    atk_font = Font('gothic.ttf', 40)
    cost_font = Font('gothic.ttf')
    cost = game_framework.player.atk * 10
    image = load_image('item page.png')


def exit():
    global image, money_font, atk_font, cost_font, cost
    del money_font
    del atk_font
    del cost_font
    del cost
    del image


def draw():
    global image, money_font, atk_font, cost
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    money_font.draw(325, 725, str(game_framework.player.money), (255, 255, 51))
    atk_font.draw(250, 225, 'atk = ' + str(game_framework.player.atk), (255, 0, 0))
    cost_font.draw(325, 150, str(cost))
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_t:
            if game_framework.player.money > cost:
                game_framework.player.reinforce(cost)


def pause():
    pass


def resume():
    pass
