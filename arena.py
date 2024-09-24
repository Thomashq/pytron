from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Arena:
    def __init__(self):
        self.size = 50.0  # Define o tamanho da arena

    def draw(self):
    # Ativar o blending (se necessário para elementos com transparência)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Definir material do chão da arena
        self.set_floor_material()

        # Desenhar o chão da arena (grade brilhante)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        step = 5.0  # Define o espaçamento da grade
        
        for i in range(-int(self.size), int(self.size)+1, int(step)):
            # Linhas paralelas ao eixo Y
            glVertex3f(i, -1.0, -self.size)
            glVertex3f(i, -1.0, self.size)
            
            # Linhas paralelas ao eixo X
            glVertex3f(-self.size, -1.0, i)
            glVertex3f(self.size, -1.0, i)
        
        glEnd()

        # Definir material das paredes da arena
        self.set_wall_material()

        # Desenhar as paredes ao redor da arena
        glBegin(GL_QUADS)
        
        # Parede frontal
        glVertex3f(-self.size, -1.0, -self.size)
        glVertex3f(self.size, -1.0, -self.size)
        glVertex3f(self.size, 20.0, -self.size)
        glVertex3f(-self.size, 20.0, -self.size)

        # Parede esquerda
        glVertex3f(-self.size, -1.0, -self.size)
        glVertex3f(-self.size, -1.0, self.size)
        glVertex3f(-self.size, 20.0, self.size)
        glVertex3f(-self.size, 20.0, -self.size)

        # Parede direita
        glVertex3f(self.size, -1.0, -self.size)
        glVertex3f(self.size, -1.0, self.size)
        glVertex3f(self.size, 20.0, self.size)
        glVertex3f(self.size, 20.0, -self.size)
        
        glEnd()

        # Desativar blending após desenhar
        glDisable(GL_BLEND)
    
    # Definir material da arena (piso)
    def set_floor_material(self):
        ambient = [0.0, 0.0, 0.3, 1.0]  # Azul escuro para a luz ambiente
        diffuse = [0.0, 0.0, 1.0, 1.0]  # Azul neon para a luz difusa
        specular = [0.5, 0.5, 0.5, 1.0]  # Reflexo especular
        shininess = [50.0]  # Brilho

        glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

    # Definir material das paredes
    def set_wall_material(self):
        ambient = [0.0, 0.25, 0.5, 1.0]  # Azul escuro para as paredes
        diffuse = [0.0, 0.5, 1.0, 1.0]  # Azul claro para a luz difusa nas paredes
        specular = [0.5, 0.5, 0.5, 1.0]  # Reflexo especular
        shininess = [30.0]  # Brilho moderado

        glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, shininess)


