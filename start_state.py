from pico2d import *
import game_framework
import item_

name = "StartState"
image = None


def enter():
    global image
    image = load_image('main page.png')
    pass


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_state(item_)
    pass

def update():
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    update_canvas()


def pause():
    pass


def resume():
    pass


class Player:
    def __init__(self):
        self.image = load_image('archer.png')
        self.x, self.y = 300, 300
        self.dir = 0
        self.vel = 30
        self.charWidth = 41
        self.charHeight = 51
        self.xframe, self.yframe = 0, 0

    def draw(self):
        self.image.clip_draw_to_origin(self.charWidth * self.xframe, self.charHeight * self.yframe, self.charWidth,
                                       self.charHeight, self.x, self.y, self.charWidth * 1.5, self.charHeight * 1.5)

    def update(self):
        self.yframe = (self.yframe + 1) % 6


#player = Player()