import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

def draw_rectangle(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def apply_transformation(vertices, matrix):
    transformed_vertices = []
    for vertex in vertices:
        vec = np.array([vertex[0], vertex[1], 1])
        transformed_vec = np.dot(matrix, vec)
        transformed_vertices.append(transformed_vec[:2])
    return transformed_vertices

def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotation_matrix(angle):
    rad = np.deg2rad(angle)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])

def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def reflection_matrix(axis):
    if axis == 'x':
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis == 'y':
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

def shearing_matrix(shx, shy):
    return np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])

def composite_transformations(vertices, transformations):
    composite_matrix = np.identity(3)
    for transformation in transformations:
        composite_matrix = np.dot(transformation, composite_matrix)
    return apply_transformation(vertices, composite_matrix)

def main():
    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-1080, 2160, -720, 1440, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    clock = pygame.time.Clock()

    # Define a simple rectangle shape
    rect_width, rect_height = 150, 150
    center_x, center_y = display[0] / 2, display[1] / 2
    rectangle = [
        [center_x - rect_width / 2, center_y - rect_height / 2],
        [center_x + rect_width / 2, center_y - rect_height / 2],
        [center_x + rect_width / 2, center_y + rect_height / 2],
        [center_x - rect_width / 2, center_y + rect_height / 2]
    ]

    transformations = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:  # Translation
                    tx, ty = 200, 150
                    transformations.append(translation_matrix(tx, ty))
                elif event.key == pygame.K_r:  # Rotation
                    angle = 30
                    transformations.append(rotation_matrix(angle))
                elif event.key == pygame.K_s:  # Scaling
                    sx, sy = 1.5, 1.5
                    transformations.append(scaling_matrix(sx, sy))
                elif event.key == pygame.K_x:  # Reflection across X-axis
                    transformations.append(reflection_matrix('x'))
                elif event.key == pygame.K_y:  # Reflection across Y-axis 
                    transformations.append(reflection_matrix('y'))
                elif event.key == pygame.K_h:  # Shearing
                    shx, shy = 0.5, 0
                    transformations.append(shearing_matrix(shx, shy))
                elif event.key == pygame.K_z:  # Composite Translate and Rotate
                    tx, ty = 200, 150
                    angle = 60
                    transformations.append(translation_matrix(-tx, -ty))
                    transformations.append(rotation_matrix(angle))
                    transformations.append(translation_matrix(tx, ty))
                elif event.key == pygame.K_c:  # Clear all transformations
                    transformations = []
        
        transformed_rectangle = composite_transformations(rectangle, transformations)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw original rectangle in white
        glColor3f(1.0, 1.0, 1.0)
        draw_rectangle(rectangle)
        # Draw transformed rectangle in green
        glColor3f(0.0, 1.0, 0.0)
        draw_rectangle(transformed_rectangle)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
