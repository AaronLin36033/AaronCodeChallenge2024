import pgzrun
from pgzhelper import *
from button import Button  
from sprite import Sprite
from pgzero import clock, music

WIDTH = 800
HEIGHT = 600

sprites = []
buttons = []
hover_buttons = []
current_step = 0
clicked_classroom_buttons = set()

background = Actor("classroom", (400, 300))

devin = Sprite("devin", (700, 450))
devin.scale = 0.5 
sprites.append(devin)

abby = Sprite("abby", (100, 450))
abby.scale = 0.5 
sprites.append(abby)

light = Sprite("lighting", (400, 450))
light.scale = 0.5
light.show = False
sprites.append(light)

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
        next_button.show = False
        devin.message = "Please click the area in the classroom you think is different and find out more details."
        music.play_once("clickthearea")
        abby.message = ""
        clock.schedule(goto_classroom_buttons, 6)
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
        next_button.show = False
        light.show = False
        abby.message = ""
        devin.message = ""
        check_classroom_buttons()
    elif current_step == 11:
        abby.message = "Have you noticed how much electricity the lights in this classroom use?"
        music.play_once("howmuchelectricity")
        devin.message=""
        clock.schedule(next_button_action, 5)
    elif current_step == 12:
        devin.message="It's not great for the environment. But there are solutions!"
        music.play_once("notgreatforenviroment")
        abby.message=""
        clock.schedule(next_button_action, 4)
    elif current_step == 13:
        abby.message="What do you think?"
        music.play_once("whatdoyouthink")
        clock.schedule(next_button_action, 2)
        devin.message=""
    elif current_step == 14:
        abby.message="Let's use natural light fiber and solar panels to reduce electricity usage."
        music.play_once("naturallight")
        devin.message=""
        light.show=True
        # TODO: Show the light fiber picture
        clock.schedule(goto_classroom_buttons, 6)
    elif current_step == 21:
        devin.message = "Not all students can experience field trips, and physical trips can be costly."
        music.play_once("fieldtrips")
        abby.message = ""
        clock.schedule(next_button_action, 6)
    elif current_step == 22:
        devin.message = ""
        abby.message = "VR headsets allow virtual field trips, making immersive experiences accessible to all students."
        #music.play_once("") # TODO: add voice for this.
        clock.schedule(goto_classroom_buttons, 7)
    elif current_step == 23:
        devin.message = ""
        abby.message = ""
    elif current_step == 31:
        devin.message = "Outdated computers can hinder learning and consume a lot of power."
        music.play_once("outdatedcomputers")
        abby.message = ""
        clock.schedule(next_button_action, 5)
    elif current_step == 32:
        devin.message = ""
        abby.message = "Using energy-efficient, modern computers can enhance learning and reduce electricity consumption."
        music.play_once("energyconsumption")
        clock.schedule(goto_classroom_buttons, 7)
    elif current_step == 33:
        devin.message = ""
        abby.message = ""
    elif current_step == 41:
        devin.message = "Whiteboard: Not all students can see the board properly, and markers are unhealthy."
        music.play_once("whiteboardunhealthy")
        clock.schedule(next_button_action, 5)
        abby.message = ""
    elif current_step == 42:
        devin.message = ""
        abby.message = "Digital whiteboards can be more accessible and eco-friendly, and they allow notes to be saved and shared easily."
        music.play_once("moreaccessable")
        clock.schedule(goto_classroom_buttons, 7)
    elif current_step == 43:
        devin.message = ""
        abby.message = ""
    elif current_step == 50:
        roofbutton.show = False
        vrbutton.show = False
        computerbutton.show = False
        whiteboardbutton.show = False
        devin.message = ""
        abby.message = "That's amazing, I can't wait for the future for those technologies."
        clock.schedule(next_button_action, 5)
    elif current_step == 51:
        devin.message = "Actually these technology are available in these days."
        abby.message = ""

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
    global current_step
    current_step = 11
    step_changed()
    clicked_classroom_buttons.add("roof")

def vrbutton_action():
    global current_step
    current_step = 21
    step_changed()
    clicked_classroom_buttons.add("vr")

def computerbutton_action():
    global current_step
    current_step = 31
    step_changed()
    clicked_classroom_buttons.add("computer")

def whiteboardbutton_action():
    global current_step
    current_step = 41
    step_changed()
    clicked_classroom_buttons.add("whiteboard")

def check_classroom_buttons():
    global current_step
    if len(clicked_classroom_buttons) == 4:
        current_step = 50
        step_changed()

def goto_classroom_buttons():
    global current_step
    current_step = 10
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
    #draw step on screen
    screen.draw.text("step: "+str(current_step), (680,10), color=(0, 0, 0), fontsize=32)

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