import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle_8way(cx, cy, radius, num_segments):
    """
    Draw a circle using 8-way symmetry centered at (cx, cy).
    """
    glBegin(GL_POINTS)  # Use points to draw the circle
    for i in range(num_segments // 8 + 1):  # Compute only one-eighth
        theta = (math.pi / 4) * (i / (num_segments / 8))  # Angle limited to 45 degrees
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        # 8-way symmetric points
        glVertex2f(cx + x, cy + y)  # (x, y)
        glVertex2f(cx + y, cy + x)  # (y, x)
        glVertex2f(cx - x, cy + y)  # (-x, y)
        glVertex2f(cx - y, cy + x)  # (-y, x)
        glVertex2f(cx - x, cy - y)  # (-x, -y)
        glVertex2f(cx - y, cy -x)   # (-y, -x)
        glVertex2f(cx + x, cy - y)  # (x, -y)
        glVertex2f(cx + y, cy - x)  # (y, -x)
    
    glEnd()
    glFlush()  # Render the points

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    
    draw_circle_8way(0.0, 0.0, 0.5, 100)  # Draw an 8-way symmetric circle at the center

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"8-Way Symmetric Circle")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
