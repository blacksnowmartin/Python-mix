import turtle
import math

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def flower_of_life():
    # Setup
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    
    # Initial settings
    radius = 100
    center_x, center_y = 0, 0
    
    # First circle in center
    draw_circle(t, center_x, center_y, radius)
    
    # Draw 6 circles around the center
    for angle in range(0, 360, 60):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        draw_circle(t, x, y, radius)
    
    # Draw outer circles
    for angle in range(30, 390, 60):
        x = center_x + (radius * 2 * math.cos(math.radians(angle)) / math.sqrt(3))
        y = center_y + (radius * 2 * math.sin(math.radians(angle)) / math.sqrt(3))
        draw_circle(t, x, y, radius)
    
    screen.mainloop()

if __name__ == "__main__":
    flower_of_life()
