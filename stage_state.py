from pico2d import *
import game_framework
import item_
import start_state

name = "StageState"
image = None


def enter():
    global image
    image = load_image('archer.png')
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
            game_framework.pop_state()
        else:
            start_state.player.handle_event(event)
    pass

def update():
    start_state.player.update()
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    start_state.player.draw()
    delay(0.05)
    update_canvas()


def pause():
    pass


def resume():
    pass