import turtle 

turtle.speed(3)
turtle.bgcolor("black")
turtle.pensize(3)
def func():
    for i in range(200):  # Fixed missing colon
        turtle.right(1)
        turtle.forward(1)

turtle.color('red','pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()

# Add animated text
turtle.penup()
turtle.goto(0, -50)  # Position text below the heart
turtle.color("white")
turtle.write("I love you Everlyne", align="center", font=("Brush Script MT", 24, "italic"))
turtle.hideturtle()
