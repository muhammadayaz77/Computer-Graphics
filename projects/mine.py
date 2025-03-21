from OpenGL.GL import *  # Import OpenGL functions
from OpenGL.GLUT import *  # Import GLUT for window management
from OpenGL.GLU import *  # Import GLU for OpenGL utilities
import math


# x = cx + radius * cos(theta)
# y = cy + radius * sin(theta)
# theta = 2 pi * i / num_segments
def draw_circle(cx,cy,radius,num_segments):
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments): 
        theta = 2.0 * math.pi * i / (num_segments)
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)

        glVertex(x,y)

    glEnd()
    glFlush()


# y = mx*c
# c = y1 - m * x1
def draw_line(x1,y1,x2,y2):
    glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
    glPointSize(2)  # Set point size


    m = (y2 - y1) / (x2 - x1)  # Calculate slope (m)
    c = y1 - m * x1  # Calculate intercept (c)

    glBegin(GL_POINTS)  # Start drawing points
    x = x1
    while x <= x2 :  # Iterate through x values
        y = m * x + c  # Calculate y using y = mx + c
        glVertex2f(x, y)  # Plot point
        x += 0.0001  # Increment x for smooth plotting
    glEnd()

    glFlush()  # Render everything


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

    # ------------(CIRCLE SECTION)---------------
    # fRONT wheel 
    draw_circle(-0.50,0.0,0.2,100)
    draw_circle(-0.50,0.0,0.01,100)


    # BACK wheel
    draw_circle(0.50,0.0,0.2,100)
    draw_circle(0.50,0.0,0.01,100)

    # MIDDLE
    draw_circle(0.0,0.0,0.1,100)
    draw_circle(0.0,0.0,0.01,100)


    # ------------(LINE SECTION)---------------

    # front wheel , lines
    draw_line(-0.50,0.0,-0.40,0.17)
    draw_line(-0.50,0.0,-0.30,0.37)


    glutSwapBuffers()  # Swap buffers to display the screen

def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set display mode (double buffering, RGB)
    glutInitWindowSize(700, 700)  # Set window size
    glutCreateWindow(b"OpenGL Blank Screen")  # Create a window with a title
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black
    glutDisplayFunc(display)  # Register the display function
    glutMainLoop()  # Start the main loop

if __name__ == "__main__":
    main()  # Run the program
