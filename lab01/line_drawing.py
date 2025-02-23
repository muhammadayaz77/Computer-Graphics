from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_point():
    glColor3f(1.0, 0.0, 0.0)  # Set point color to red
    glPointSize(20.0)  # Set the size of the point

    glBegin(GL_POINTS)  # Begin drawing points
    glVertex2f(0.0, 0.0)  # Draw a point at the center
    glEnd() 

    glFlush()  # Ensure execution of OpenGL commands

def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode
    glutInitWindowSize(500, 500)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position
    glutCreateWindow(b"OpenGL Point")  # Create window with title

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set coordinate system

    glutDisplayFunc(draw_point)  # Set display callback
    glutMainLoop()  # Start the main loop

if __name__ == "__main__":
    main()
