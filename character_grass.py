from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

x = 0
y = 90

def run_rectangle():
    #clear_canvas_now()
    #boy.draw_now(x + 400, y + 255)
    #grass.draw_now(400, 30)
    #delay(0.1)
    pass

def run_circle():
    r, cx, cy = 250, 800 // 2, 600 // 2 + 40    #   화면 크기의 반
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree - 90)    #   theta -> rad
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        clear_canvas_now()
        boy.draw_now(x, y)
        grass.draw_now(400, 30)
        
        delay(0.01)

while True:     #   뼈대 잡는 것이 제일 중요
    run_rectangle()
    run_circle()

close_canvas()
