import pgzrun
from pgzhelper import *
from button import Button  
from sprite import Sprite

WIDTH = 800
HEIGHT = 600

sprites = []
buttons = []
current_step = 0


background = Actor("classroom", (400, 300))
background.scale = 0.6

devin = Sprite("devin", (700, 450))
devin.scale = 0.5 
sprites.append(devin)

abby = Sprite("abby", (100, 450))
abby.scale = 0.5 
sprites.append(abby)

def step_changed():
    if current_step == 0:
        devin.show = False
        abby.show = False
        start_button.show = True 
    if current_step == 1:
        devin.show = True
        abby.show = True
        start_button.show = False 
        devin.message = "Hello, I am Devin. I am going to show you what a school in the future looks like. "

def start_button_action():
    global current_step
    current_step = 1
    step_changed()

start_button = Button("start", (WIDTH // 2, HEIGHT // 2), start_button_action)
start_button.scale = 0.5
buttons.append(start_button)
 
def draw():
    screen.clear()
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

step_changed()
pgzrun.go()  
