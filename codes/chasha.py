from pico2d import *
import random
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode


class Chasha:
    def __init__(self):
        self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\chasha.png')
        self.x, self.y = 250, 600
        self.velocity = 2
        self.charWidth = 33
        self.charHeight = 32
        self.drop_money = 2356
        self.atk = 50
        self.level = 4
        self.health = self.level * 500
        self.xframe, self.yframe = 0, 0
        self.event_que = []
        self.cur_state = Swerving
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self)

    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass


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
        pass

    @staticmethod
    def draw(monster):
        monster.image.clip_draw_to_origin(monster.charWidth * monster.xframe, monster.charHeight * (monster.yframe + 4),
                                          monster.charWidth,
                                          monster.charHeight, monster.x, monster.y, monster.charWidth * 1.5,
                                          monster.charHeight * 1.5)
