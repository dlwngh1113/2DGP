from pico2d import *
import random
from arrow import Arrow
import game_framework

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

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Player:
    money = 1000
    atk = 157

    def __init__(self):
        self.image = load_image('image_resources\\character.png')
        self.shooting_sound = load_wav('sound_resources\\shooting sound.ogg')
        self.shooting_sound.set_volume(30)
        self.x, self.y = 300, 300
        self.life = 1000
        self.dir = 0
        self.vertic_vel = 0
        self.horizon_vel = 0
        self.Isinvincible = False
        self.charWidth = 55
        self.charHeight = 54
        self.invincible_time = 0.0
        self.font = load_font('gothic.ttf', 12)
        self.frame = 0
        self.arrow_list = []
        self.event_que = []
        self.cur_state = MovingState
        self.cur_state.enter(self, None)

    def stage_init(self):
        self.x, self.y = 250, 0
        self.life = 1000
        self.vertic_vel = 0
        self.horizon_vel = 0
        self.cur_state = MovingState

    def draw(self):
        self.cur_state.draw(self)
        for arrow in self.arrow_list:
            arrow.draw()
        self.font.draw(self.x + self.charWidth / 2, self.y + self.charHeight + 20, str(self.life), (255, 0, 0))

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        for arrow in self.arrow_list:
            arrow.update()
            if arrow.x > 550 or arrow.x < 0 or arrow.y > 750 or arrow.y < 0 or arrow.velocity >= 100:
                self.arrow_list.remove(arrow)
        if self.Isinvincible:
            if get_time() - self.invincible_time > 2.0:
                self.Isinvincible = False

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
        self.shooting_sound.play()
        self.arrow_list.insert(0, Arrow(event, self.x + self.charWidth / 2, self.y + self.charHeight / 2))
        pass

    def get_bb(self):
        return self.x, self.y + 10, self.x + self.charWidth, self.y + self.charHeight + 10


class MovingState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.horizon_vel += RUN_SPEED_PPS
            player.dir += 1
        elif event == RIGHT_UP:
            player.horizon_vel -= RUN_SPEED_PPS
            player.dir -= 1
        if event == LEFT_DOWN:
            player.horizon_vel -= RUN_SPEED_PPS
            player.dir -= 1
        elif event == LEFT_UP:
            player.horizon_vel += RUN_SPEED_PPS
            player.dir += 1

        if event == UPSIDE_DOWN:
            player.vertic_vel += RUN_SPEED_PPS
        elif event == UPSIDE_UP:
            player.vertic_vel -= RUN_SPEED_PPS
        if event == DOWNSIDE_DOWN:
            player.vertic_vel -= RUN_SPEED_PPS
        elif event == DOWNSIDE_UP:
            player.vertic_vel += RUN_SPEED_PPS

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        player.x += player.horizon_vel * game_framework.frame_time
        player.y += player.vertic_vel * game_framework.frame_time
        player.x = clamp(25, player.x, 480)
        player.y = clamp(25, player.y, 700)

    @staticmethod
    def draw(player):
        if player.vertic_vel > 0:
            player.image.clip_draw_to_origin(player.charWidth * 4,
                                             player.charHeight * (int(player.frame) + 4),
                                             player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)
            player.dir = 1
        elif player.vertic_vel < 0:
            player.image.clip_draw_to_origin(player.charWidth * 0,
                                             player.charHeight * (int(player.frame) + 4),
                                             player.charWidth,
                                             player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                             player.charHeight * 1.5)
            player.dir = -1
        else:
            # if boy vertic_vel == 0
            if player.horizon_vel > 0 or player.horizon_vel < 0:
                if player.horizon_vel > 0:
                    player.image.clip_draw_to_origin(player.charWidth * 6, player.charHeight * (int(player.frame) + 4),
                                                     player.charWidth,
                                                     player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                                     player.charHeight * 1.5)
                else:
                    player.image.clip_draw_to_origin(player.charWidth * 2, player.charHeight * (int(player.frame) + 4),
                                                     player.charWidth,
                                                     player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                                     player.charHeight * 1.5)
            else:
                # boy is idle
                player.image.clip_draw_to_origin(player.charWidth * 0,
                                                 player.charHeight * (int(player.frame) + 4),
                                                 player.charWidth,
                                                 player.charHeight, player.x, player.y, player.charWidth * 1.5,
                                                 player.charHeight * 1.5)


next_state_table = {
    MovingState: {RIGHT_UP: MovingState, RIGHT_DOWN: MovingState,
                  UPSIDE_UP: MovingState, UPSIDE_DOWN: MovingState,
                  LEFT_UP: MovingState, LEFT_DOWN: MovingState,
                  DOWNSIDE_UP: MovingState, DOWNSIDE_DOWN: MovingState}
}
