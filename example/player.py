from OpenGL.GL import *
from utils import draw_cube

class Player:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.direction = [1.0, 0.0, 0.0]
        self.speed = 0.1
        self.size = 0.2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position[2] -= self.speed
        if keys[pygame.K_s]:
            self.position[2] += self.speed
        if keys[pygame.K_a]:
            self.position[0] -= self.speed
        if keys[pygame.K_d]:
            self.position[0] += self.speed

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glColor3f(0.0, 1.0, 1.0)
        draw_cube(self.size)
        glPopMatrix()
