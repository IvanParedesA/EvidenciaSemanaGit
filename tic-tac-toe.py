from turtle import *  # Importing all symbols from the 'turtle' module
from freegames import line  # Importing the 'line' function from the 'freegames' module


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)  # Drawing vertical lines for the grid
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)  # Drawing horizontal lines for the grid
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)  # Drawing the first diagonal line for 'X'
    line(x, y + 133, x + 133, y)  # Drawing the second diagonal line for 'X'


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)  # Moving the pen to the center of the circle
    down()
    circle(62)  # Drawing the circle with a radius of 62


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200  # Rounding down to the nearest grid position


state = {'player': 0}  # Dictionary to keep track of the current player
players = [drawx, drawo]  # List containing the draw functions for 'X' and 'O'


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)  # Rounding down the x-coordinate
    y = floor(y)  # Rounding down the y-coordinate
    player = state['player']  # Getting the current player
    draw = players[player]  # Getting the draw function for the current player
    draw(x, y)  # Drawing 'X' or 'O' at the tapped square
    update()  # Updating the screen display
    state['player'] = not player  # Changing the player for the next turn


setup(420, 420, 370, 0)  # Setting up the turtle window
hideturtle()  # Hiding the turtle
tracer(False)  # Turning off the screen updates
grid()  # Drawing the grid
update()  # Updating the screen display
onscreenclick(tap)  # Binding the 'tap' function to mouse clicks on the screen
done()  # Completing the drawing and releasing control of the turtle window
