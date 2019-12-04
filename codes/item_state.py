from pico2d import *
import game_framework
import start_state

image = None
money_font = None
atk_font = None
cost_font = None
cost = None
x, y = 0, 0
reinforce_sound = None

def enter():
    global image, money_font, atk_font, cost_font, cost, reinforce_sound
    reinforce_sound = load_wav('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\sound_resources\\reinforce result.mp3')
    reinforce_sound.set_volume(40)
    money_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf')
    atk_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf', 40)
    cost_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf')
    cost = game_framework.player.atk * 10
    image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\item page.png')


def exit():
    global image, money_font, atk_font, cost_font, cost, reinforce_sound
    del money_font
    del atk_font
    del cost_font
    del cost
    del image
    del reinforce_sound

def draw():
    global image, money_font, atk_font, cost
    clear_canvas()
    image.clip_draw(0, 0, game_framework.Width, game_framework.Height, game_framework.Width / 2,
                    game_framework.Height / 2)
    money_font.draw(325, 725, str(game_framework.player.money), (255, 255, 51))
    atk_font.draw(250, 225, 'atk = ' + str(game_framework.player.atk), (255, 0, 0))
    cost_font.draw(325, 150, str(cost))
    draw_rectangle(240, 100, 430, 170)
    draw_rectangle(270, 0, 360, 70)
    update_canvas()


def update():
    global cost
    cost = game_framework.player.atk * 10
    pass


def handle_events():
    global x, y, reinforce_sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
            game_framework.player.money += 100000
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 750 - event.y - 1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            print(x, y)
            if 240 < x < 420 and 100 < y < 160:
                if game_framework.player.money > cost:
                    game_framework.player.reinforce(cost)
                    reinforce_sound.play()
            elif 270 < x < 360 and 0 < y < 70:
                game_framework.pop_state()



def pause():
    pass


def resume():
    pass
