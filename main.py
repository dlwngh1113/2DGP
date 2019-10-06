from pico2d import *

Width, Height = 550, 750
frame = 0
charWidth = 41
charHeight = 51
open_canvas(Width, Height)
main_page = load_image('main page.png')
character = load_image('archer.png')


# item_page = load_image('item page.png')

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
    pass


while True:
    clear_canvas()
    main_page.clip_draw(0, 0, Width, Height, Width / 2, Height / 2)
    character.clip_draw_to_origin(charWidth, charHeight * frame, charWidth, charHeight, 300, 300, charWidth * 1.5, charHeight * 1.5)
    frame = (frame + 1) % 5 + 2
    update_canvas()
    handle_events()
    delay(0.1)

close_canvas()
