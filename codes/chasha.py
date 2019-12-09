from pico2d import *
import random
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 25.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Chasha:
    image = None
    def __init__(self, level=None, x=None, y=None):
        if self.image is None:
            self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\chasha.png')
        self.font = load_font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf', 12)
        if x is None and y is None:
            x, y = 250, 600
        self.x, self.y = x, y
        if level is None:
            level = 3
        self.level = level
        self.charWidth = self.level * 33
        self.charHeight = self.level * 32
        self.money = self.level * 1087
        self.atk = level * 43
        self.timer = 1.0
        self.speed = 0
        self.dir = random.random() * 2 * math.pi
        self.life = self.level * int(game_framework.player.atk * 5.5)
        self.frame = 0
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(33, self.x, 500 - 33)
        self.y = clamp(32, self.y, 800 - 64)

    def draw(self):
        if 0 < self.dir < math.pi:
            self.image.clip_draw(int(self.frame) * 33, 0,
                                 33, 32, self.x, self.y, self.charWidth, self.charHeight)
        else:
            self.image.clip_draw(int(self.frame) * 33, 4 * 32,
                                 33, 32, self.x, self.y, self.charWidth, self.charHeight)
        self.font.draw(self.x + self.charWidth / 2, self.y + self.charHeight / 2, str(self.life), (255,0,0))

    def update(self):
        self.bt.run()
        pass

    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("WanderNode", self.wander)
        self.bt = BehaviorTree(wander_node)
        pass

    def wander(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time / 2
        if self.timer < 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi
        self.x = clamp(33, self.x, 500 - 33)
        self.y = clamp(32, self.y, 800 - 64)
        return BehaviorTree.SUCCESS
        pass

    def get_bb(self):
        return self.x - self.charWidth / 2, self.y - self.charHeight / 2, self.x + self.charWidth / 2 - 10, self.y + self.charHeight / 2
