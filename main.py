import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=700,height=500)
window.bgcolor("black")

border = turtle.Turtle()
border.speed(0)
border.color('black')
border.begin_fill()
border.goto(-250,150)
border.goto(250,150)
border.goto(250,-150)
border.goto(-250,-150)
border.goto(-250,150)
border.end_fill()

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1,stretch_wid=7)
rocket_a.penup()
rocket_a.goto(-350,0)

rocket_b = turtle.Turtle()
rocket_b.speed(3)
rocket_b.shape("square")
rocket_b.color("white")
rocket_b.shapesize(stretch_wid=7, stretch_len=1)
rocket_b.penup()
rocket_b.goto(344, 0)

def move_up():
     y  = rocket_a.ycor() + 10
     if y > 250:
         y = 250
     rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

window.mainloop()