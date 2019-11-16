from pico2d import *


class Arrow:
    image = None
    frame = None
    gradient = None

    def __init__(self, event, x, y):
        self.x = x
        self.y = y
        self.target_x = event.x
        self.target_y = 750 - event.y
        self.velocity = 0
        if self.target_y - self.y != 0:
            Arrow.gradient = (self.target_x - self.x) / (self.target_y - self.y)
        else:
            Arrow.gradient = 0.1
        if -1 < Arrow.gradient < 1:
            self.frame = 4
        else:
            self.frame = 2
        if self.image == None:
            self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\arrow_image.png')

    def draw(self):
        self.image.clip_draw(55 * self.frame, 0, 55, 48, self.x, self.y)
        draw_rectangle(*self.get_bb())
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

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_event(self):
        pass
