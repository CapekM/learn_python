from turtle import forward, left, exitonclick, speed


def draw_square(a: int=50):
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)

for i in range(20):
    speed(i)
    draw_square(i*20)
    left(20)

exitonclick()
