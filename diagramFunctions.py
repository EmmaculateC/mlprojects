import turtle
import math

def main():
    turtle.hideturtle()
    turtle.speed(15)

    # Draw the 3 squares
    square(-125, 110, 300, fill_colour='blue', line_colour='yellow')
    square(130, 50, 75, fill_colour='red')
    square(85, -125, 150, fill_colour='purple', line_colour='green')

    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(25)

    # Draw the 3 Octogons
    octogon(85, -125, 115, fill_colour='blue', line_colour='yellow')
    octogon(-125, 75, 30, fill_colour='red')
    octogon(125, 100, 65, fill_colour='purple', line_colour='green')

    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(50)

    # Draw the 3 Spyrographs
    spyrograph(-125, 110, 100, fill_colour='blue', line_colour='yellow', line_width=2)
    spyrograph(130, 50, 25, fill_colour='red')
    spyrograph(85, -125, 50, fill_colour='purple', line_colour='green')

    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(100)

    # Draw the 3 Starburst
    starburst(130, 50, 380, fill_colour='blue', line_colour='yellow')
    starburst(60, -180, 95, fill_colour='red', line_width=2)
    starburst(-180, -30, 190, fill_colour='purple', line_colour='green')

    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(100)

    # Draw something fancy with all four diagrams
    square(-120, 120, 240, fill_colour='black')
    square(120, -120, 240, fill_colour='black')
    starburst(-120, 120, 200, fill_colour='blue', line_colour='orange', line_width=1)
    spyrograph(120, -120, 50, fill_colour='purple', line_colour='yellow', line_width=1)
    octogon(120, 120, 60, fill_colour='red', line_colour='green', line_width=3)
    square(-120, -120, 130, fill_colour='magenta', line_colour='green', line_width=3)

def square(center_x, center_y, side_length, *, line_colour='black', fill_colour='', line_width=1):
    start_x = center_x - side_length / 2
    start_y = center_y - side_length / 2
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    if fill_colour:
        turtle.begin_fill()
        turtle.fillcolor(fill_colour)
    turtle.pencolor(line_colour)
    turtle.pensize(line_width)
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    if fill_colour:
        turtle.end_fill()

def octogon(center_x, center_y, side_length, *, line_colour='black', fill_colour='', line_width=1):
    start_x = center_x - side_length * (2 ** 0.5) / 2
    start_y = center_y + side_length / 2
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    if fill_colour:
        turtle.begin_fill()
        turtle.fillcolor(fill_colour)
    turtle.pencolor(line_colour)
    turtle.pensize(line_width)
    for _ in range(8):
        turtle.forward(side_length)
        turtle.right(45)
    if fill_colour:
        turtle.end_fill()

def spyrograph(center_x, center_y, circle_radius, *, line_colour='black', fill_colour='', line_width=1):
    turtle.penup()
    turtle.goto(center_x, center_y - circle_radius)
    turtle.pendown()
    if fill_colour:
        turtle.begin_fill()
        turtle.fillcolor(fill_colour)
    turtle.pencolor(line_colour)
    turtle.pensize(line_width)
    for _ in range(36):
        turtle.circle(circle_radius, 170)
        turtle.circle(circle_radius / 2, 170)
    if fill_colour:
        turtle.end_fill()

def starburst(center_x, center_y, side_length, *, line_colour='black', fill_colour='', line_width=0):
    start_x = center_x - side_length / 2
    start_y = center_y + side_length / 2
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    if fill_colour:
        turtle.begin_fill()
        turtle.fillcolor(fill_colour)
    turtle.pencolor(line_colour)
    turtle.pensize(line_width)
    for _ in range(36):
        turtle.forward(side_length)
        turtle.right(170)
        turtle.forward(side_length)
    if fill_colour:
        turtle.end_fill()

if __name__ == '__main__':
    main()
