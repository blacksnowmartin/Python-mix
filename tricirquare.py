from ursina import *
import math
import random

app = Ursina()
window.color = color.rgb(20, 20, 30)  # Start with a dark background

# Create base entities for transformation
class AlchemyElement(Entity):
    def __init__(self, position, **kwargs):
        super().__init__(
            position=position,
            scale=1,
            **kwargs
        )
        self.original_color = self.color
        self.target_color = None
        self.is_transformed = False
        self.pulse_speed = random.uniform(1, 2)
        
    def transform(self):
        if not self.is_transformed:
            self.target_color = color.rgb(
                random.randint(200, 255),
                random.randint(200, 255),
                random.randint(150, 255)
            )
            self.is_transformed = True
            # Play transform sound if available
            if 'transform_sound' in globals():
                transform_sound.play()

    def update(self):
        if self.is_transformed:
            self.color = lerp(self.color, self.target_color, time.dt)
            self.rotation_y += time.dt * 50
            scale_pulse = math.sin(time.time() * self.pulse_speed) * 0.1
            self.scale = Vec3(1 + scale_pulse, 1 + scale_pulse, 1 + scale_pulse)

# Create negative thought elements
negative_thoughts = []
for i in range(5):
    thought = AlchemyElement(
        position=Vec3(
            random.uniform(-3, 3),
            random.uniform(-2, 2),
            0
        ),
        model='cube',
        color=color.rgb(50, 50, 50),
        texture='white_cube',
        scale=0.5
    )
    negative_thoughts.append(thought)

# Create transformation particles
particle_system = ParticleSystem(
    position=Vec3(0,0,0),
    particles_per_second=20,
    lifetime=1,
    scale=0.2,
    speed=2,
    rotation_speed=50
)
particle_system.disable()

# Text elements for emotional states
negative_words = ['Fear', 'Doubt', 'Worry', 'Stress', 'Anxiety']
positive_words = ['Peace', 'Joy', 'Hope', 'Love', 'Growth']
text_elements = []

for i, word in enumerate(negative_words):
    text = Text(
        text=word,
        position=Vec2(-0.6 + i * 0.3, 0.4),
        color=color.rgb(100, 100, 100),
        scale=1.5
    )
    text_elements.append(text)

# Interaction handling
def on_click():
    hit_info = mouse.hovered_entity
    if hit_info in negative_thoughts:
        hit_info.transform()
        particle_system.position = hit_info.position
        particle_system.enable()
        invoke(particle_system.disable, delay=1)
        
        # Transform corresponding text
        index = negative_thoughts.index(hit_info)
        if index < len(text_elements):
            text_elements[index].text = positive_words[index]
            text_elements[index].color = color.rgb(200, 200, 100)
        
        # Check if all elements are transformed
        if all(thought.is_transformed for thought in negative_thoughts):
            window.animate_color(color.rgb(50, 100, 150), duration=2)

mouse.on_click = on_click

# Camera setup
camera.orthographic = True
camera.fov = 10
EditorCamera()

# Global update function
def update():
    for thought in negative_thoughts:
        if not thought.is_transformed:
            thought.rotation_y += time.dt * 20
            thought.y += math.sin(time.time() + negative_thoughts.index(thought)) * time.dt

# Audio setup (requires audio file)
try:
    transform_sound = Audio(
        'transform.wav',
        autoplay=False,
        loop=False
    )
except:
    print("Note: Transform sound file not found")

app.run()
