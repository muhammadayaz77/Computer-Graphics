from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line():
    glColor3f(1.0, 0.0, 1.0)  # Set color to purple
    glPointSize(4)  # Set point size

    glBegin(GL_POINTS)  # Start drawing points
    for i in range(0, 50):  # Loop for multiple points
        glVertex2f(0.02 * i - 0.5, 0.02 * i - 0.5)  # Creating a line with small increments
    glEnd()

    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line()  # Call the function to draw the line
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"OpenGL Line with GL_POINTS")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background to black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
