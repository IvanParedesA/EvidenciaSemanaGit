from turtle import setup, clear, goto, down, up, shape, stamp
from turtle import tracer, update, ontimer, done, onscreenclick
from turtle import color, begin_fill, forward, left, end_fill
from turtle import addshape, hideturtle, write
from random import shuffle

from freegames import path

# Load the car image
car = path('car.gif')

# Create tiles for the game
tiles = list(range(32)) * 2

# Store and update the game state
state = {'mark': None}

# Store the and track the hidden tiles
hide = [True] * 64

# Tap counter variable
tap_counter = 0


# Creates and visually represents the laying board
# The board consists of white square withh black outline
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


# Function that changes x,y coordinates to index
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Function that performs a change in tiles to x,y coordinates
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Function registers tap events executed by user
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    # Add tap counter to the game and increase when tap
    global tap_counter
    tap_counter += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


# Function will show the hidden image and tiles
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    # Variable that determines all tiles as uncovered
    uncovered_tiles = True

    for count in range(64):
        if hide[count]:
            uncovered_tiles = False
            x, y = xy(count)
            square(x, y)

    # Creating the text on screen
    up()
    goto(-190, 180)
    color('green')
    write(f'Taps: {tap_counter}', font=('Arial', 16, 'normal'))

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    if uncovered_tiles:
        up()
        goto(0, 0)
        color('green')
        write("Congratulations!", align='center', font=('Arial', 35, 'normal'))
    ontimer(draw, 100)


# Calling out every function previously declared

# Shuffle tiles randmonly
shuffle(tiles)

# Using the imported library will setup the window
setup(420, 420, 370, 0)

# Add car image
addshape(car)

# Hides the turtle cursor
hideturtle()

# Turn off animation
tracer(False)

# Follows and analyses the clicks performed by the user
onscreenclick(tap)

# Draws the game
draw()

# Finishes the event
done()
