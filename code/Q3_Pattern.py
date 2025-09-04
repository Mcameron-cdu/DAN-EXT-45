import turtle

def edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length = length / 3
        edge(length, depth - 1)
        turtle.right(60)
        edge(length, depth - 1)
        turtle.left(120)
        edge(length, depth - 1)
        turtle.right(60)
        edge(length, depth - 1)


def shape(sides, length, depth):
    angle = 360 / sides
    for i in range(sides):
        edge(length, depth)
        turtle.right(angle)

sides = int(input("Number of sides: "))
length = int(input("Length of each side: "))
depth = int(input("Recursion depth: "))

turtle.speed(0)
turtle.hideturtle()

shape(sides, length, depth)

turtle.done()