from pico2d import *

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


class RunState:
    pass

class IdleState:
    pass

class Player:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 300, 300
        self.dir = 0
        self.vel = 30
        self.charWidth = 55
        self.charHeight = 54
        self.xframe, self.yframe = 0, 0
        self.event_que = []
        #self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        #self.image.clip_draw_to_origin(self.charWidth * self.xframe, self.charHeight * self.yframe, self.charWidth,
        #                               self.charHeight, self.x, self.y, self.charWidth * 1.5, self.charHeight * 1.5)
        self.cur_state.draw(self)
        delay(0.01)

    def update(self):
        #self.yframe = (self.yframe + 1) % 5 + 3
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UPSIDE_UP: RunState, UPSIDE_DOWN: RunState,
                DOWNSIDE_DOWN: RunState, DOWNSIDE_UP: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState,
               UPSIDE_UP: IdleState, UPSIDE_DOWN: IdleState,
               DOWNSIDE_DOWN: IdleState, DOWNSIDE_UP: IdleState}
}