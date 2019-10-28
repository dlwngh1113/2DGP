from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 300, 300
        self.dir = 0
        self.vel = 30
        self.charWidth = 41
        self.charHeight = 51
        self.xframe, self.yframe = 62.75, 55.3

    def draw(self):
        self.image.clip_draw_to_origin(self.charWidth * self.xframe, self.charHeight * self.yframe, self.charWidth,
                                       self.charHeight, self.x, self.y, self.charWidth * 1.5, self.charHeight * 1.5)

    def update(self):
        self.yframe = (self.yframe + 1) % 6


player = Player()