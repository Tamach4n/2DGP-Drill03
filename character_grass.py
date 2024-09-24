from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

x = 0
y = 90

def run_rectangle():
    clear_canvas_now()
    boy.draw_now(400, 90)
    grass.draw_now(400, 30)
    delay(0.1)

def run_circle():
    clear_canvas_now()
    boy.draw_now(400, 90)
    grass.draw_now(400, 30)
    delay(0.1)

while True: #   뼈대 잡는 것이 제일 중요
    run_rectangle()
    run_circle()
    break

close_canvas()
