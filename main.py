from turtle import Screen
from xmlrpc.client import APPLICATION_ERROR
import pgzrun
from button import Button  

WIDTH = 800
HEIGHT = 600

sprites = []
buttons = []
current_step = 0


background = ("classroom.png")
sprite = ("devin.png", (WIDTH // 2, HEIGHT // 2))

def step_changed(step):
    global current_step
    current_step = step
    if step == 1:
        buttons.clear()  
        sprites.append()  

def start_button_action():
    step_changed(1)

start_button = Button("start_up.png", (WIDTH // 2, HEIGHT // 2), start_button_action)
buttons.append(start_button)

def draw():
    Screen.clear()
    background.draw()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()

def update():
    pass

def on_mouse_down(pos):
    for b in buttons:
        b.on_mouse_down(pos)

def on_mouse_up(pos):
    for b in buttons:
        b.on_mouse_up(pos)

pgzrun.go()  
