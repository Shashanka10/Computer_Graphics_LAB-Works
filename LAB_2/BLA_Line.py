import matplotlib.pyplot as plt

def BLA(x1, y1, x2, y2):
    # Calculate dx and dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine increments based on slope
    if dx > dy:  # Shallow slope
        p = 2 * dy - dx
        x_inc = 1 if x2 > x1 else -1
        y_inc = 1 if y2 > y1 else -1
        x, y = x1, y1
        points = []
        for _ in range(int(dx + 1)):
            points.append((x, y))
            if p >= 0:
                y += y_inc
                p -= 2 * dx
            x += x_inc
            p += 2 * dy
    else:  # Steep slope
        p = 2 * dx - dy
        x_inc = 1 if x2 > x1 else -1
        y_inc = 1 if y2 > y1 else -1
        x, y = x1, y1
        points = []
        for _ in range(int(dy + 1)):
            points.append((x, y))
            if p >= 0:
                x += x_inc
                p -= 2 * dy
            y += y_inc
            p += 2 * dx
    return points
x1, y1 = 1, 1
x2, y2 = 8, 7
points = BLA(x1, y1, x2, y2)
# Plotting the line
plt.plot([point[0] for point in points], [point[1] for point in points], marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Line Algorithm')
plt.grid(True)
plt.show()


