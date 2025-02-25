from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line():
    glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
    glPointSize(5)  # Set point size

    x1, y1 = -0.8, -0.8  # Start point (x1, y1)
    x2, y2 = 0.8, 0.8  # End point (x2, y2)

    m = (y2 - y1) / (x2 - x1)  # Calculate slope (m)
    c = y1 - m * x1  # Calculate intercept (c)

    glBegin(GL_POINTS)  # Start drawing points
    x = x1
    while x <= x2:  # Iterate through x values
        y = m * x + c  # Calculate y using y = mx + c
        glVertex2f(x, y)  # Plot point
        x += 0.01  # Increment x for smooth plotting
    glEnd()

    glFlush()  # Render everything

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line()  # Call the line drawing function
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"OpenGL Line Equation y=mx+c")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background to black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
