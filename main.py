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
    if music.is_playing:
        music.stop()
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
        music.play_once("iamdevin")
    elif current_step == 2:
        devin.show = True
        abby.show = True
        next_button.show = True
        abby.message = "That's great, let's see what is different between now and the future in the classroom."
        music.play_once("seethefuture")
        devin.message=""
    elif current_step == 3:
        devin.show = True
        abby.show = True
        next_button.show = True
        devin.message = "Please click the area in the classroom you think is different and find out more details."
        music.play_once("clickthearea")
        abby.message = ""
    elif current_step == 4:
        devin.show = True
        abby.show = True
        next_button.show = False
        problem_button.show = False
        solution_button.show = False
        abby.message = "Let's use natural light fiber and solar panels to reduce electricity usage."
        music.play_once("naturallight")
    elif current_step == 10:
        roofbutton.show = True
        vrbutton.show = True
        computerbutton.show = True
        whiteboardbutton.show = True
    elif current_step == 11:
        abby.message = "Have you noticed how much electricity the lights in this classroom use?"
        music.play_once("howmuchelectricity")
        devin.message=""
    elif current_step == 12:
        devin.message="It's not great for the environment. But there are solutions!"
        music.play_once("notgreatforenviroment")
        abby.message=""
    elif current_step == 13:
        abby.message="What do you think?"
        music.play_once("whatdoyouthink")
        devin.message=""
    elif current_step == 14:
        abby.message="Let's use natural light fiber and solar panels to reduce electricity usage."
        music.play_once("naturallight")
        devin.message=""
        # TODO: Show the light fiber picture
    elif current_step == 21:
        devin.message = "Not all students can experience field trips, and physical trips can be costly."
        music.play_once("")
        abby.message = ""
    elif current_step == 22:
        devin.message = ""
        abby.message = "VR headsets allow virtual field trips, making immersive experiences accessible to all students."
        music.play_once("fieldtrips")
    elif current_step == 23:
        devin.message = ""
        abby.message = ""
    elif current_step == 31:
        devin.message = "Outdated computers can hinder learning and consume a lot of power."
        music.play_once("outdatedcomputers")
        abby.message = ""
    elif current_step == 32:
        devin.message = ""
        abby.message = "Using energy-efficient, modern computers can enhance learning and reduce electricity consumption."
        music.play_once("energyconsumption")
    elif current_step == 33:
        devin.message = ""
        abby.message = ""
    elif current_step == 41:
        devin.message = "Whiteboard: Not all students can see the board properly, and markers are unhealthy."
        music.play_once("whiteboardunhealthy")
        abby.message = ""
    elif current_step == 42:
        devin.message = ""
        abby.message = "Digital whiteboards can be more accessible and eco-friendly, and they allow notes to be saved and shared easily."
        music.play_once("moreaccessable")
    elif current_step == 43:
        devin.message = ""
        abby.message = ""

def start_button_action():
    global current_step
    current_step = 1
    step_changed()

def next_button_action():
    global current_step
    if current_step in [3, 14, 23, 33, 43]:
        current_step = 10
    else:
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
    global current_step
    current_step = 11
    step_changed()

def vrbutton_action():
    global current_step
    current_step = 21
    step_changed()

def computerbutton_action():
    global current_step
    current_step = 31
    step_changed()

def whiteboardbutton_action():
    global current_step
    current_step = 41
    step_changed()

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
roofbutton.action = roofbutton_action
hover_buttons.append(roofbutton)

vrbutton = Actor("vr", (116, 390))
vrbutton.imagename = "vr"
vrbutton.action = vrbutton_action
hover_buttons.append(vrbutton)

computerbutton = Actor("computer", (254, 329))
computerbutton.imagename = "computer"
computerbutton.action = computerbutton_action
hover_buttons.append(computerbutton)

whiteboardbutton = Actor("whiteboard", (340, 225))
whiteboardbutton.imagename = "whiteboard"
whiteboardbutton.action = whiteboardbutton_action
hover_buttons.append(whiteboardbutton)

def draw():
    screen.clear()
    background.draw()
    for h in hover_buttons:
        h.draw()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()

def update():
    pass

def on_mouse_down(pos):
    for b in buttons:
        b.on_mouse_down(pos)
    for h in hover_buttons:
        if h.show:
            if h.get_rect().collidepoint(pos):
                h.action()

def on_mouse_up(pos):
    for b in buttons:
        b.on_mouse_up(pos)

def on_mouse_move(pos):
    for h in hover_buttons:
        if h.show:
            if h.get_rect().collidepoint(pos):
                h.image = h.imagename + "_hover"
            else:
                h.image = h.imagename

step_changed()
pgzrun.go()