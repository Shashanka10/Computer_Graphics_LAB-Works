import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

def draw_cube():
    vertices = [
        [0.5, 0.5, -0.5],
        [0.5, -0.5, -0.5],
        [-0.5, -0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
        [0.5, -0.5, 0.5],
        [-0.5, -0.5, 0.5],
        [-0.5, 0.5, 0.5]
    ]
    
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def rotation_matrix_x(angle):
    rad = np.deg2rad(angle)
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_y(angle):
    rad = np.deg2rad(angle)
    return np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(angle):
    rad = np.deg2rad(angle)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def shearing_matrix(shxy, shxz, shyx, shyz, shzx, shzy):
    return np.array([
        [1, shxy, shxz, 0],
        [shyx, 1, shyz, 0],
        [shzx, shzy, 1, 0],
        [0, 0, 0, 1]
    ])

def composite_transformations(matrix, transformations):
    for transformation in transformations:
        matrix = np.dot(transformation, matrix)
    return matrix

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    transformations = []
    rotation_x, rotation_y = 0, 0
    running = True
    clock = pygame.time.Clock()
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:  # Translation
                    tx, ty, tz = 0.5, 0.5, 0.5
                    transformations.append(translation_matrix(tx, ty, tz))
                elif event.key == pygame.K_r:  # Rotation around Y-axis
                    angle = 30
                    transformations.append(rotation_matrix_y(angle))
                elif event.key == pygame.K_s:  # Scaling
                    sx, sy, sz = 1.5, 1.5, 1.5
                    transformations.append(scaling_matrix(sx, sy, sz))
                elif event.key == pygame.K_h:  # Shearing
                    shxy, shxz, shyx, shyz, shzx, shzy = 0.5, 0, 0, 0.5, 0, 0
                    transformations.append(shearing_matrix(shxy, shxz, shyx, shyz, shzx, shzy))
                elif event.key == pygame.K_c:  # Clear all transformations
                    transformations = []

        dx, dy = pygame.mouse.get_rel()
        rotation_x += dy * 0.1
        rotation_y += dx * 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Apply mouse rotation
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        # Draw original cube (constant shape)
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        draw_cube()
        glPopMatrix()

        # Apply composite transformations
        glPushMatrix()
        matrix = np.identity(4)
        matrix = composite_transformations(matrix, transformations)
        glMultMatrixf(matrix.T)

        # Draw transformed cube
        glColor3f(1.0, 0.0, 0.0)  # Change color to distinguish from original
        draw_cube()
        glPopMatrix()
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
