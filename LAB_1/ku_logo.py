import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Draw a circle with lines, filled with a triangle fan, and radial lines inside
def draw_circle2(center_x, center_y, radius, num_segments=20):
    
    #Number of line segments to approximate the circle. Default is 20.
    # Draw outer circle with lines
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
    # Draw radial lines inside the circle
    glLineWidth(4)
    num_lines = 12  # Number of radial lines
    for i in range(num_lines):
        line_angle = 2 * np.pi * i / num_lines
        x1 = center_x + radius * np.cos(line_angle)
        y1 = center_y + radius * np.sin(line_angle)
        x2 = center_x + radius * np.cos(line_angle + np.pi) # Opposite direction
        y2 = center_y + radius * np.sin(line_angle + np.pi)
        
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 0.0) 
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
    
def draw_circle1(center_x, center_y, radius, num_segments=100):
    
    glLineWidth(8)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.53, 0.81, 0.98)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_circle(center_x, center_y, radius, num_segments=100):
    
    glLineWidth(8)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
def draw_circle3(center_x, center_y, radius, num_segments=100):
    
    glLineWidth(8)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(num_segments):
        angle = 2 * np.pi * i / num_segments
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()


def draw_triangle(x1, y1, x2, y2, x3, y3, window_width, window_height, scale_factor):
    # Calculate the center of the window
    center_x = window_width / 2
    center_y = window_height / 2
    
    # Calculate the offset to move the triangle to the center of the window
    offset_x = center_x - (x1 + x2 + x3) / 3
    offset_y = center_y - (y1 + y2 + y3) / 3
    
    # Begin drawing the triangle
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f((x1 + offset_x) * scale_factor, (y1 + offset_y) * scale_factor)
    glVertex2f((x2 + offset_x) * scale_factor, (y2 + offset_y) * scale_factor)
    glVertex2f((x3 + offset_x) * scale_factor, (y3 + offset_y) * scale_factor)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.75, 0.8)
    glVertex2f((x1 + offset_x) * scale_factor, (y1 + offset_y) * scale_factor)
    glVertex2f((x2 + offset_x) * scale_factor, (y2 + offset_y) * scale_factor)
    glVertex2f((x3 + offset_x) * scale_factor, (y3 + offset_y) * scale_factor)
    glEnd()


def draw_mirror_triangle(x1, y1, x2, y2, x3, y3, window_width, window_height, scale_factor):
    glLineWidth(8)
    # Calculate the center of the window
    center_x = window_width / 2
    center_y = window_height / 2
    
    # Calculate the offset to move the triangle to the center of the window
    offset_x = center_x - (x1 + x2 + x3) / 3
    offset_y = center_y - (y1 + y2 + y3) / 3
    
    # Begin drawing the mirror triangle (upside-down)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f((x1 + offset_x) * scale_factor, window_height - (y1 + offset_y) * scale_factor)
    glVertex2f((x2 + offset_x) * scale_factor, window_height - (y2 + offset_y) * scale_factor)
    glVertex2f((x3 + offset_x) * scale_factor, window_height - (y3 + offset_y) * scale_factor)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f((x1 + offset_x) * scale_factor, window_height - (y1 + offset_y) * scale_factor)
    glVertex2f((x3 + offset_x) * scale_factor, window_height - (y3 + offset_y) * scale_factor)
    glVertex2f((x2 + offset_x) * scale_factor, window_height - (y2 + offset_y) * scale_factor)
    glEnd()



def draw_mirror_triangle1(x1, y1, x2, y2, x3, y3, window_width, window_height, scale_factor):
    
    glLineWidth(4)
    # Calculate the center of the window
    center_x = window_width / 2
    center_y = window_height / 2
    
    # Calculate the offset to move the triangle to the center of the window
    offset_x = center_x - (x1 + x2 + x3) / 3
    offset_y = center_y - (y1 + y2 + y3) / 3
    
    # Begin drawing the mirror triangle (upside-down)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f((x1 + offset_x) * scale_factor, window_height - (y1 + offset_y) * scale_factor)
    glVertex2f((x2 + offset_x) * scale_factor, window_height - (y2 + offset_y) * scale_factor)
    glVertex2f((x3 + offset_x) * scale_factor, window_height - (y3 + offset_y) * scale_factor)
    glEnd()
    
    
def draw_rectangle(x, y, width, height):
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 0.0)
    # Define vertices of the rectangle
    glVertex2f(x, y)            # Bottom-left vertex
    glVertex2f(x + width, y)    # Bottom-right vertex
    glVertex2f(x + width, y + height)  # Top-right vertex
    glVertex2f(x, y + height)   # Top-left vertex
    glEnd()
   
def draw_u_shape(x, y, width, height, space):
    glLineWidth(5)
    glPushMatrix()
    # Translate to the center of rotation, rotate, and then translate back
    glTranslatef(x + width / 2, y + height / 2, 0)
    glRotatef(55, 0, 0, 1)
    glTranslatef(-width / 2, -height / 2, 0)

    # Draw the bottom horizontal segment of the U shape
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    # Draw the upper horizontal segment of the U shape
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(x + width + space, y)
    glVertex2f(x + width + space + width, y)
    glVertex2f(x + width + space + width, y + height + 20)
    glVertex2f(x + width + space, y + height + 20)
    glEnd()

    # Draw the connecting vertical segment of the U shape
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(x, y + height + 20)
    glVertex2f(x + width + space + width, y + height + 20)
    glVertex2f(x + width + space + width, y + height)
    glVertex2f(x, y + height)
    glEnd()
    glPopMatrix()

# Class for rendering a KU (Kathmandu University) logo using OpenGL and Pygame.    
class KULogo():
    def __init__(self):
        
        #Initialize the KULogo object and create the Pygame display surface.
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
        self.clock = pygame.time.Clock()
        self.show_screen()
        
    def show_screen(self):
        # Main rendering loop to display the KU logo.
        glClearColor(1.0, 0.96, 1.0, 0.86)  # Set background color to a light shade of pink
        glOrtho(0, 1280, 720, 0, -1, 1)     # Set up orthographic projection

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            
            draw_circle2(640, 360, 300)           
            draw_circle1(640, 360, 250)        
            draw_circle(640, 360, 200)  
            
            draw_triangle(180, 120, 425, 120, 300, 308, 850, 500, 1.5)
            
            draw_mirror_triangle(198, 120, 404, 120, 300, 340, 850, 1500, 1.5)
            draw_mirror_triangle1(198, 120, 404, 120, 300, 340, 1280, 750, 1)
            
            draw_circle3(637, 170, 35)
            draw_circle3(485, 480, 35)
            draw_circle3(790, 480, 35)

            draw_rectangle(605,340,20,80)            
            draw_u_shape(416,5,20,30,20)
            
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == "__main__":
    KULogo()