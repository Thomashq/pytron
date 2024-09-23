from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Arena:
    def __init__(self):
        self.size = 50.0  # Define o tamanho da arena

    def draw(self):
        # Ativar o blending para suportar transparência (se necessário para outros elementos)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Desenhar o chão da arena com estilo Tron (grade brilhante)
        glColor3f(0.0, 0.0, 1.0)  # Cor azul neon para as linhas
        glLineWidth(2.0)  # Define a largura das linhas
        
        glBegin(GL_LINES)
        step = 5.0  # Define o espaçamento da grade
        
        for i in range(-int(self.size), int(self.size)+1, int(step)):
            # Linhas paralelas ao eixo X
            glVertex3f(i, -1.0, -self.size)
            glVertex3f(i, -1.0, self.size)
            
            # Linhas paralelas ao eixo Z
            glVertex3f(-self.size, -1.0, i)
            glVertex3f(self.size, -1.0, i)
        
        glEnd()

        # Desenhar as paredes ao redor da arena (exceto a parede traseira)
        glColor3f(0.0, 0.5, 1.0)  # Azul mais escuro para as paredes
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
