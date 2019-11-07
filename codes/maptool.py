from pico2d import *
import math

WIDTH, HEIGHT = 550, 750
open_canvas(WIDTH, HEIGHT)
map_list = []
SIZE = 50
image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\tile_sheet.png')


def load():
    global map_list, HEIGHT, SIZE
    filename = 'map1.txt'
    with open(filename) as data:
        map_list = [[int(i) for i in line.split()] for line in data.readlines()]
    print_ary()
    pass


def load_stage(filename):
    with open(filename) as data:
        map_source = [[int(i) for i in line.split()] for line in data.readlines()]
    return map_source


def save():
    global map_list
    f = open('map1.txt', 'w')
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            f.write(str(map_list[i][j]))
            f.write(' ')
        f.write('\n')
    f.close()
    print('successfully saved!')
    pass


def print_ary():
    global map_list
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            print(map_list[i][j], end=' ')
        print()


def handle_events():
    global SIZE, map_list, WIDTH, HEIGHT
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            map_list[event.y // SIZE][event.x // SIZE] = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            save()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            print_ary()
    pass


def draw():
    pass


def init():
    global map_list
    for i in range(15):
        line = []
        for j in range(11):
            line.append(0)
        map_list.append(line)
    pass


init()
while True:
    handle_events()
