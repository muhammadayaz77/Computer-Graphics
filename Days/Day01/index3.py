from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glLineWidth(3)  # Set line width

    glBegin(GL_LINES)  # Start drawing lines
    glVertex2f(-0.5, -0.5)  # First point of the line (bottom-left)
    glVertex2f(0.5, 0.5)  # Second point of the line (top-right)
    glEnd()  # End drawing

    glutSwapBuffers()  # Swap buffers to display the line

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"OpenGL Line Drawing")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
