import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig, ax = plt.subplots()

# Face (circle)
face = plt.Circle((0, 0), 1, color='yellow', ec='black', lw=2)
ax.add_patch(face)

# Eyes
left_eye = plt.Circle((-0.3, 0.4), 0.1, color='black')
right_eye = plt.Circle((0.3, 0.4), 0.1, color='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Smile (using a semicircle)
theta = np.linspace(200, 340, 100)  # arc angles for smile
x = 0.5 * np.cos(np.deg2rad(theta))
y = 0.3 * np.sin(np.deg2rad(theta)) - 0.2
ax.plot(x, y, color='black', lw=3)

# Set aspect ratio and remove axes
ax.set_aspect('equal')
ax.axis('off')

# Display the smile
plt.title("Smiley Face 😊", fontsize=16)
plt.show()
