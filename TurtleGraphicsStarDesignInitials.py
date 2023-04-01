# Imports turtle module
import turtle

turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('green')
for x in range(13):
        turtle.forward(200)
        turtle.left(150)
# turns the background color to darkred
turtle.bgcolor("darkred")

length = 50
angle = 90

for x in range(5):
        turtle.left(50)
        turtle.right(90)
        #length = length + 10
# Designing the letter S
turtle.pensize(8)
turtle.color("turquoise")
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

# Moving the pen next to the letter S
turtle.penup()
turtle.goto(75, -50)
turtle.pendown()

# Drawing the G
turtle.pensize(4)
turtle.color("midnightblue")
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(15)
turtle.left(90 * 2)
turtle.forward(30)

# re position pen
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.left(100)

# Draw Star
turtle.pensize(12)
turtle.color("darkslategray")
turtle.forward(300)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300)

# re position pen
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.left(100)
turtle.pensize(12)
turtle.color("silver")
length = 300
angle = 144

for x in range(5):
        turtle.forward(length + length)
        turtle.right(angle)
        length = length + 10

# Draw Second Star
turtle.pensize(12)
turtle.color("silver")
turtle.forward(300)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300 * 2)
turtle.right(144)
turtle.forward(300)
turtle.done()

