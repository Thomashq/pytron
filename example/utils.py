from OpenGL.GL import *

def draw_cube(size):
    glBegin(GL_QUADS)
    # Face Frontal
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)

    # Face Traseira
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)
    glVertex3f(size, size, -size)
    glVertex3f(-size, size, -size)

    # Outras faces...
    glEnd()
