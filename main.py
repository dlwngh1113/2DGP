from lib2to3.fixer_util import p1

from pico2d import *

Width, Height = 550, 750
frame = 0
charWidth = 41
charHeight = 51
open_canvas(Width, Height)
main_page = load_image('main page.png')


class player:
    image = load_image('archer.png')
    x, y = 300, 300
    dir = 0
    vel = 30

    def move(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                close_canvas()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    player.dir -= 1
                    player.x += player.dir * player.vel
                elif event.key == SDLK_RIGHT:
                    player.dir += 1
                    player.x += player.dir * player.vel
                elif event.key == SDLK_UP:
                    player.y += player.vel
                elif event.key == SDLK_DOWN:
                    player.y -= player.vel
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    player.dir -= 1
                elif event.key == SDLK_LEFT:
                    player.dir += 1


# item_page = load_image('item page.png')
p1 = player()

while True:
    clear_canvas()
    main_page.clip_draw(0, 0, Width, Height, Width / 2, Height / 2)
    p1.image.clip_draw_to_origin(charWidth * 4, charHeight * frame, charWidth, charHeight, p1.x, p1.y, charWidth * 1.5,
                                  charHeight * 1.5)
    p1.move()
    frame = (frame + 1) % 5 + 2
    update_canvas()
    delay(0.1)

close_canvas()
