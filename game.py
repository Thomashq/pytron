from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from arena import Arena
from moto import Motorcycle

class Game:
    def __init__(self):
        self.arena = Arena()
        self.moto1 = Motorcycle(-10.0, 0.0, 0.0, (0.0, 0.0, 1.0))  # Moto azul
        self.moto2 = Motorcycle(10.0, 0.0, 0.0, (1.0, 1.0, 0.0))   # Moto verde
        self.keys = {}  # Dicionário para armazenar o estado das teclas
        self.game_paused = False  # Variável para pausar o jogo

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glFrontFace(GL_CCW) 

        # Ajuste a posição da luz para melhorar a iluminação
        light_position = [0.0, 50.0, 100.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        
        # Aumente a intensidade da luz difusa e especular
        diffuse_light = [0.7, 0.7, 0.7, 1.0]
        specular_light = [0.5, 0.5, 0.5, 1.0]
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
        
        # Luz ambiente mais baixa para criar um contraste com as luzes das motos e da arena
        ambient_light = [0.1, 0.1, 0.1, 1.0]
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light)

    def check_collisions(self):
        if not self.game_paused:  # Verificar colisões apenas se o jogo não estiver pausado
            for x, z in self.moto1.trail:
                if self.moto2.check_collision(x, z):
                    print("Moto2 colidiu com o rastro da Moto1!")
                    self.moto2.speed = 0

            for x, z in self.moto2.trail:
                if self.moto1.check_collision(x, z):
                    print("Moto1 colidiu com o rastro da Moto2!")
                    self.moto1.speed = 0

    def reshape(self, w, h):
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(w) / float(h), 0.1, 500.0)
        glMatrixMode(GL_MODELVIEW)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0.0, 50.0, 100.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        self.arena.draw()
        self.moto1.draw()
        self.moto2.draw()
        glutSwapBuffers()

    def update(self, value):
        if not self.game_paused:  # Atualizar apenas se o jogo não estiver pausado
            # Verifica o estado das teclas para moto1
            if self.keys.get(b'w'):
                self.moto1.accelerate()
            if self.keys.get(b's'):
                self.moto1.move_backwards()
            if self.keys.get(b'a'):
                self.moto1.turn_left()
            if self.keys.get(b'd'):
                self.moto1.turn_right()

            # Verifica o estado das teclas para moto2 (teclas especiais)
            if self.keys.get(GLUT_KEY_UP):
                self.moto2.accelerate()
            if self.keys.get(GLUT_KEY_DOWN):
                self.moto2.move_backwards()
            if self.keys.get(GLUT_KEY_LEFT):
                self.moto2.turn_left()
            if self.keys.get(GLUT_KEY_RIGHT):
                self.moto2.turn_right()
            
            self.check_collisions()
            # Atualiza a posição das motos
            self.moto1.update_position(self.arena.size)
            self.moto2.update_position(self.arena.size)
        
        glutPostRedisplay()
        glutTimerFunc(16, self.update, 0)

    def keyboard(self, key, x, y):
        self.keys[key] = True  # Marca a tecla como pressionada

    def keyboard_up(self, key, x, y):
        self.keys[key] = False  # Marca a tecla como liberada

    def special_input(self, key, x, y):
        self.keys[key] = True  # Marca tecla especial como pressionada

    def special_input_up(self, key, x, y):
        self.keys[key] = False  # Marca tecla especial como liberada

    def toggle_pause(self):
        self.game_paused = not self.game_paused
        if self.game_paused:
            print("Jogo pausado.")
        else:
            print("Jogo retomado.")

