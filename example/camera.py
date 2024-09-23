from OpenGL.GL import *
from OpenGL.GLUT import *

class Camera:
    def __init__(self):
        self.position = [0.0, 5.0, -10.0]
        self.look_at = [0.0, 0.0, 0.0]

    def update(self, player_position):
        self.look_at = player_position
        glLoadIdentity()
        gluLookAt(self.position[0], self.position[1], self.position[2],
                  self.look_at[0], self.look_at[1], self.look_at[2],
                  0, 1, 0)
