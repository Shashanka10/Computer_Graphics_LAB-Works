import pygame
from OpenGL.GL import *

def draw_ellipse(rx, ry, xc, yc):
    glBegin(GL_POINTS)
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    while dx < dy:
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)

        if p1 < 0:
            x += 1
            dx += 2 * ry**2
            p1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2

    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    while y >= 0:
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)

        if p2 > 0:
            y -= 1
            dy -= 2 * rx**2
            p2 += rx**2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p2 += dx - dy + rx**2

    glEnd()

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
        draw_ellipse(200, 100, 400, 300)  # Change rx, ry, xc, yc as needed
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
