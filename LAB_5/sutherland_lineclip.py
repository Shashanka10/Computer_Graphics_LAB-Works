import pygame
from pygame.locals import *
from OpenGL.GL import *

# Define the clipping boundary
xmin, xmax, ymin, ymax = -0.5, 0.5, -0.5, 0.5

# Sutherland-Hodgman polygon clipping algorithm
def sutherland_hodgman_clip(subject_polygon, clip_polygon):
    def inside(p, edge):
        if edge == "left":
            return p[0] >= xmin
        elif edge == "right":
            return p[0] <= xmax
        elif edge == "bottom":
            return p[1] >= ymin
        elif edge == "top":
            return p[1] <= ymax

    def compute_intersection(p1, p2, edge):
        if edge == "left":
            x = xmin
            y = p1[1] + (p2[1] - p1[1]) * (xmin - p1[0]) / (p2[0] - p1[0])
        elif edge == "right":
            x = xmax
            y = p1[1] + (p2[1] - p1[1]) * (xmax - p1[0]) / (p2[0] - p1[0])
        elif edge == "bottom":
            y = ymin
            x = p1[0] + (p2[0] - p1[0]) * (ymin - p1[1]) / (p2[1] - p1[1])
        elif edge == "top":
            y = ymax
            x = p1[0] + (p2[0] - p1[0]) * (ymax - p1[1]) / (p2[1] - p1[1])
        return [x, y]

    def clip_polygon_edge(subject_polygon, edge):
        clipped_polygon = []
        for i in range(len(subject_polygon)):
            p1 = subject_polygon[i - 1]
            p2 = subject_polygon[i]
            if inside(p2, edge):
                if not inside(p1, edge):
                    clipped_polygon.append(compute_intersection(p1, p2, edge))
                clipped_polygon.append(p2)
            elif inside(p1, edge):
                clipped_polygon.append(compute_intersection(p1, p2, edge))
        return clipped_polygon

    for edge in ["left", "right", "bottom", "top"]:
        subject_polygon = clip_polygon_edge(subject_polygon, edge)
    return subject_polygon

def main():
    pygame.init()
    display = (900, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-1, 1, -1, 1, -1, 1)

    # Define the vertices of the pentagon
    subject_polygon = [
        [-0.6, -0.2],
        [-0.2, 0.5],
        [0.2, 0.7],
        [0.6, 0.2],
        [0.2, -0.6]
    ]

    clipped_polygon = sutherland_hodgman_clip(subject_polygon, [
        [xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]
    ])

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

        # Draw the original pentagon
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for vertex in subject_polygon:
            glVertex2f(*vertex)
        glEnd()

        # Draw the clipped pentagon
        if clipped_polygon:
            glColor3f(0.0, 0.0, 1.0)
            glBegin(GL_LINE_LOOP)
            for vertex in clipped_polygon:
                glVertex2f(*vertex)
            glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()



