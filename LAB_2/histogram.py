import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from dda import DDA

def draw_histogram(data):
    for i, height in enumerate(data):
        x0, y0 = i * 2, 0
        x1, y1 = i * 2, height
        x2, y2 = i * 2 + 1, height
        x3, y3 = i * 2 + 1, 0
        
        # Draw the four edges of the rectangle
        DDA(x0, y0, x1, y1)  # Left edge
        DDA(x1, y1, x2, y2)  # Top edge
        DDA(x2, y2, x3, y3)  # Right edge
        DDA(x3, y3, x0, y0)  # Bottom edge

def main():
    # Initialize Pygame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-5.0, 15.0, 0.0, 12.0, -1.0, 1.0)

    # Example histogram data
    data = [5, 10, 7, 3, 6, 8, 2]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(1.0, 1.0, 1.0)  # Set the color to white
        draw_histogram(data)
        
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
