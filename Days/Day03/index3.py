import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle_4way(cx, cy, radius, num_segments):
    """
    Draw a circle using 4-way symmetry centered at (cx, cy).
    """
    glBegin(GL_POINTS)  # Use points to draw
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments  # Compute angle
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        # 4-way symmetric points
        glVertex2f(cx + x, cy + y)  # (x, y)
        glVertex2f(cx - x, cy + y)  # (-x, y)
        glVertex2f(cx + x, cy - y)  # (x, -y)
        glVertex2f(cx - x, cy - y)  # (-x, -y)
    
    glEnd()
    glFlush()  # Render the points

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    
    draw_circle_4way(0.0, 0.0, 0.5, 10)  # Draw a symmetric circle at the center

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"4-Way Symmetric Circle")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
