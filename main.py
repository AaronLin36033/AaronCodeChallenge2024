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
        next_button.show = False
        problem_button.show = False
        solution_button.show = False
    elif current_step == 1:
        devin.show = True
        abby.show = True
        start_button.show = False 
        next_button.show = True
        problem_button.show = False
        solution_button.show = False
        devin.message = "Hello, I am Devin. I am going to show you what a school in the future looks like."
    elif current_step == 2:
        devin.show = True
        abby.show = True
        next_button.show = False
        problem_button.show = True
        solution_button.show = False
        abby.message = "Have you noticed how much electricity the lights in this classroom use?"
    elif current_step == 3:
        devin.show = True
        abby.show = True
        next_button.show = False
        problem_button.show = False
        solution_button.show = True
        devin.message = "It's not great for the environment. But there are solutions!"
    elif current_step == 4:
        devin.show = True
        abby.show = True
        next_button.show = False
        problem_button.show = False
        solution_button.show = False
        abby.message = "Let's use natural light fiber and solar panels to reduce electricity usage."

def start_button_action():
    global current_step
    current_step = 1
    step_changed()

def next_button_action():
    global current_step
    current_step += 1
    step_changed()

def problem_button_action():
    global current_step
    current_step = 3
    step_changed()

def solution_button_action():
    global current_step
    current_step = 4
    step_changed()

start_button = Button("start", (WIDTH // 2, HEIGHT // 2), start_button_action)
start_button.scale = 0.5
buttons.append(start_button)

next_button = Button("next", (WIDTH // 2 + 100, HEIGHT // 2 + 200), next_button_action)
next_button.scale = 0.5
buttons.append(next_button)

problem_button = Button("problem", (WIDTH // 2 - 200, HEIGHT // 2 + 200), problem_button_action)
problem_button.scale = 0.2
buttons.append(problem_button)

solution_button = Button("solution", (WIDTH // 2 + 200, HEIGHT // 2 + 200), solution_button_action)
solution_button.scale = 0.2
buttons.append(solution_button)

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
