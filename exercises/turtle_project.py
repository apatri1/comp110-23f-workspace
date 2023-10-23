"""Turtle Scene Project, landscape."""

__author__ = "730656248"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    myrtle: Turtle = Turtle()
    jim: Turtle = Turtle()
    john: Turtle = Turtle()
    draw_sky(myrtle, jim, john, 0, -900, 450)
    leo: Turtle = Turtle()
    line: Turtle = Turtle()
    draw_sun(leo, line, -75, -190, 110)
    jeff: Turtle = Turtle()
    draw_mountains(jeff, -300, -200, 400)
    draw_mountains(jeff, 100, -200, 400)
    chris: Turtle = Turtle()
    draw_grass(chris, -400, -200, 100, 800)
    i: int = 0
    distance: int = 0
    while i < 17:
        bob: Turtle = Turtle()
        bill: Turtle = Turtle()
        draw_trees(bob, bill, -270 + distance, -170, 30, 15)
        i += 1
        distance += 25
    
    done()


def draw_grass(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of given width as grass"""
    turtle.pencolor(3, 177, 15)
    turtle.fillcolor(3, 177, 15)
    turtle.speed(90)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()
    i: int = 0
    while (i < 2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_trees(turtle_br: Turtle, turtle_gr: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws the trees in the scene with triangles and rectangles."""
    turtle_br.pencolor(110, 60, 10)
    turtle_br.fillcolor(110, 60, 10)
    turtle_br.speed(90)
    turtle_br.hideturtle()

    turtle_br.penup()
    turtle_br.goto(x,y)
    turtle_br.pendown()

    turtle_br.begin_fill()
    i: int = 0
    while (i < 2):
        turtle_br.forward(length)
        turtle_br.right(90)
        turtle_br.forward(width)
        turtle_br.right(90)
        i += 1
    turtle_br.end_fill()

    turtle_gr.pencolor(10, 110, 20)
    turtle_gr.fillcolor(10, 110, 20)
    turtle_gr.speed(90) 
    turtle_gr.hideturtle()

    turtle_gr.penup()
    turtle_gr.goto(x - 13,y)
    turtle_gr.pendown()

    turtle_gr.begin_fill()
    i: int = 0
    while (i < 3):
        turtle_gr.forward(length + 26)
        turtle_gr.left(120)
        i += 1
    turtle_gr.end_fill()


def draw_mountains(turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draws the mountains with an obtuse triangle."""
    turtle.pencolor(204, 153, 96)
    turtle.fillcolor(251, 191, 124)
    turtle.speed(90)
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0.0)
    turtle.pendown()

    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(160)
    turtle.forward(length)
    turtle.left(40)
    turtle.forward(length)
    turtle.left(120)
    turtle.end_fill()


def draw_sky(turtle_blu: Turtle, turtle_dark: Turtle, turtle_darkest: Turtle, x: float, y: float, radius: float) -> None:
    """Draws the sky using three layers of circles."""
    turtle_blu.pencolor(170, 220, 255)
    turtle_blu.fillcolor(170, 220, 255)
    turtle_blu.speed(97)
    turtle_dark.pencolor(108, 186, 238)
    turtle_dark.fillcolor(108, 186, 238)
    turtle_dark.speed(97)
    turtle_darkest.pencolor(9, 127, 206)
    turtle_darkest.fillcolor(9, 127, 206)
    turtle_darkest.speed(97)

    turtle_darkest.penup()
    turtle_darkest.goto(x,y)
    turtle_darkest.pendown()

    turtle_darkest.begin_fill()
    turtle_darkest.circle(radius + 300)
    turtle_darkest.end_fill()

    turtle_dark.penup()
    turtle_dark.goto(x,y)
    turtle_dark.pendown()

    turtle_dark.begin_fill()
    turtle_dark.circle(radius + 100)
    turtle_dark.end_fill()
 
    turtle_blu.penup()
    turtle_blu.goto(x,y)
    turtle_blu.pendown()

    turtle_blu.begin_fill()
    turtle_blu.circle(radius)
    turtle_blu.end_fill()


def draw_sun(turtle: Turtle, turtle_2: Turtle, x: float, y: float, radius: float) -> None:
    """Draws the sun with a pattern inside."""
    turtle.pencolor(254, 204, 56)
    turtle.fillcolor(254, 204, 56)
    turtle.speed(97)

    turtle_2.pencolor(197, 150, 5)
    turtle_2.fillcolor(197, 150, 5)
    turtle_2.speed(97)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
    turtle_2.penup()
    turtle_2.goto(x,y)
    turtle_2.pendown()
    i: int = 0
    while (i < 155):
        turtle_2.circle(radius)
        i += 1
        radius = radius * 0.97


if __name__ == "__main__":
    main()