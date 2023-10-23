from turtle import Turtle, colormode, done
colormode(255)
side_length: int = 300

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.pencolor(104, 12, 153)
leo.fillcolor(212, 158, 236)

leo.penup()
leo.goto(0,0)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor(67, 17, 89)
bob.speed(89)
bob.hideturtle()

bob.penup()
bob.goto(0,0)
bob.pendown()

i: int = 0
while (i < 155):
    bob.forward(side_length)
    bob.left(120.7)
    i += 1
    side_length = side_length * 0.97

done()