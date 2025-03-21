from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

i = -1.0  # Initial x-position of the bicycle

def draw_circle(x, y, radius, num_segments=100):
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        glVertex2f(x + radius * math.cos(theta), y + radius * math.sin(theta))
    glEnd()

def draw_bicycle(x):
    glColor3f(1.0, 1.0, 1.0)  # White color for the frame
    glBegin(GL_LINES)
    
    # Frame
    glVertex2f(x - 0.4, -0.2)
    glVertex2f(x + 0.4, -0.2)
    
    glVertex2f(x - 0.4, -0.2)
    glVertex2f(x - 0.1, 0.2)
    
    glVertex2f(x + 0.4, -0.2)
    glVertex2f(x + 0.1, 0.2)
    
    glVertex2f(x - 0.1, 0.2)
    glVertex2f(x + 0.1, 0.2)
    
    # Handlebars
    glVertex2f(x + 0.1, 0.2)
    glVertex2f(x + 0.25, 0.3)
    
    glVertex2f(x + 0.25, 0.3)
    glVertex2f(x + 0.2, 0.35)
    
    # Seat
    glVertex2f(x - 0.1, 0.2)
    glVertex2f(x - 0.2, 0.25)
    
    glVertex2f(x - 0.2, 0.25)
    glVertex2f(x - 0.05, 0.25)
    glEnd()
    
    # Wheels (Increased size)
    glColor3f(0.0, 0.0, 1.0)  # Blue wheels
    draw_circle(x - 0.4, -0.4, 0.15)  # Rear wheel
    draw_circle(x + 0.4, -0.4, 0.15)  # Front wheel
    
    # Rims
    glColor3f(1.0, 1.0, 1.0)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        glBegin(GL_LINES)
        glVertex2f(x - 0.4, -0.4)
        glVertex2f(x - 0.4 + 0.15 * math.cos(rad), -0.4 + 0.15 * math.sin(rad))
        glEnd()
        
        glBegin(GL_LINES)
        glVertex2f(x + 0.4, -0.4)
        glVertex2f(x + 0.4 + 0.15 * math.cos(rad), -0.4 + 0.15 * math.sin(rad))
        glEnd()
    
    # Pedals
    glColor3f(1.0, 1.0, 1.0)
    draw_circle(x, -0.2, 0.06)
    glBegin(GL_LINES)
    glVertex2f(x, -0.14)
    glVertex2f(x, -0.26)
    glVertex2f(x - 0.06, -0.2)
    glVertex2f(x + 0.06, -0.2)
    glEnd()

def display():
    global i
    glClear(GL_COLOR_BUFFER_BIT)
    draw_bicycle(i)
    glutSwapBuffers()

def update(value):
    global i
    i += 0.01  # Move the bicycle to the right
    if i > 1.2:  # Reset position when it reaches the right edge
        i = -1.2
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Approximately 60 FPS

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Moving Bicycle Animation")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-1, 1, -1, 1, -1, 1)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
