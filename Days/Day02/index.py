from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define start and end points
x1, y1 = -0.8, -0.5  # Start point
x2, y2 = 0.8, 0.5    # End point

def draw_dda_line():
    glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
    glPointSize(3)            # Set point size

    # Compute dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps
    steps = max(abs(dx), abs(dy)) * 100  # Multiply by 100 for smooth rendering

    # Compute increments
    x_increment = dx / steps
    y_increment = dy / steps

    # Start at the initial point
    x, y = x1, y1

    glBegin(GL_POINTS)  # Use points to draw the line pixel by pixel

    for _ in range(int(steps) + 1):  # Iterate through steps
        glVertex2f(x, y)  # Plot the next point
        x += x_increment  # Update x
        y += y_increment  # Update y

    glEnd()
    glFlush()  # Render the drawing

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
    draw_dda_line()  # Call the function to draw the line
    glutSwapBuffers()  # Swap buffers for smooth rendering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)  # Window size
    glutCreateWindow(b"DDA Line Algorithm")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background to black
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
