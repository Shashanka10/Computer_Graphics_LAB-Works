from OpenGL.GL import *

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
        glBegin(GL_LINE_LOOP)
        for _ in range(int(dx + 1)):
            glVertex2f(x, y)
            if p >= 0:
                y += y_inc
                p -= 2 * dx
            x += x_inc
            p += 2 * dy
        glEnd()
    else:  # Steep slope
        p = 2 * dx - dy
        x_inc = 1 if x2 > x1 else -1
        y_inc = 1 if y2 > y1 else -1
        x, y = x1, y1
        glBegin(GL_LINE_LOOP)
        for _ in range(int(dy + 1)):
            glVertex2f(x, y)
            if p >= 0:
                x += x_inc
                p -= 2 * dy
            y += y_inc
            p += 2 * dx
        glEnd()
