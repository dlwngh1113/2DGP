from pico2d import *
import math

WIDTH, HEIGHT = 550, 750
open_canvas(WIDTH, HEIGHT)
map_list = []
SIZE = 50
select_num = 1
tile_image = load_image('image_resources\\tile_sheet.png')



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
    global SIZE, map_list, WIDTH, HEIGHT, select_num
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            map_list[event.y // SIZE][event.x // SIZE] = select_num
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            select_num = (select_num + 1) % 15
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if(select_num > 1):
                select_num -= 1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            map_list[event.y // SIZE][event.x // SIZE] = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            save()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            print_ary()
        elif event.type == SDL_MOUSEMOTION:
            tile_image.clip_draw(0, select_num * 32, 32, 32, event.x, HEIGHT - event.y)
    pass


def draw():
    global map_list, tile_image, SIZE, HEIGHT
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] != 0:
                tile_image.clip_draw(0, map_list[i][j] * 32, 32, 32, (j + 0.5) * SIZE, (len(map_list) - i) * SIZE - SIZE // 2, SIZE, SIZE)
    pass


def init():
    global map_list
    for i in range(15):
        line = []
        for j in range(11):
            line.append(0)
        map_list.append(line)
    pass


hide_cursor()
init()
while True:
    clear_canvas()
    draw()
    handle_events()
    update_canvas()