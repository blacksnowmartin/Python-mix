import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Define the Sephirah points (positions)
sephirot = {
    'Keter': (0, 2),      # Crown
    'Chokhmah': (-1, 1),  # Wisdom
    'Binah': (1, 1),      # Understanding
    'Chesed': (-1, 0),    # Mercy
    'Gevurah': (1, 0),    # Strength
    'Tiferet': (0, 0),    # Beauty
    'Malkhut': (0, -1)    # Kingdom
}

# Define connections between Sephirah
connections = [
    ('Keter', 'Chokhmah'),
    ('Keter', 'Binah'),
    ('Chokhmah', 'Chesed'),
    ('Binah', 'Gevurah'),
    ('Chesed', 'Tiferet'),
    ('Gevurah', 'Tiferet'),
    ('Tiferet', 'Malkhut')
]

# Create scatter plot for points
scatter = ax.scatter([], [], c='gold', s=200)

# Create lines for connections
lines = [ax.plot([], [], 'w-', alpha=0.5)[0] for _ in connections]

# Add labels
labels = {name: ax.text(x, y, name, ha='center', va='center', color='white')
          for name, (x, y) in sephirot.items()}

def init():
    scatter.set_offsets(np.c_[[], []])
    for line in lines:
        line.set_data([], [])
    return scatter, *lines

def animate(frame):
    # Calculate positions with animation
    t = frame / 50.0
    points = []
    
    for name, (x, y) in sephirot.items():
        # Add subtle circular motion
        dx = 0.1 * math.sin(t + hash(name) % 10)
        dy = 0.1 * math.cos(t + hash(name) % 10)
        points.append([x + dx, y + dy])
    
    scatter.set_offsets(np.c_[points])
    
    # Update connection lines
    for i, (start, end) in enumerate(connections):
        start_idx = list(sephirot.keys()).index(start)
        end_idx = list(sephirot.keys()).index(end)
        lines[i].set_data([points[start_idx][0], points[end_idx][0]],
                         [points[start_idx][1], points[end_idx][1]])
    
    # Update labels
    for (name, label), point in zip(labels.items(), points):
        label.set_position(point)
    
    return scatter, *lines

# Create animation
anim = FuncAnimation(fig, animate, init_func=init,
                    frames=200, interval=50, blit=True)

# Set background color
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])

plt.show()
