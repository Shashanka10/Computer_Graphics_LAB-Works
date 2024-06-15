import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Determine number of steps
    steps = max(abs(dx), abs(dy))

    # Calculate increment in x and y for each step
    x_inc = dx / steps
    y_inc = dy / steps

    # Draw the line
    x, y = x1, y1
    points = []
    for _ in range(int(steps + 1)):
        points.append((x, y))
        x += x_inc
        y += y_inc
    return points

x1, y1 = 1, 1
x2, y2 = 8, 7

points = DDA(x1, y1, x2, y2)

# Plotting the line
plt.plot([point[0] for point in points], [point[1] for point in points], marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('DDA Line Drawing Algorithm')
plt.grid(True)
plt.show()

