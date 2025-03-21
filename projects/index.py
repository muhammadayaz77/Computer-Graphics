from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

global cycle_x, pedal_angle
cycle_x = -100
pedal_angle = 0

def draw_pixel(x, y, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def midpoint_circle(xc, yc, r, color):
    x, y = 0, r
    p = 1 - r
    while x <= y:
        for dx, dy in [(x, y), (y, x), (-x, y), (-y, x), 
        (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            draw_pixel(xc + dx, yc + dy, *color)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

def dda(x1, y1, x2, y2, color):
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    for _ in range(int(steps) + 1):
        draw_pixel(round(x), round(y), *color)
        x += x_inc
        y += y_inc

def draw_wheel_lines(xc, yc, r, color):
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x = xc + r * math.cos(rad)
        y = yc + r * math.sin(rad)
        dda(xc, yc, x, y, color)

def draw_pedals(xc, yc, r, color):
    global pedal_angle
    pedal_rad = math.radians(-pedal_angle)
    
    # Calculate pedal positions (reversed direction)
    pedal_x1 = xc - r * math.cos(pedal_rad)  # Reversed direction
    pedal_y1 = yc - r * math.sin(pedal_rad)  # Reversed direction
    pedal_x2 = xc + r * math.cos(pedal_rad)  # Reversed direction
    pedal_y2 = yc + r * math.sin(pedal_rad)  # Reversed direction
    
    # Draw pedal arms
    dda(xc, yc, pedal_x1, pedal_y1, color)
    dda(xc, yc, pedal_x2, pedal_y2, color)
    
    # Draw rectangular pedal bodies
    pedal_width = 10
    pedal_height = 5
    
    # Pedal 1
    dda(pedal_x1 - pedal_width // 2, pedal_y1 - pedal_height // 2, 
        pedal_x1 + pedal_width // 2, pedal_y1 - pedal_height // 2, color)
    dda(pedal_x1 + pedal_width // 2, pedal_y1 - pedal_height // 2, 
        pedal_x1 + pedal_width // 2, pedal_y1 + pedal_height // 2, color)
    dda(pedal_x1 + pedal_width // 2, pedal_y1 + pedal_height // 2, 
        pedal_x1 - pedal_width // 2, pedal_y1 + pedal_height // 2, color)
    dda(pedal_x1 - pedal_width // 2, pedal_y1 + pedal_height // 2, 
        pedal_x1 - pedal_width // 2, pedal_y1 - pedal_height // 2, color)
    
    # Pedal 2
    dda(pedal_x2 - pedal_width // 2, pedal_y2 - pedal_height // 2, 
        pedal_x2 + pedal_width // 2, pedal_y2 - pedal_height // 2, color)
    dda(pedal_x2 + pedal_width // 2, pedal_y2 - pedal_height // 2, 
        pedal_x2 + pedal_width // 2, pedal_y2 + pedal_height // 2, color)
    dda(pedal_x2 + pedal_width // 2, pedal_y2 + pedal_height // 2, 
        pedal_x2 - pedal_width // 2, pedal_y2 + pedal_height // 2, color)
    dda(pedal_x2 - pedal_width // 2, pedal_y2 + pedal_height // 2, 
        pedal_x2 - pedal_width // 2, pedal_y2 - pedal_height // 2, color)
    
    # Draw pedal grips (small circles at the ends)
    midpoint_circle(pedal_x1, pedal_y1, 3, color)
    midpoint_circle(pedal_x2, pedal_y2, 3, color)

def draw_cycle():
    global cycle_x
    glClear(GL_COLOR_BUFFER_BIT)
    
    midpoint_circle(cycle_x - 60, -50, 40, (1, 0, 0))  # Rear Wheel
    midpoint_circle(cycle_x + 60, -50, 40, (0, 1, 0))  # Front Wheel
    draw_wheel_lines(cycle_x - 60, -50, 40, (0, 1, 0))
    draw_wheel_lines(cycle_x + 60, -50, 40, (1, 0, 0))
    
    dda(cycle_x - 60, -50, cycle_x, 20, (0.8, 0.5, 0.5))  # Rear Frame
    dda(cycle_x, 20, cycle_x + 60, -50, (0.8, 0.5, 0.5))  # Front Frame
    dda(cycle_x - 60, -50, cycle_x + 60, -50, (0.8, 0.5, 0.5))  # Bottom Bar
    
    dda(cycle_x, 20, cycle_x, 30, (0.8, 0.5, 0.5))  # Lowered Seat Post
    dda(cycle_x - 15, 30, cycle_x + 15, 30, (1, 0.5, 0))  # Lowered Seat
    
    dda(cycle_x + 60, -50, cycle_x + 80, 30, (0.8, 0.5, 0.5))  # Raised Handle Bar
    dda(cycle_x + 80, 30, cycle_x + 60, 40, (0.8, 0.5, 0.5))
    dda(cycle_x + 80, 30, cycle_x + 100, 30, (0.8, 0.5, 0.5))  # Raised Handle Extension
    
    midpoint_circle(cycle_x, -50, 10, (1, 1, 1))  # Pedal Center
    draw_pedals(cycle_x, -50, 15, (1, 1, 0))  # Pedals
    
    glFlush()

def update(value):
    global cycle_x, pedal_angle
    cycle_x += 2  # Move the cycle forward
    pedal_angle = (pedal_angle + 10) % 360  # Rotate pedals forward
    if cycle_x > 100:
        cycle_x = -100
    glutPostRedisplay()
    glutTimerFunc(50, update, 0)

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-120, 120, -100, 100)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Animated Cycle with Improved Shape")
glutDisplayFunc(draw_cycle)
glutTimerFunc(50, update, 0)
init()
glutMainLoop()









