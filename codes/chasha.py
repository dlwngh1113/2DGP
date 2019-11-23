from pico2d import *
import random
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Chasha:
    def __init__(self):
        self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\chasha.png')
        self.x, self.y = 250, 600
        self.charWidth = 33
        self.charHeight = 32
        self.drop_money = 2356
        self.atk = 50
        self.timer = 1.0
        self.speed = 0
        self.dir = random.random() * 2 * math.pi
        self.health = game_framework.player.atk ** 2 + game_framework.player.atk + game_framework.player.atk
        self.xframe, self.yframe = 0, 4
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.xframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 600 - 50)
        self.y = clamp(50, self.y, 700 - 50)

    def draw(self):
        self.image.clip_draw(self.xframe * self.charWidth, self.yframe * self.charHeight,
                             self.charWidth, self.charHeight, self.x, self.y)

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
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi
        clamp(25, self.x, 500)
        clamp(25, self.y, 700)
        return BehaviorTree.SUCCESS
        pass

    def get_bb(self):
        return self.x - self.charWidth, self.y - self.charHeight, self.x + self.charWidth, self.y + self.charHeight
