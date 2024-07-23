import pgzrun
from pgzhelper import *
from button import Button  
from sprite import Sprite

WIDTH = 800
HEIGHT = 600

sprites = []
buttons = []
hover_buttons = []
current_step = 0

background = Actor("classroom", (400, 300))

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
        roofbutton.show = False
        vrbutton.show = False
        computerbutton.show = False
        whiteboardbutton.show = False
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
    elif current_step == 10:
        roofbutton.show = True
        vrbutton.show = True
        computerbutton.show = True
        whiteboardbutton.show = True

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

def roofbutton_action():
    devin.message = "Roof: Traditional roofs don't use space efficiently and contribute to heat buildup."
    abby.message = "Solution: Green roofs can reduce heat and provide space for plants, improving insulation and energy efficiency."

def vrbutton_action():
    devin.message = "VR Headsets: Not all students can experience field trips, and physical trips can be costly."
    abby.message = "Solution: VR headsets allow virtual field trips, making immersive experiences accessible to all students."

def computerbutton_action():
    devin.message = "Computers: Outdated computers can hinder learning and consume a lot of power."
    abby.message = "Solution: Using energy-efficient, modern computers can enhance learning and reduce electricity consumption."

def whiteboardbutton_action():
    devin.message = "Whiteboard: Not all students can see the board properly, and markers are unhealthy."
    abby.message = "Solution: Digital whiteboards can be more accessible and eco-friendly, and they allow notes to be saved and shared easily."

# Buttons setup
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

# Hover buttons setup
roofbutton = Actor("roof", (400, 80))
roofbutton.imagename = "roof"
roofbutton_action = roofbutton_action
hover_buttons.append(roofbutton)

vrbutton = Actor("vr", (116, 390))
vrbutton.imagename = "vr"
vrbutton_action = vrbutton_action
hover_buttons.append(vrbutton)

computerbutton = Actor("computer", (254, 329))
computerbutton.imagename = "computer"
computerbutton_action = computerbutton_action
hover_buttons.append(computerbutton)

whiteboardbutton = Actor("whiteboard", (340, 225))
whiteboardbutton.imagename = "whiteboard"
whiteboardbutton_action = whiteboardbutton_action
hover_buttons.append(whiteboardbutton)

def draw():
    screen.clear()
    background.draw()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()
    for h in hover_buttons:
        h.draw()

def update():
    pass

def on_mouse_down(pos):
    for b in buttons:
        b.on_mouse_down(pos)
    for h in hover_buttons:
        if h.get_rect().collidepoint(pos):
            if h == roofbutton:
                roofbutton_action()
            elif h == vrbutton:
                vrbutton_action()
            elif h == computerbutton:
                computerbutton_action()
            elif h == whiteboardbutton:
                whiteboardbutton_action()

def on_mouse_up(pos):
    for b in buttons:
        b.on_mouse_up(pos)

def on_mouse_move(pos):
    for h in hover_buttons:
        if h.get_rect().collidepoint(pos):
            h.image = h.imagename + "_hover"
        else:
            h.image = h.imagename

step_changed()
pgzrun.go()
