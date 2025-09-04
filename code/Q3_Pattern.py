import turtle                   # imports turtle, pythons graphics module

# the following section is the recursion, for whatever number of 'depth' the user inputs this section will repeat, creating the V pattern for every existing line and value of 'depth' until depth = 0

def edge(length, depth):        # draws one 'side' of the pattern
    if depth == 0:              
        turtle.forward(length)  # draws a straight line 
    else:
        length = length / 3     # splits the line into 3 parts
        edge(length, depth - 1) # draws the first straight part of the line
        turtle.right(60)        # angles the turtle downward for the first part of the V
        edge(length, depth - 1) # draws the second part of the line 
        turtle.left(120)        # angles the turtle upward for the second part of the V
        edge(length, depth - 1) # draws the third part of the line
        turtle.right(60)        # angles the turtle back to the original direction
        edge(length, depth - 1) # draws the final line


def shape(sides, length, depth):# draws a polygon
    angle = 360 / sides         # the angle for the turtle to turn at each 'corner', 360 degrees divided by the amount of sides (eg, 4 sides means the turtle turns at 90 degrees each side)
    for i in range(sides):      # loops this sections for the amount of sides
        edge(length, depth)
        turtle.right(angle)     # draws one side and turns the turtle at the specified angle for the next side

# this sections gets the users inputs for the drawing
sides = int(input("Number of sides: "))
length = int(input("Length of each side: "))
depth = int(input("Recursion depth: "))

turtle.speed(0)                 # this line tells the turtle to run at the fastest speed possible
turtle.hideturtle()             # this line hides the actual turtle cursor

shape(sides, length, depth)     # the line that tells the module to draw the shape

turtle.done()                   # this keeps the drawing window open after the turtle is complete
