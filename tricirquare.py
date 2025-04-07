from ursina import *
import math

app = Ursina()

# Create a window
window.color = color.black

# Function to create triangle vertices
def create_triangle(size=4):
    height = size * math.sqrt(3) / 2
    return [
        (0, height/2, 0),
        (-size/2, -height/2, 0),
        (size/2, -height/2, 0)
    ]

# Create triangle
triangle_vertices = create_triangle()
triangle = Entity(
    model=Mesh(vertices=triangle_vertices, triangles=[0,1,2]),
    color=color.white,
    position=(0,0,0)
)

# Calculate radius of inscribed circle
# r = A/s where A is area and s is semi-perimeter
side = 4  # length of triangle side
s = (3 * side) / 2  # semi-perimeter
area = (side * side * math.sqrt(3)) / 4
radius = area / s

# Create inscribed circle
circle = Entity(
    model='circle',
    color=color.yellow,
    scale=(radius, radius),
    position=(0, -radius/3, 0)
)

# Create inscribed square
# Side length of inscribed square in circle = radius * sqrt(2)
square_size = radius * math.sqrt(2)
square = Entity(
    model='quad',
    color=color.red,
    scale=(square_size, square_size),
    position=(0, -radius/3, 0)
)

# Camera setup
camera.orthographic = True
camera.fov = 10
camera.position = (0, 0, -20)

def update():
    camera.x = math.sin(time.time()) * 2
    camera.y = math.cos(time.time()) * 2

app.run()
