import turtle

def draw_star():
    # Create and configure turtle
    t = turtle.Turtle()
    t.speed(5)
    t.color("yellow")
    
    # Draw star
    t.penup()
    t.goto(-100, 0)  # Position for star
    t.pendown()
    
    for _ in range(5):
        t.forward(100)
        t.right(144)  # 144 degrees for a 5-pointed star
    
    t.hideturtle()

def draw_pentagon():
    # Create and configure turtle
    t = turtle.Turtle()
    t.speed(5)
    t.color("blue")
    
    # Draw pentagon
    t.penup()
    t.goto(100, 0)  # Position for pentagon
    t.pendown()
    
    for _ in range(5):
        t.forward(80)
        t.right(72)  # 72 degrees for a pentagon
    
    t.hideturtle()

# Draw both shapes
draw_star()
draw_pentagon()

# Keep the window open
turtle.done()
