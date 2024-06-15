import pygame
from OpenGL.GL import *
from math import cos, sin, radians

def draw_circle_segment(radius, xc, yc):
    glBegin(GL_POINTS)
    theta = 0
    while theta <= 45:  # theta goes from 0 to 45 degrees (pi/4)
        angle = radians(theta)
        x = radius * cos(angle)
        y = radius * sin(angle)
        draw_points(xc, yc, x, y)
        theta += 1  # increment theta by 1 degree
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
        glColor3f(0.0, 1.0, 0.0)  # green color
        glPointSize(2)
        draw_circle_segment(200, 400, 300)  # Change radius and center coordinates as needed
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
