from pico2d import *


class Button:
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.width = widht
        self.height = height

    def draw(self):
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x, self.y, self.x + self.width, self.y + self.height
