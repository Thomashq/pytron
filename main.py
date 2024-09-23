from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from arena import Arena
from moto import Motorcycle
from game import Game  # Supondo que a classe Game esteja em um arquivo separado

def main():
    game = Game()  # Inicializa o jogo

    # Inicializa a janela do OpenGL e define o título
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Jogo de Moto com Arena")

    # Inicializa o jogo (OpenGL e configurações)
    game.init()

    # Liga as funções de display e reshape
    glutDisplayFunc(game.draw)
    glutReshapeFunc(game.reshape)
    
    # Liga as funções de teclado para múltiplos inputs
    glutKeyboardFunc(game.keyboard)  # Teclas normais (moto1)
    glutKeyboardUpFunc(game.keyboard_up)  # Teclas normais ao soltar
    glutSpecialFunc(game.special_input)  # Teclas especiais (moto2)
    glutSpecialUpFunc(game.special_input_up)  # Teclas especiais ao soltar

    # Atualiza o estado do jogo
    glutTimerFunc(16, game.update, 0)

    # Inicia o loop principal do GLUT
    glutMainLoop()

if __name__ == "__main__":
    main()
