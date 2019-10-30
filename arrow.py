from pico2d import *


class Arrow:
    image = None

    def __init__(self, event, x, y):
        self.x = x
        self.y = y
        self.target_x = event.x
        self.target_y = 750 - event.y
        self.velocity = 0
        if self.image == None:
            self.image = load_image('arrow_image.png')

    def draw(self):
        self.image.clip_draw(110, 0, 55, 48, self.x, self.y)
        pass

    def update(self):
        if self.velocity < 100:
            t = self.velocity / 100
            x = (1 - t) * self.x + t * self.target_x
            y = (1 - t) * self.y + t * self.target_y
            self.x = x
            self.y = y
            self.velocity += 2
        pass

    def handle_event(self):
        pass
