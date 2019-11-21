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
        self.velocity = 1
        self.charWidth = 33
        self.charHeight = 32
        self.drop_money = 2356
        self.atk = 50
        self.timer = 1.0
        self.speed = 0
        self.level = 4
        self.health = self.level * 500
        self.xframe, self.yframe = 0, 0
        self.event_que = []
        self.cur_state = Swerving
        self.cur_state.enter(self, None)
        self.build_behavior_tree()

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self)

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
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

class Swerving:
    @staticmethod
    def enter(monster, event):
        pass

    @staticmethod
    def exit(monster, event):
        del monster
        pass

    @staticmethod
    def do(monster):
        if monster.level <= 1:
            del monster
        pass

    @staticmethod
    def draw(monster):
        monster.image.clip_draw_to_origin(monster.charWidth * monster.xframe, monster.charHeight * (monster.yframe + 4),
                                          monster.charWidth,
                                          monster.charHeight, monster.x, monster.y, monster.charWidth * 1.5,
                                          monster.charHeight * 1.5)
