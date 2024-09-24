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

def run_rBottom():
    for x in range(20, 780, 5):
        printImages(x, 90)

def run_rRight():
    for y in range(90, 555, 5):
        printImages(780, y)

def run_rTop():
    for x in range(780, 20, -5):
        printImages(x, 555)

def run_rLeft():
    for y in range(555, 90, -5):
        printImages(20, y)

def run_rectangle():
    run_rBottom()
    run_rRight()
    run_rTop()
    run_rLeft()

def run_circle():
    r, cx, cy = 250, 800 // 2, 600 // 2 + 40    #   화면 크기의 반
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree - 90)    #   theta -> rad, -90 ~ 270
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        printImages(x, y)

while True:     #   뼈대 잡는 것이 제일 중요
    run_rectangle()
    #run_circle()
    break

close_canvas()
