import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from player import Player
from arena import Arena
from camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Tron Light Cycles")

        # Configurações OpenGL
        glEnable(GL_DEPTH_TEST)

        # Inicializando o jogo
        self.clock = pygame.time.Clock()
        self.arena = Arena()
        self.player = Player()
        self.camera = Camera()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Atualizar jogador e câmera
            self.player.update()
            self.camera.update(self.player.position)

            # Limpar a tela
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Renderizar o jogo
            self.arena.draw()
            self.player.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
