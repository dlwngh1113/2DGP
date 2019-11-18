import game_framework
from pico2d import *

def enter():
    global image, player, money_font
    money_font = Font('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\gothic.ttf')
    image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\main page.png')
    pass


def exit():
    global image, money_font
    del money_font
    del image
    pass


def handle_events():
    pass

def update():
    pass


def draw():
    clear_canvas()
    update_canvas()


def pause():
    pass


def resume():
    pass
