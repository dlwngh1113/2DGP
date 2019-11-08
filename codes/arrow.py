from pico2d import *


class Arrow:
    image = None
    frame = None

    def __init__(self, event, x, y):
        self.x = x
        self.y = y
        self.target_x = event.x
        self.target_y = 750 - event.y
        self.velocity = 0
        self.gradient = (self.target_x - self.x) / (self.target_y - self.y)
        if -1 < self.gradient < 1:
            self.frame = 4
        else:
            self.frame = 2
        if self.image == None:
            self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\arrow_image.png')

    def draw(self):
        self.image.clip_draw(55 * self.frame, 0, 55, 48, self.x, self.y)
        pass

    def update(self):
        if self.velocity < 100:
            t = self.velocity / 100
            x = (1 - t) * self.x + t * self.target_x
            y = (1 - t) * self.y + t * self.target_y
            self.x = x
            self.y = y
            self.velocity += 10
        pass

    def handle_event(self):
        pass
