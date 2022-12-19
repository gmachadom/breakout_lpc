import turtle
import os
import random

# score and lives
score = 0
lives = 3

# Draw screen
screen = turtle.Screen()
screen.title("My Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

# Draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=0.5, stretch_len=2)
paddle.penup()
paddle.goto(0, -350)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Draw blocks
blocks_x = [-195, -130, -65, 0, 65, 130, 195]
blocks_y = [260, 240, 220, 200, 180]
block_list = []
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue',
          'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'chocolate', 'brown', 'gray']

for i in blocks_x:
    for j in blocks_y:
        block = turtle.Turtle()
        block.speed(0)
        block.shape("square")
        block.color(random.choice(colors))
        block.shapesize(stretch_wid=0.5, stretch_len=3)
        block.penup()
        block.goto(i, j)
        block_list.append(block)

block_count = len(block_list)


# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 320)
hud.write(f"LIVES: {lives}\n", align="center", font=("Arial", 18, "normal"))
hud.write(f"SCORE: {score}", align="center", font=("Arial", 18, "normal"))


def paddle_right():
    if paddle.xcor() < 270:
        paddle.setx(paddle.xcor() + 30)


def paddle_left():
    if paddle.xcor() > -270:
        paddle.setx(paddle.xcor() - 30)


def paddle_collision():
    if ball.ycor() == -340:
        if (ball.xcor() > paddle.xcor() - 30) and (ball.xcor() < paddle.xcor() + 30):
            ball.dy *= -1


# keyboard
screen.listen()
screen.onkeypress(paddle_right, "d")
screen.onkeypress(paddle_left, "a")

while block_count > 0 and lives >= 0:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() - ball.dx)
    ball.sety(ball.ycor() - ball.dy)

    paddle_collision()

    # collision with the right wall
    if ball.xcor() > 290:
        os.system("afplay bounce.wav&")
        ball.dx *= -1

    # collision with left wall
    if ball.xcor() < -290:
        os.system("afplay bounce.wav&")
        ball.dx *= -1

    # collision with upper wall
    if ball.ycor() > 390:
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.dy *= -1

    # collision with bottom wall
    if ball.ycor() < -390:
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        lives -= 1
        hud.clear()
        hud.write(f"LIVES: {lives}\n", align="center", font=("Arial", 18, "normal"))
        hud.write(f"SCORE: {score}", align="center", font=("Arial", 18, "normal"))

    # collision with the paddle
    if ball.xcor() < -330 and paddle.xcor() + 50 > ball.ycor() > paddle.xcor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    for i in block_list:
        if (ball.xcor() >= i.xcor()-30) and (ball.xcor() <= i.xcor()+30):
            if (ball.ycor()+5 >= i.ycor()-10) and (ball.ycor()-5 <= i.ycor()+10):
                if (i.ycor()-10 - ball.ycor()+5) >= 0 or (i.ycor()+10 - ball.ycor()-5) >= 0:
                    ball.dy *= -1
                elif (i.xcor()-30 - ball.xcor()) >= 0 or (i.xcor()+30 - ball.xcor()) >= 0:
                    ball.dx *= -1
                else:
                    ball.dy *= -1
                    ball.dx *= -1
                i.goto(1000, 1000)
                score += 1
                hud.clear()
                hud.write(f"LIVES: {lives}\n", align="center", font=("Arial", 18, "normal"))
                hud.write(f"SCORE: {score}", align="center", font=("Arial", 18, "normal"))
                block_count -= 1


ball.reset()
for i in block_list:
    i.reset()
paddle.reset()
hud.clear()
hud.goto(0, 0)
hud.write("GAME OVER\n", align="center", font=("Press Start 2P", 20, "normal"))
hud.write(f"SCORE: {score}", align="center", font=("Press Start 2P", 20, "normal"))
turtle.done()
