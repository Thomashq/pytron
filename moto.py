from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Motorcycle:
    def __init__(self, x, y, z, color):
        # Atributos de material
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.speed = 0.0
        self.direction = 0.0
        self.max_speed = 0.7
        self.acceleration_rate = 0.01
        self.rotation_speed = 1.5
        self.backwards_speed = -0.5
        self.trail = [(x, z)]
        self.trail_length = 150

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.direction, 0.0, 1.0, 0.0)
        
        # Definir as propriedades do material da motocicleta
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (*self.color, 1.0))  # Cor da moto
        glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))  # Componente especular branca
        glMaterialf(GL_FRONT, GL_SHININESS, 32.0)  # Brilho da especularidade

        # Desenhar a moto como um triângulo (frente da moto em +Z)
        glBegin(GL_TRIANGLES)
        
        # Frente da moto
        glNormal3f(0.0, 1.0, 0.0)  # Normal apontando para cima
        glVertex3f(0.0, 0.0, 1.5)  # Frente
        
        # Traseira esquerda
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, 0.0, -1.0)
        
        # Traseira direita
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 0.0, -1.0)
        
        glEnd()
        glPopMatrix()

        # Desenhar o rastro
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in range(1, len(self.trail)):
            x1, z1 = self.trail[i - 1]
            x2, z2 = self.trail[i]

            # Desenhar o rastro como uma parede vertical
            glVertex3f(x1, 0.0, z1)
            glVertex3f(x2, 0.0, z2)
            glVertex3f(x2, 0.5, z2)  # Altura da parede
            glVertex3f(x1, 0.5, z1)
        glEnd()


    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += self.acceleration_rate

    def brake(self):
        if self.speed > 0:
            self.speed -= self.acceleration_rate
        elif self.speed < 0:
            self.speed = 0

    def move_backwards(self):
        if self.speed > self.backwards_speed:
            self.speed -= self.acceleration_rate

    def turn_left(self):
        self.direction += self.rotation_speed

    def turn_right(self):
        self.direction -= self.rotation_speed

    def update_position(self, arena_size):
        rad = math.radians(self.direction)

        # Atualizar a posição com base na velocidade e direção
        self.x += self.speed * math.sin(rad)
        self.z += self.speed * math.cos(rad)

        # Adicionar a nova posição ao rastro (da traseira da moto)
        if self.speed != 0:
            back_x = self.x - 1.5 * math.sin(rad)  # Calcula a posição da traseira da moto
            back_z = self.z - 1.5 * math.cos(rad)
            self.trail.append((back_x, back_z))

        # Limitar o tamanho do rastro
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)

        # Reduz a velocidade suavemente
        self.speed *= 0.98

        # Limites da arena com margens
        margin = 5.0
        if self.x < -arena_size + margin:
            self.x = -arena_size + margin
            self.speed = 0
        elif self.x > arena_size - margin:
            self.x = arena_size - margin
            self.speed = 0

        if self.z < -arena_size + margin:
            self.z = -arena_size + margin
            self.speed = 0
        elif self.z > arena_size - margin:
            self.z = arena_size - margin
            self.speed = 0

        # Verificar colisão com o rastro
        if self.check_collision(self.x, self.z):
            print("Colisão com o rastro!")

    def check_collision(self, x, z):
        # Checa colisão com o próprio rastro
        for tx, tz in self.trail[:-10]:  # Ignorar as últimas posições recentes para evitar colisão imediata
            if abs(x - tx) < 0.5 and abs(z - tz) < 0.5:
                return True
        return False
