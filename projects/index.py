import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(xc, yc, radius, num_segments=100):
    """Draws a circle at (xc, yc) with given radius."""
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta) + xc
        y = radius * math.sin(theta) + yc
        glVertex2f(x, y)
    glEnd()

def draw_line(x1, y1, x2, y2):
    """Draws a line from (x1, y1) to (x2, y2)."""
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_oval(xc, yc, rx, ry, num_segments=100):
    """Draws an oval at (xc, yc) with given radii."""
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = rx * math.cos(theta) + xc
        y = ry * math.sin(theta) + yc
        glVertex2f(x, y)
    glEnd()

def draw_bicycle():
    """Draws a properly proportioned bicycle using OpenGL."""
    glColor3f(1.0, 1.0, 1.0)
    
    # Draw wheels
    rear_wheel_center = (-0.5, -0.5)
    front_wheel_center = (0.5, -0.5)
    wheel_radius = 0.3
    draw_circle(*rear_wheel_center, wheel_radius)  
    draw_circle(*front_wheel_center, wheel_radius)  
    
    # Draw wheel spokes
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        for center in [rear_wheel_center, front_wheel_center]:
            draw_line(center[0], center[1], 
                      center[0] + wheel_radius * math.cos(rad), 
                      center[1] + wheel_radius * math.sin(rad))

    # Frame adjustments
    seat_post = (0.0, 0.0)
    top_tube = (0.2, -0.1)
    handlebar_post = (0.4, -0.2)

    draw_line(*rear_wheel_center, *seat_post)   # Rear wheel to seat post
    draw_line(*seat_post, *front_wheel_center)  # Seat post to front wheel
    draw_line(*rear_wheel_center, *top_tube)    # Rear wheel to top tube
    draw_line(*top_tube, *front_wheel_center)   # Top tube to front wheel
    draw_line(*seat_post, *top_tube)            # Seat post to top tube

    # Handlebars - fixed unpacking issue
    draw_line(*front_wheel_center, *handlebar_post)
    draw_line(handlebar_post[0], handlebar_post[1], 0.6, -0.1)
    draw_line(handlebar_post[0], handlebar_post[1], 0.3, -0.1)

    # Pedals - refined shape
    draw_circle(0.0, -0.2, 0.05)  # Center crank
    draw_line(0.0, -0.2, -0.06, -0.28)
    draw_line(0.0, -0.2, 0.06, -0.12)

    # Seat - better alignment
    draw_oval(0.0, 0.1, 0.12, 0.04)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_bicycle()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Fixed Bicycle Drawing")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
