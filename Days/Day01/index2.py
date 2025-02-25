from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

    glColor3f(1.0, 0.0, 0.0)  # Set color to red (RGB format)
    glPointSize(5)  # Set point size

    glBegin(GL_POINTS)  # Start drawing points
    glVertex2f(0.0, 0.0)  # Draw a point at the center of the window
    
    glEnd()  # End drawing

    glutSwapBuffers()  # Swap buffers to display the point

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"OpenGL Single Point")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main() 
