import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(radius, num_segments):
   
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        angle = 2.0 * math.pi * i / num_segments  # Angle for this vertex
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        angle = 2.0 * math.pi * i / num_segments  # Calculate the angle for this vertex (angle = 2πi / num_segments)
        x = radius * math.cos(angle)  # Calculate the x coordinate (x = radius * cos(angle))
        y = radius * math.sin(angle)  # Calculate the y coordinate (y = radius * sin(angle))
        glVertex2f(x, y)  # Specify the vertex
    glEnd()
    glFlush()  # Render the circle

def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background color (black)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle(0.5, 100)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circle")
    setup()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()