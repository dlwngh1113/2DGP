from pico2d import *

Width, Height = 550, 750
open_canvas(Width, Height)
main_page = load_image('main page.png')


class Player:
    def __init__(self):
        self.image = load_image('archer.png')
        self.x, self.y = 300, 300
        self.dir = 0
        self.vel = 30
        self.charWidth = 41
        self.charHeight = 51
        self.xframe, self.yframe = 0, 0

    def draw(self):
        self.image.clip_draw_to_origin(self.charWidth * self.xframe, self.charHeight * self.yframe, self.charWidth,
                                       self.charHeight, self.x, self.y, self.charWidth * 1.5, self.charHeight * 1.5)

    def update(self):
        self.yframe = (self.yframe + 1) % 6


player = Player()

while True:
    clear_canvas()
    main_page.clip_draw(0, 0, Width, Height, Width / 2, Height / 2)
    player.draw()

    player.update()
    update_canvas()
    delay(0.1)

close_canvas()
