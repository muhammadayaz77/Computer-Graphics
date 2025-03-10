from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display(): 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

  # Draw a line
  glColor3f(1.0, 1.0, 1.0)  # Set the color to black
  glLineWidth(15)

  glBegin(GL_LINES)
  
  glVertex2f(-0.5, 0.5)
  glVertex2f(0.5, -0.5)
  glEnd()
  glColor3f(1.0, 1.0, 1.0)  # Set the color to black
  glLineWidth(15)

  glBegin(GL_LINES)
  
  glVertex2f(0.5, 0.5)
  glVertex2f(-0.5, -0.5)
  glEnd()
  glutSwapBuffers()  # Swap buffers to display the point


def main():
  glutInit()
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
  glutInitWindowSize(700, 700)
  glutCreateWindow(b"OpenGL Single Point")
  glClearColor(.0, .0, .0, 1.0)  # Set background color to black
  glutDisplayFunc(display)
  glutMainLoop()

if __name__ == "__main__":
  main()