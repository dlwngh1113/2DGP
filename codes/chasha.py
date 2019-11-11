from pico2d import *

class Chasha:
    def __init__(self):
        self.image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\golem image.png')
        self.x, self.y = random.randint(0, 500), random.randint(0, 700)
        self.horizon_dir, self.vertic_dir = 0, 0
        self.velocity = 2
        self.charWidth = 33
        self.charHeight = 32
        self.drop_money = 30
        self.atk = 50
        self.health = 1000
        self.xframe, self.yframe = 0, 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self)

    def add_event(self, event):
        pass

    def handle_event(self, event):
        pass