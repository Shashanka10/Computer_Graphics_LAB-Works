import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from dda import DDA
from bla import BLA

# Define the window dimensions
width, height = 800, 600

def draw_histogram(frequency_data):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Set up the orthographic projection with padding
    glOrtho(-1.2, 1.2, -1.2, 1.2, -1, 1)

    # Draw grid lines
    glColor3f(0.5, 0.5, 0.5)  # Gray color for grid lines
    glBegin(GL_LINES)
    for i in range(-10, 11):  # Draw grid lines along x-axis
        glVertex2f(i / 10, -1)
        glVertex2f(i / 10, 1)
    for i in range(-10, 11):  # Draw grid lines along y-axis
        glVertex2f(-1, i / 10)
        glVertex2f(1, i / 10)
    glEnd()

    # # Draw the histogram bars
    bar_width = 2 / len(frequency_data)
    for i, freq in enumerate(frequency_data):
        x1 = -1 + i * bar_width
        y1 = -1
        x2 = x1 + bar_width
        y2 = -1 + freq / max(frequency_data) * 1.8  # Scale the bar's height

        # Draw histogram bar
        glColor3f(0.0, 0.3, 0.6)
        glBegin(GL_QUADS)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()
        
        # Draw histogram bar
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x1, y1)
        glVertex2f(x2, y1)
        glVertex2f(x2, y2)
        glVertex2f(x1, y2)
        glEnd()
    
    # Draw x and y axes with ticks
    glColor3f(0.0, 1.0, 0.0) # White color for axes
    glBegin(GL_LINES)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)
    for i in range(-10, 11):
        glVertex2f(i / 10, -1)
        glVertex2f(i / 10, -0.98)
        glVertex2f(-1, i / 10)
        glVertex2f(-0.98, i / 10)
    glEnd()

    # # Draw lines using BLA and DDA
    # glColor3f(0.0, 0.0, 0.0)  # Red color for lines
    # BLA(-0.8, 0.8, 0.8, -0.8)  # Using Bresenham (steep slope)
    # DDA(-0.8, -0.8, 0.8, 0.8)  # Using DDA

    pygame.display.flip()

def main():
    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.1, 0.1, 0.1, 1.0)

    frequency_data = [50, 30, 70, 40, 90, 60, 20, 80, 75, 55]  # Adjusted example data

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_histogram(frequency_data)

if __name__ == "__main__":
    main()
