from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

def printImages(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.01)

def run_rBottom(s, e):
    for x in range(s, e, 5):
        printImages(x, 90)

def run_rRight():
    for y in range(90, 460, 5):
        printImages(680, y)

def run_rTop():
    for x in range(680, 120, -5):
        printImages(x, 460)

def run_rLeft():
    for y in range(460, 90, -5):
        printImages(120, y)
        

def tri_BC(s, e):
    for x in range(s, e, 4):
        printImages(x, 90)

def tri_AC():
    x, y = 700, 90      # 좌표 일일이 선언하기 불편
    dx, dy = -300, 400

    length = math.sqrt(dx ** 2 + dy ** 2)

    mx = dx / length
    my = dy / length
    
    while x > 400:
        x += mx * 4
        y += my * 4
        printImages(x, y)

def tri_AB():
    x, y = 400, 490
    dx, dy = -300, -400

    length = math.sqrt(dx ** 2 + dy ** 2)

    mx, my = dx / length, dy / length

    while x > 101:
        x += 4 * mx
        y += 4 * my
        printImages(x, y)

def run_rectangle():
    run_rBottom(400, 680)
    run_rRight()
    run_rTop()
    run_rLeft()
    run_rBottom(120, 400)

def run_circle():
    r, cx, cy = 200, 800 // 2, 600 // 2 - 13    #   화면 크기의 반
    
    for degree in range(0, 360, 1):
        theta = math.radians(degree - 90)    #   degree -> rad, -90 ~ 270
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        printImages(x, y)

def run_triangle():
    tri_BC(400, 700)
    tri_AC()
    tri_AB()
    tri_BC(100, 400)

while True:     #   뼈대 잡는 것이 제일 중요
    run_rectangle()
    run_circle()
    run_triangle()

close_canvas()
