import os
import webbrowser
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
link_buttons = []
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

title = Sprite("program_title", (400, 100))
title.scale = 0.3
sprites.append(title)

info_title = Sprite("info_title", (200, 50))
info_title.scale = 0.3
sprites.append(info_title)

info_detail = Sprite("more_info_detail", (400, 350))
sprites.append(info_detail)

def step_changed():
    story_button.show = False
    info_button.show = False
    next_button.show = False
    problem_button.show = False
    solution_button.show = False
    roofbutton.show = False
    vrbutton.show = False
    computerbutton.show = False
    whiteboardbutton.show = False
    title.show = current_step == 0
    info_title.show = current_step == 70
    info_detail.show = current_step == 70
    link1button.show = current_step == 70
    link2button.show = current_step == 70
    link3button.show = current_step == 70

    if music.is_playing:
        music.stop()
    if current_step == 0:
        devin.show = False
        abby.show = False
        start_button.show = True
    elif current_step == 1:
        background.image="classroom"
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
        devin.message = ""
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
        devin.message = ""
        clock.schedule(next_button_action, 5)
    elif current_step == 12:
        devin.message = "It's not great for the environment. But there are solutions!"
        music.play_once("notgreatforenviroment")
        abby.message = ""
        clock.schedule(next_button_action, 4)
    elif current_step == 13:
        abby.message = "What do you think?"
        music.play_once("whatdoyouthink")
        clock.schedule(next_button_action, 2)
        devin.message = ""
    elif current_step == 14:
        abby.message = "Let's use natural light fiber and solar panels to reduce electricity usage."
        music.play_once("naturallight")
        devin.message = ""
        light.show = True
        # TODO: Show the light fiber picture
        clock.schedule(goto_classroom_buttons, 6)
    elif current_step == 21:
        vrbutton.image="vr_hover"
        vrbutton.show = True
        devin.message = "Not all students can experience field trips, and physical trips can be costly."
        music.play_once("fieldtrips")
        abby.message = ""
        clock.schedule(next_button_action, 6)
    elif current_step == 22:
        devin.message = ""
        abby.message = "VR headsets allow virtual field trips, making immersive experiences accessible to all students."
        music.play_once("vrheadset")
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
        music.play_once("waitfuture")
        clock.schedule(next_button_action, 5)
    elif current_step == 51:
        devin.message = "Actually, these technologies are available these days."
        abby.message = ""
        music.play_once("availablethesedays")
        clock.schedule(next_button_action, 4)
    elif current_step == 52:
        devin.message = "Please return to the Menu screen and check out more from the information button."
        music.play_once("returnmenu")
        clock.schedule(goto_Menu_buttons, 6)
    elif current_step == 60:
        background.image = "menu"
        abby.message = ""
        devin.message = ""
        info_button.show = True
        story_button.show = True
    elif current_step == 70:
        background.image = "info_bg" # more info page
        abby.message = ""
        devin.message = ""


def start_button_action():
    global current_step
    current_step = 70
    step_changed()
    start_button.show = False


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

def click_link1():
    print("clicked link 1")
    pass
    #webbrowser.open('https://www.viewsonic.com/library/education/what-is-an-interactive-whiteboard-5-features-you-need-to-know/')

def click_link2():
    print("clicked link 2")
    pass
    #webbrowser.open('https://edtechmagazine.com/higher/article/2023/01/future-computing-and-its-impact-higher-education')

def click_link3():
    print("clicked link 3")
    pass
    #webbrowser.open('https://edtechmagazine.com/k12/article/2023/05/how-virtual-reality-helping-kids-learn')

def check_classroom_buttons():
    global current_step
    if len(clicked_classroom_buttons) == 4:
        current_step = 50
        step_changed()


def goto_classroom_buttons():
    global current_step
    current_step = 10
    step_changed()


def goto_Menu_buttons():
    global current_step
    current_step = 60
    step_changed()

def goto_story_action():
    global current_step
    current_step = 1
    step_changed()

def goto_info_action():
    global current_step
    current_step = 70
    step_changed()


# Buttons setup
start_button = Button("start", (WIDTH // 2, HEIGHT // 2), start_button_action)
start_button.scale = 0.5
buttons.append(start_button)

next_button = Button("next", (WIDTH // 2 + 100, HEIGHT //
                     2 + 200), next_button_action)
next_button.scale = 0.5
buttons.append(next_button)

problem_button = Button(
    "problem", (WIDTH // 2 - 200, HEIGHT // 2 + 200), problem_button_action)
problem_button.scale = 0.2
buttons.append(problem_button)

solution_button = Button(
    "solution", (WIDTH // 2 + 200, HEIGHT // 2 + 200), solution_button_action)
solution_button.scale = 0.2
buttons.append(solution_button)

story_button = Button("storybutton", pos=(400, 200), callback=goto_story_action, show=False)
story_button.scale=0.3
buttons.append(story_button)

info_button = Button("information", pos=(400, 400), callback=goto_info_action,  show=False)
info_button.scale=0.3
buttons.append(info_button)

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

link1button = Actor("link1", (400, 242))
link1button.imagename = "link1"
link1button.scale = 0.46
link1button.action = click_link1
link_buttons.append(link1button)

link2button = Actor("link2", (400, 364))
link2button.imagename = "link2"
link2button.scale = 0.46
link2button.action = click_link2
link_buttons.append(link2button)

link3button = Actor("link3", (400, 479))
link3button.imagename = "link3"
link3button.scale = 0.46
link3button.action = click_link3
link_buttons.append(link3button)

def draw():
    screen.clear()
    background.draw()
    for h in hover_buttons:
        if h.show :
            h.draw()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()
    for b in link_buttons:
        if b.show:
            b.draw()
    # draw step on screen
    screen.draw.text("step: "+str(current_step), (680, 10),
                     color=(0, 0, 0), fontsize=32)


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
    for l in link_buttons:
        if l.show:
            if l.get_rect().collidepoint(pos):
                l.action()


def on_mouse_move(pos):
    for h in hover_buttons:
        if h.show:
            if h.get_rect().collidepoint(pos):
                h.image = h.imagename + "_hover"
            else:
                h.image = h.imagename
    for l in link_buttons:
        if l.show:
            if l.get_rect().collidepoint(pos):
                l.image = l.imagename + "_hover"
            else:
                l.image = l.imagename


step_changed()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()
