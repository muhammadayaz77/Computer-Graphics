import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(xc, yc, radius, num_segments=100):
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta) + xc
        y = radius * math.sin(theta) + yc
        glVertex2f(x, y)
    glEnd()

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_bicycle():
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Wheels
    rear_wheel_x, rear_wheel_y = -0.6, -0.5
    front_wheel_x, front_wheel_y = 0.6, -0.5
    wheel_radius = 0.3

    draw_circle(rear_wheel_x, rear_wheel_y, wheel_radius)
    draw_circle(front_wheel_x, front_wheel_y, wheel_radius)

    # Spokes
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        for wheel_x, wheel_y in [(rear_wheel_x, rear_wheel_y), (front_wheel_x, front_wheel_y)]:
            spoke_x = wheel_x + wheel_radius * math.cos(rad)
            spoke_y = wheel_y + wheel_radius * math.sin(rad)
            draw_line(wheel_x, wheel_y, spoke_x, spoke_y)

    # Frame
    seat_post_x, seat_post_y = 0.0, 0.0
    top_tube_x, top_tube_y = 0.2, -0.1
    handlebar_x, handlebar_y = 0.5, -0.2

    draw_line(rear_wheel_x, rear_wheel_y, seat_post_x, seat_post_y)
    draw_line(seat_post_x, seat_post_y, front_wheel_x, front_wheel_y)
    draw_line(rear_wheel_x, rear_wheel_y, top_tube_x, top_tube_y)
    draw_line(top_tube_x, top_tube_y, front_wheel_x, front_wheel_y)
    draw_line(seat_post_x, seat_post_y, top_tube_x, top_tube_y)

    # Handlebars
    draw_line(front_wheel_x, front_wheel_y, handlebar_x, handlebar_y)
    draw_line(handlebar_x, handlebar_y, 0.7, -0.1)
    draw_line(handlebar_x, handlebar_y, 0.4, -0.1)

    # Pedals
    draw_circle(0.0, -0.2, 0.05)  
    draw_line(0.0, -0.2, -0.06, -0.28)
    draw_line(0.0, -0.2, 0.06, -0.12)

    # Seat
    draw_line(-0.05, 0.1, 0.05, 0.1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()  # Reset transformations before drawing
    draw_bicycle()
    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix
    aspect_ratio = width / height if height > 0 else 1
    if width >= height:
        glOrtho(-1.0 * aspect_ratio, 1.0 * aspect_ratio, -1.0, 1.0, -1.0, 1.0)
    else:
        glOrtho(-1.0, 1.0, -1.0 / aspect_ratio, 1.0 / aspect_ratio, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"PyOpenGL Bicycle")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)  
    glutMainLoop()

if __name__ == "__main__":
    main()
