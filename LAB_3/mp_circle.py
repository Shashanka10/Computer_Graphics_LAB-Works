import pygame
from OpenGL.GL import *

def draw_circle(radius, xc, yc):
    glBegin(GL_POINTS)
    x = 0
    y = radius
    d = 1 - radius
    draw_points(xc, yc, x, y)
    while y > x:
        if d < 0:
            d += 2 * x
        else:
            d += 2 * (x - y)
            y -= 1
        x += 1
        draw_points(xc, yc, x, y)
    glEnd()
    
def draw_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glOrtho(0, 800, 0, 600, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)  # white color
        glPointSize(3)
        draw_circle(200, 400, 300)  # Change radius and center coordinates as needed
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


