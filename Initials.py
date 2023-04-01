# Imports turtle module
import turtle
turtle.showturtle()

# turns the background color to darkred
turtle.bgcolor("darkred")

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