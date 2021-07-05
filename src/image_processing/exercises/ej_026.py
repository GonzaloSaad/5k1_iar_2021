import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy import ndimage

from src import matrix as m

found_lines_colors = ["red", "green", "cyan", "magenta"]

points = [
    (1, 4),
    (2, 5),
    (2, 7),
    (2, 9),
    (3, 10),
]
input_points = np.array([points])
x_space, y_space = input_points.T

# Classic straight-line Hough transform
# Set a precision of 0.5 degree.
tested_angles = np.linspace(-np.pi / 2, np.pi / 2, 360, endpoint=False)

radius_precision = 0.05

r_size = int(11 * 2 * (1 / radius_precision))
accumulator = np.zeros((360, r_size))

medium_r_index = (r_size / 2) - 1
for x, y in points:
    for theta_index, theta in enumerate(tested_angles):
        r = round(x * np.cos(theta) + y * np.sin(theta), 2)
        r_index = int(medium_r_index + (r / radius_precision))
        accumulator[theta_index, r_index] += 1

# Figures
fig, axes = plt.subplots(1, 3, figsize=(15, 6))

###############################
# Generating figure 1
###############################
axes[0].set_title('Puntos a detectar')
axes[0].scatter(x_space, y_space)
axes[0].set_ylim(bottom=0, ymax=13)
axes[0].set_xlim(xmin=0, xmax=4)
axes[0].grid(linestyle='--', linewidth='0.5', color='grey')

###############################
# Generating figure 2
###############################

angle_step = 0.5 * np.diff(tested_angles).mean()
d_step = 360 / np.pi

bounds = [-90, +90, -220, +220]
rotated_img = ndimage.rotate(accumulator, 90)
axes[1].imshow(rotated_img, extent=bounds, cmap=cm.gray, aspect=1 / 1.5)
axes[1].set_title('Espacio de Hough')
axes[1].set_xlabel('Ángulos (grados)')
axes[1].set_ylabel(f'Distancia (cantidad de steps de {radius_precision})')

###############################
# Generating figure 3
###############################
axes[2].scatter(x_space, y_space)

axes[2].grid(linestyle='--', linewidth='0.5', color='grey')
axes[2].set_title('Lineas detectadas')
sorted_points = sorted(m.iterate(accumulator), key=lambda elem: elem[2], reverse=True)

for index, point in enumerate(sorted_points[:4]):
    theta_index, r_index, acc = point
    theta = tested_angles[theta_index]
    r = (r_index - medium_r_index) * radius_precision
    (x0, y0) = r * np.array([np.cos(theta), np.sin(theta)])

    angle = theta + np.pi / 2
    axes[2].axline(
        (x0, y0),
        slope=np.tan(angle),
        color=found_lines_colors[index],
        linewidth='1.1',
        linestyle='dashed',
        label=f'theta={np.rad2deg(angle):.2f}°, rho={r:.2f}'
    )

axes[2].set_ylim(bottom=0, ymax=13)
axes[2].set_xlim(xmin=0, xmax=4)
plt.legend(loc='lower center')
plt.tight_layout()
plt.show()
