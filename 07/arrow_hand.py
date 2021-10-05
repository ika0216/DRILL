from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global p
    global q
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
a = KPU_WIDTH // 2
b = KPU_HEIGHT // 2
frame = 0
y = 100
p = random.randint(0, 1280)
q = random.randint(0, 1024)

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, y * 1, 100, 100, a, b)
    hand.draw(p, q)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    a += (p-a)/10
    b += (q-b)/10

    delay(0.01)

close_canvas()
