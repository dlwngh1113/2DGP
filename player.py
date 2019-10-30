from pico2d import *
import random
from arrow import Arrow

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


class Player:
    money = 0
    atk = 50
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 300, 300
        self.horizon_dir, self.vertic_dir = 0, 0
        self.velocity = 0
        self.charWidth = 55
        self.charHeight = 54
        self.xframe, self.yframe = 0, 0
        self.arrow_list = []
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)
        for arrow in self.arrow_list:
            arrow.draw()

    def update(self):
        self.cur_state.do(self)
        for arrow in self.arrow_list:
            arrow.update()
            if arrow.x > 550 or arrow.x < 0 or arrow.y > 750 or arrow.y < 0 or arrow.velocity >= 100:
                self.arrow_list.remove(arrow)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass

    def reinforce(self, cost):
        self.money -= cost
        if random.randint(0, 100) < 80:
            self.atk += int(self.atk ** 0.5)
        else:
            self.atk += int(self.atk ** 0.7) + 3

    def attack(self, event):
        self.arrow_list.insert(0, Arrow(event, self.x, self.y))
        pass


class VerticMove:
    @staticmethod
    def enter(player, event):
        if event == UPSIDE_DOWN:
            player.vertic_dir = 2
            player.velocity += 1
        elif event == DOWNSIDE_DOWN:
            player.vertic_dir = 2
            player.velocity -= 1
        elif event == UPSIDE_UP:
            player.vertic_dir -= 1
            player.velocity -= 1
        elif event == DOWNSIDE_UP:
            player.vertic_dir += 1
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.yframe = (player.yframe + 1) % 5
        player.y += player.velocity * player.vertic_dir * 10
        player.y = clamp(-25, player.y, 700)

    @staticmethod
    def draw(player):
        if player.vertic_dir * player.velocity > 0:
            player.image.clip_draw_to_origin(player.charWidth * 4, player.charHeight * (player.yframe + 4),
                                             player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)
        else:
            player.image.clip_draw_to_origin(0, player.charHeight * (player.yframe + 4), player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)


class HorizonMove:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.horizon_dir = 2
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.horizon_dir = 2
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.horizon_dir -= 1
            player.velocity -= 1
        elif event == LEFT_UP:
            player.horizon_dir += 1
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.yframe = (player.yframe + 1) % 5
        player.x += player.velocity * player.horizon_dir * 10
        player.x = clamp(-25, player.x, 500)

    @staticmethod
    def draw(player):
        if player.horizon_dir * player.velocity > 0:
            player.image.clip_draw_to_origin(player.charWidth * 6, player.charHeight * (player.yframe + 4),
                                             player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)
        else:
            player.image.clip_draw_to_origin(player.charWidth * 2, player.charHeight * (player.yframe + 4),
                                             player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)


class IdleState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.horizon_dir = 2
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.horizon_dir = 2
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.horizon_dir -= 1
            player.velocity -= 1
        elif event == LEFT_UP:
            player.horizon_dir += 1
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.yframe = (player.yframe + 1) % 5

    @staticmethod
    def draw(player):
        player.image.clip_draw_to_origin(player.charWidth * player.xframe, player.charHeight * (player.yframe + 4),
                                         player.charWidth,
                                         player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                         player.charHeight * 1.5)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, RIGHT_DOWN: HorizonMove,
                LEFT_UP: IdleState, LEFT_DOWN: HorizonMove,
                UPSIDE_UP: IdleState, UPSIDE_DOWN: HorizonMove,
                DOWNSIDE_UP: IdleState, DOWNSIDE_DOWN: HorizonMove},
    HorizonMove: {RIGHT_UP: IdleState, RIGHT_DOWN: HorizonMove,
                  LEFT_UP: IdleState, LEFT_DOWN: HorizonMove},
#    VerticMove: {UPSIDE_UP: IdleState, UPSIDE_DOWN: VerticMove,
#                 DOWNSIDE_UP: IdleState, DOWNSIDE_DOWN: VerticMove}
}
