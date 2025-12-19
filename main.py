import turtle
import random
from random import randint

#setting
gameBoard = turtle.Screen()
gameBoard.setup(width=800, height=800)
gameBoard.bgcolor("light blue")
gameBoard.title("Turtle Board Game")
y1 = gameBoard.window_height() * 0.45
y2 = gameBoard.window_height() * 0.45

#player objects
t1 = turtle.Turtle()
t1.speed(0)
t1.shape("turtle")
t1.color("green")
t1.turtlesize(2)
score_title = turtle.Turtle()
score_title.hideturtle()
score_title.penup()
score_title.goto(-50, y1)
score_title.write("Score: 0", align="center", font=("Courier", 20, "normal"))
timer_title = turtle.Turtle()
timer_title.hideturtle()
timer_title.penup()
timer_title.goto(70, y2)


score = 0
game_over = False



#functions
def border_draw():
    border = turtle.Turtle()
    border.hideturtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.goto(-290, 290)
    border.pendown()
    for i in range(4):
        border.forward(580)
        border.right(90)
def score_update(x, y):
    global score
    score += 1
    score_title.clear()
    score_title.write(
        f"Score: {score}",
        align="center",
        font=("Courier", 20, "normal")
    )
    t1.color("red")
    gameBoard.ontimer(turn_green(), 500)
def turn_green():
    t1.color("green")

def turtle_move():
    if not game_over:
        #t1.hideturtle()
        t1.penup()
        x = randint(-280, 280)
        y = randint(-280, 280)
        t1.goto(x, y)
        #t1.showturtle()
        gameBoard.ontimer(turtle_move, 800)

def count_down(time_left):
    global game_over
    if time_left > 0:
        timer_title.clear()
        timer_title.write(
            f"Time: {time_left}",
            align="center",
            font=("Courier", 20, "normal")
        )
        gameBoard.ontimer(lambda: count_down(time_left-1), 1000)
    else:
        game_over = True
        gameBoard.bgcolor("red")
        timer_title.clear()
        timer_title.write(
        "GAME_OVER",
        align="center",
        font=("Courier", 20, "normal")
        )
        t1.hideturtle()
gameBoard.tracer(0)
border_draw()
gameBoard.tracer(1)
t1.onclick(score_update)
turtle_move()
count_down(20)
turtle.mainloop()
