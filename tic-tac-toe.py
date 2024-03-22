from turtle import *  # Importing all symbols from the 'turtle' module
from freegames import line  # Importing the 'line' function from the 'freegames' module

# Global variables:
a = 67
b = 200
occupied_cells = set() # Set to store the occupied cells

def grid():
    """Draw tic-tac-toe grid."""
    line(-a, b, -a, -b)  # Drawing vertical lines for the grid
    line(a, b, a, -b)
    line(-b, -a, b, -a)  # Drawing horizontal lines for the grid
    line(-b, a, b, a)


def drawx(x, y):
    """Draw X player."""
    center_x = x + a  # Calculating the center of the grid square for x-coordinate
    center_y = y + a  # Calculating the center of the grid square for y-coordinate
    color('blue') # Setting color to blue
    line(center_x - 40, center_y - 40, center_x + 40, center_y + 40)  # Drawing the first diagonal line for 'X'
    line(center_x - 40, center_y + 40, center_x + 40, center_y - 40)  # Drawing the second diagonal line for 'X'


def drawo(x, y):
    """Draw O player."""
    center_x = x + a  # Calculating the center of the grid square for x-coordinate
    center_y = y + a  # Calculating the center of the grid square for y-coordinate
    color('red') # Setting color to red
    up()
    goto(center_x, center_y - 40)  # Moving the pen to the center of the circle
    down()
    circle(40)  # Drawing the circle with a radius of 40


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + b) // (a * 2)) * (a * 2) - b  # Rounding down to the nearest grid position


state = {'player': 0}  # Dictionary to keep track of the current player
players = [drawx, drawo]  # List containing the draw functions for 'X' and 'O'


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)  # Rounding down the x-coordinate
    y = floor(y)  # Rounding down the y-coordinate
    player = state['player']  # Getting the current player
    draw = players[player]  # Getting the draw function for the current player

    if (x, y) in occupied_cells:
        return  # Don't make a move if the cell is already occupied

    draw(x, y)  # Drawing 'X' or 'O' at the tapped square
    update()  # Updating the screen display
    state['player'] = not player  # Changing the player for the next turn
    occupied_cells.add((x, y))  # Add the cell to the occupied set


setup(420, 420, 370, 0)  # Setting up the turtle window
hideturtle()  # Hiding the turtle
tracer(False)  # Turning off the screen updates
grid()  # Drawing the grid
update()  # Updating the screen display
onscreenclick(tap)  # Binding the 'tap' function to mouse clicks on the screen
done()  # Completing the drawing and releasing control of the turtle window
