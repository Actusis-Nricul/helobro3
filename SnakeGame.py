import turtle
import random
import time
import sys

# Try sound (Windows only)
try:
    import winsound
    SOUND_ON = True
except:
    SOUND_ON = False

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game🐍")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

GRID_SIZE = 20

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 🐍 tongue (fun little triangle)
tongue = turtle.Turtle()
tongue.shape("triangle")
tongue.color("red")
tongue.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.penup()

# Snap food to grid
def spawn_food():
    x = random.randint(-14, 14) * GRID_SIZE
    y = random.randint(-14, 14) * GRID_SIZE
    food.goto(x, y)

spawn_food()

segments = []
score = 0

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + GRID_SIZE)
    if head.direction == "down":
        head.sety(y - GRID_SIZE)
    if head.direction == "left":
        head.setx(x - GRID_SIZE)
    if head.direction == "right":
        head.setx(x + GRID_SIZE)

# Keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def play_sound():
    if SOUND_ON:
        winsound.Beep(800, 100)
    else:
        print("🍎 *nom sound*")

def update_tongue():
    # tongue sticks out in movement direction
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        tongue.goto(x, y + 10)
    elif head.direction == "down":
        tongue.goto(x, y - 10)
    elif head.direction == "left":
        tongue.goto(x - 10, y)
    elif head.direction == "right":
        tongue.goto(x + 10, y)
    else:
        tongue.goto(1000, 1000)  # hide

# Game loop
while True:
    wn.update()
    update_tongue()

    # wall collision
    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for seg in segments:
            seg.goto(1000, 1000)

        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

    # food collision (GRID PERFECT)
    if head.distance(food) < 20:
        spawn_food()
        play_sound()

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lime")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    # move body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # self collision
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(1000, 1000)

            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

    time.sleep(0.1)

wn.mainloop()
