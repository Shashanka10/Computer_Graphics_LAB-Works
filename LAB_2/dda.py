from OpenGL.GL import *

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
    glBegin(GL_LINE_LOOP)
    for _ in range(int(steps + 1)):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()
