import turtle
from freegames import line

# Global variables
a = 67
b = 200
occupied_cells = set()  # Set to store the occupied cells


def grid():
    """Draw tic-tac-toe grid."""
    # Drawing vertical lines for the grid
    line(-a, b, -a, -b)
    line(a, b, a, -b)
    # Drawing horizontal lines for the grid
    line(-b, -a, b, -a)
    line(-b, a, b, a)


def drawx(x, y):
    """Draw X player."""
    # Calculating the center of the square for x-coordinate and y-coordinate
    center_x = x + a
    center_y = y + a
    turtle.color('blue')  # Setting color to blue
    # Drawing the first diagonal line for 'X'
    line(center_x - 40, center_y - 40, center_x + 40, center_y + 40)
    # Drawing the second diagonal line for 'X'
    line(center_x - 40, center_y + 40, center_x + 40, center_y - 40)


def drawo(x, y):
    """Draw O player."""
    # Calculating the center of the square for x-coordinate and y-coordinate
    center_x = x + a
    center_y = y + a
    turtle.color('red')  # Setting color to red
    turtle.up()
    # Moving the pen to the center of the circle
    turtle.goto(center_x, center_y - 40)
    turtle.down()
    turtle.circle(40)  # Drawing the circle with a radius of 40


def floor(value):
    """Round down to the nearest grid position."""
    return ((value + b) // (a * 2)) * (a * 2) - b


state = {'player': 0}  # Dictionary to keep track of the current player
players = [drawx, drawo]  # List containing the draw functions for 'X' and 'O'


def tap(x, y):
    """Draw X or O in tapped square."""
    # Rounding down the x-coordinate and y-coordinate
    x = floor(x)
    y = floor(y)
    player = state['player']  # Getting the current player
    draw = players[player]  # Getting the draw function for the current player

    if (x, y) in occupied_cells:
        return  # Don't make a move if the cell is already occupied

    draw(x, y)  # Drawing 'X' or 'O' at the tapped square
    turtle.update()  # Updating the screen display
    state['player'] = not player  # Changing the player for the next turn
    occupied_cells.add((x, y))  # Add the cell to the occupied set


turtle.setup(420, 420, 370, 0)  # Setting up the turtle window
turtle.hideturtle()  # Hiding the turtle
turtle.tracer(False)  # Turning off the screen updates
grid()  # Drawing the grid
turtle.update()  # Updating the screen display
turtle.onscreenclick(tap)  # Binding the 'tap' function to mouse clicks
turtle.done()  # Completing the drawing and releasing control of the window
