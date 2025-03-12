import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(radius, num_segments):
    """
    Draw a circle centered at the origin using the parametric equations:
    
    - x = r * cos(θ)
    - y = r * sin(θ)
    
    where θ = (2π * i) / num_segments for each segment.
    """
    glBegin(GL_LINE_LOOP)  # Draw using line segments
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments  # Calculate angle
        x = radius * math.cos(theta)  # X coordinate
        y = radius * math.sin(theta)  # Y coordinate
        glVertex2f(x, y)  # Pass vertex to OpenGL
    glEnd()
    glFlush()  # Ensure rendering

def init():
    """Initialize OpenGL settings."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, 500, 500)  # Set viewport to match the window

def display():
    """OpenGL display function."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set drawing color to white
    draw_circle(0.5, 50000)  # Draw a circle with radius 0.5 and 100 segments

def main():
    """Initialize GLUT and run the OpenGL loop."""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffering with RGB mode
    glutInitWindowSize(500, 500)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position
    glutCreateWindow(b"OpenGL Circle")  # Create a window with a title
    init()  # Initialize OpenGL settings
    glutDisplayFunc(display)  # Register the display function
    glutMainLoop()  # Start the main loop

# Run the program
if __name__ == "__main__":
    main()
