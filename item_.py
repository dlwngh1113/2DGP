from pico2d import *
import game_framework
import start_state

image = None


def enter():
    global image
    image = load_image('item page.png')


def exit():
    global image
    del (image)


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    update_canvas()


def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()


def pause():
    pass


def resume():
    pass
