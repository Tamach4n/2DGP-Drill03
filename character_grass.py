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
    for y in range(90, 555, 5):
        printImages(780, y)

def run_rTop():
    for x in range(780, 20, -5):
        printImages(x, 555)

def run_rLeft():
    for y in range(555, 90, -5):
        printImages(20, y)
        

def tri_BC(s, e):
    for x in range(s, e, 2):
        printImages(x, 90)

def tri_AC():
    x, y = 700, 90
    #theta = math.radians(60.64)
    # mx = 2 * math.cos(theta)
    # my = 2 * math.sin(theta)
    
    dx, dy = -300, 400

    length = math.sqrt(300 ** 2 + 400 ** 2)

    mx = dx / length
    my = dy / length
    
    while x > 400:
        x += mx * 2
        y += my * 2
        printImages(x, y)

    print(x, y)

#def tri_AB():
    #while 

def run_rectangle():
    run_rBottom(400, 780)
    run_rRight()
    run_rTop()
    run_rLeft()
    run_rBottom(20, 400)

def run_circle():
    r, cx, cy = 250, 800 // 2, 600 // 2 + 40    #   화면 크기의 반
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree - 90)    #   degree -> rad, -90 ~ 270
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        printImages(x, y)

def run_triangle():
   # tri_BC(400, 700)
    tri_AC()
    #tri_AB()
    #tri_BC(100, 400)
    delay(5)

while True:     #   뼈대 잡는 것이 제일 중요
    #run_rectangle()
    #run_circle()
    run_triangle()
    break

close_canvas()
