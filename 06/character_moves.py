
from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    # 사각형 운동
    x = 400
    y = 90
    while x < 784:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)
    while y < 556:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(782, y)
        y += 2
        delay(0.01)
    while x > 16:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 554)
        x -= 2
        delay(0.01)
    while y > 88:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(18, y)
        y -= 2
        delay(0.01)
    while x < 402:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)

    # 원 운동
    i = 270
    while i < 631:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + math.cos(math.pi * (i/180)) * 232, 322 + math.sin(math.pi * (i/180)) * 232)
        i += 2
        delay(0.01)

close_canvas()
