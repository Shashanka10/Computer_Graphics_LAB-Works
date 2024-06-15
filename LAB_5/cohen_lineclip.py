import pygame
from pygame.locals import *
from OpenGL.GL import *

# Cohen-Sutherland outcode region constants
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define the clipping boundary
xmin, xmax, ymin, ymax = -0.5, 0.5, -0.5, 0.5

# Function to compute the outcode for a point (x, y)
def compute_outcode(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

# Cohen-Sutherland line clipping algorithm
def cohen_sutherland_clip(x0, y0, x1, y1):
    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)
    accept = False

    while True:
        if not (outcode0 | outcode1):
            accept = True
            break
        elif outcode0 & outcode1:
            break
        else:
            x, y = 0.0, 0.0
            outcode_out = outcode0 if outcode0 else outcode1
            if outcode_out & TOP:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)
    
    if accept:
        return x0, y0, x1, y1
    else:
        return None

def main():
    pygame.init()
    display = (900,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-1, 1, -1, 1, -1, 1)

    line_start = (-0.7, -0.2)
    line_end = (0.7, 0.7)

    clipped_line = cohen_sutherland_clip(*line_start, *line_end)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the clipping boundary
        glColor3f(0.0, 1.0, 0.0)
        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # Draw the original line
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(*line_start)
        glVertex2f(*line_end)
        glEnd()

        # Draw the clipped line
        if clipped_line:
            glColor3f(0.0, 0.0, 1.0)
            glBegin(GL_LINES)
            glVertex2f(clipped_line[0], clipped_line[1])
            glVertex2f(clipped_line[2], clipped_line[3])
            glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
