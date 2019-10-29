from pico2d import *
import random
import start_state

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UPSIDE_DOWN, UPSIDE_UP, DOWNSIDE_DOWN, DOWNSIDE_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_w): UPSIDE_DOWN,
    (SDL_KEYDOWN, SDLK_s): DOWNSIDE_DOWN,
    (SDL_KEYUP, SDLK_w): UPSIDE_UP,
    (SDL_KEYUP, SDLK_s): DOWNSIDE_UP
}


class Monster:
    def __init__(self):
        self.image = load_image('mob1.png')
        self.x, self.y = random.randint(0, 500), random.randint(0, 700)
        self.horizon_dir, self.vertic_dir = 0, 0
        self.velocity = 2
        self.charWidth = 33
        self.charHeight = 32
        self.money = 30
        self.atk = 50
        self.xframe, self.yframe = 0, 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self)

    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass


class VerticMove:
    pass


class HorizonMove:
    pass


class IdleState:
    @staticmethod
    def enter(monster, event):
        pass

    @staticmethod
    def exit(monster, event):
        del(monster)
        pass

    @staticmethod
    def do(monster):
        monster.xframe = (monster.xframe + 1) % 3
        if monster.x < start_state.player.x:
            monster.x += monster.velocity
        else:
            monster.x -= monster.velocity
        if monster.y < start_state.player.y:
            monster.y += monster.velocity
        else:
            monster.y -= monster.velocity

    @staticmethod
    def draw(monster):
        monster.image.clip_draw_to_origin(monster.charWidth * monster.xframe, monster.charHeight * (monster.yframe + 4),
                                          monster.charWidth,
                                          monster.charHeight, monster.x, monster.y, monster.charWidth * 1.5,
                                          monster.charHeight * 1.5)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, RIGHT_DOWN: HorizonMove,
                LEFT_UP: IdleState, LEFT_DOWN: HorizonMove,
                UPSIDE_UP: IdleState, UPSIDE_DOWN: VerticMove,
                DOWNSIDE_UP: IdleState, DOWNSIDE_DOWN: VerticMove}
}
