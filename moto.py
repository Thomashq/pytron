from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Motorcycle:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.speed = 0.0
        self.direction = 0.0  # Ângulo de direção (em graus)
        self.max_speed = 1.0  # Reduzi a velocidade máxima
        self.acceleration_rate = 0.02  # Reduzi a taxa de aceleração
        self.rotation_speed = 1.5  # Taxa de rotação mais suave
        self.backwards_speed = -0.5  # Reduzi a velocidade máxima ao andar para trás
        self.trail = []
        
    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.direction, 0.0, 1.0, 0.0)  # Rotaciona a moto na direção correta
        glColor3f(*self.color)

        # Desenhar a moto como um triângulo isósceles com normais para iluminação
        glBegin(GL_TRIANGLES)
        
        # Definir a normal para a face do triângulo
        glNormal3f(0.0, 1.0, 0.0)
        
        # Vértices do triângulo
        glVertex3f(0.0, 0.0, 1.5)  # Ponta do triângulo (frente da moto)
        glVertex3f(-1.0, 0.0, -1.0)  # Lado esquerdo da base
        glVertex3f(1.0, 0.0, -1.0)  # Lado direito da base
        glEnd()

        glPopMatrix()

        # Desenhar o rastro
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in range(1, len(self.trail)):
            x1, z1 = self.trail[i - 1]
            x2, z2 = self.trail[i]
            
            # Desenhar o rastro como um quadrado vertical
            glVertex3f(x1, 0.0, z1)
            glVertex3f(x2, 0.0, z2)
            glVertex3f(x2, 1.0, z2)  # Altura da parede do rastro
            glVertex3f(x1, 1.0, z1)
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

        # Atrito natural para desacelerar a moto gradualmente quando não está acelerando
        self.speed *= 0.98  # Reduz a velocidade suavemente

        # Limites da arena com margens para evitar colisão imediata
        margin = 5.0
        if self.x < -arena_size + margin:
            self.x = -arena_size + margin
            self.speed = 0  # Parar a moto na colisão
            # Aqui pode-se adicionar lógica de 'game over'
        elif self.x > arena_size - margin:
            self.x = arena_size - margin
            self.speed = 0

        if self.z < -arena_size + margin:
            self.z = -arena_size + margin
            self.speed = 0
        elif self.z > arena_size - margin:
            self.z = arena_size - margin
            self.speed = 0

    def check_collision(self, x, z):
        # Checa colisão com o próprio rastro
        for tx, tz in self.trail[:-1]:  # Ignora a última posição para não detectar a moto em si
            if abs(x - tx) < 0.5 and abs(z - tz) < 0.5:
                return True
        return False