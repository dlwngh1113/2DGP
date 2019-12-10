from pico2d import *
import game_framework
import stage_state
import item_state

name = "StartState"
image = None
money_font = None
x, y = None, None
main_music = None


def enter():
    global image, money_font, main_music
    main_music = load_music('sound_resources\\main background sound.mp3')
    main_music.set_volume(80)
    main_music.repeat_play()
    money_font = Font('gothic.ttf')
    image = load_image('image_resources\\main page.png')
    pass


def exit():
    global image, money_font, main_music
    del money_font
    del image
    del main_music
    pass


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 165 < x < 380 and 140 < y < 220:
                game_framework.push_state(stage_state)
            elif 90 < x < 180 and 0 < y <70:
                game_framework.push_state(item_state)
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 750 - event.y + 1
    pass

def update():
    pass


def draw():
    global image, player, money_font
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2, game_framework.Height / 2)
    money_font.draw(325, 730, str(game_framework.player.money), (255, 255, 51))
    draw_rectangle(165, 140, 380, 220)
    draw_rectangle(90, 0, 180, 70)
    update_canvas()


def pause():
    pass


def resume():
    pass
