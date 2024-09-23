import pygame
from OpenGL.GL import *

class Arena:
    def __init__(self):
        self.size = 10

    def draw(self):
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_LINES)
        for x in range(-self.size, self.size):
            glVertex3f(x, -1, -self.size)
            glVertex3f(x, -1, self.size)
        for z in range(-self.size, self.size):
            glVertex3f(-self.size, -1, z)
            glVertex3f(self.size, -1, z)
        glEnd()
