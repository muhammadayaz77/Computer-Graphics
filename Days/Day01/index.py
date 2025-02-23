from OpenGL.GL import *  # Import OpenGL functions
from OpenGL.GLUT import *  # Import GLUT for window management
from OpenGL.GLU import *  # Import GLU for OpenGL utilities

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
    glutSwapBuffers()  # Swap buffers to display the screen

def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set display mode (double buffering, RGB)
    glutInitWindowSize(700, 700)  # Set window size
    glutCreateWindow(b"OpenGL Blank Screen")  # Create a window with a title
    glClearColor(1.0, 0.0, 0.0, 0.0)  # Set background color to black
    glutDisplayFunc(display)  # Register the display function
    glutMainLoop()  # Start the main loop

if __name__ == "__main__":
    main()  # Run the program
