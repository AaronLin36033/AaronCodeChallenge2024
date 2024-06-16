import pgzrun

WIDTH = 800
HEIGHT = 600

sprites = []
buttons = []
#Add your code below

background = Actor("classroom.png")

def draw():
    screen.clear()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()
    # elements need to be draw here

def update():
    # any global variable need to be updated need specify global
    pass

def on_mouse_down(pos):
    for b in buttons:
        b.on_mouse_down(pos)

def on_mouse_up(pos):
    for b in buttons:
        b.on_mouse_up(pos)

pgzrun.go() # Must be last line