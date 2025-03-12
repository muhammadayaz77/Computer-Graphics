import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(cx, cy, radius, num_segments):
    """
    Draw a circle at a given position (cx, cy) with a specified radius.
    The circle is approximated using line segments.
    """
    glBegin(GL_LINE_LOOP)  # Draw using line segments
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments  # Calculate angle
        x = cx + radius * math.cos(theta)  # X coordinate with center offset
        y = cy + radius * math.sin(theta)  # Y coordinate with center offset
        glVertex2f(x, y)  # Define the vertex
    glEnd()
    glFlush()  # Ensure rendering

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set drawing color to white
    
    # Draw circles at different positions
    # draw_circle(-0.5, 0.5, 0.2, 50)  # Circle at (-0.5, 0.5)
    draw_circle(0.5, -0.5, 0.3, 50)  # Circle at (0.5, -0.5)
    # draw_circle(0.0, 0.0, 0.4, 50)  # Circle at the center

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circle at Any Position")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background color black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
