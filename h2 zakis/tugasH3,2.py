import turtle

window = turtle.Screen()

def drawColoredSquare(ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
    ttl.end_fill()
    ttl.penup()

def drawColoredTriangle(ttl, x, y, length, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(3):
        ttl.forward(length)
        ttl.left(120)
    ttl.end_fill()
    ttl.penup()

def drawColoredJa(ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(130)
        ttl.forward(width)
        ttl.left(50)
    ttl.end_fill()
    ttl.penup()

def drawColoredTrapezoid(ttl, x, y, top_length, bottom_length, height, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.forward(top_length)
    ttl.left(120)
    ttl.forward(height)
    ttl.left(60)
    ttl.forward(bottom_length)
    ttl.left(60)
    ttl.forward(height)
    ttl.left(60)
    ttl.forward(bottom_length)
    ttl.end_fill()
    ttl.penup()

def drawColoredPentagon(ttl, x, y, side_length, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(90)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(5):
        ttl.forward(side_length)
        ttl.right(72)
    ttl.end_fill()
    ttl.penup()

Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)

drawColoredSquare(Bob, 0, 0, 150, 100, "red")
drawColoredTriangle(Bob, 0, 150, 150, "yellow")
drawColoredJa(Bob, 0, -150, 150, 75, "blue")
drawColoredTrapezoid(Bob, 300, 0, 100, 50, 120, "green")
drawColoredPentagon(Bob, 0, 300, 100, "purple")  # Adjust the position and size as needed

window.exitonclick()