from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import Game

class Menu:
    def __init__(self):
        self.game = Game()  # Instancia o jogo

    def menu_handler(self, option):
        if option == 0:
            print("Iniciar o jogo")
            if self.game.game_paused:  # Despausa apenas se estiver pausado
                self.game.toggle_pause()
        elif option == 1:
            print("Pausar o jogo")
            if not self.game.game_paused:  # Pausa apenas se não estiver pausado
                self.game.toggle_pause()
        elif option == 2:
            print("Sair do jogo")
            glutLeaveMainLoop()  # Finaliza o loop principal do OpenGL

    def create_menu(self):
        glutCreateMenu(self.menu_handler)
        glutAddMenuEntry("Iniciar Jogo", 0)
        glutAddMenuEntry("Pausar Jogo", 1)
        glutAddMenuEntry("Sair", 2)
        glutAttachMenu(GLUT_RIGHT_BUTTON)  # Exibe o menu no botão direito do mouse

    def start_game(self):
        # Inicializa a janela do OpenGL e define o título
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow(b"Tron Lightcycle")

        # Inicializa o jogo (OpenGL e configurações)
        self.game.init()

        # Liga as funções de display e reshape
        glutDisplayFunc(self.game.draw)
        glutReshapeFunc(self.game.reshape)

        # Liga as funções de teclado para múltiplos inputs
        glutKeyboardFunc(self.game.keyboard)  # Teclas normais (moto1)
        glutKeyboardUpFunc(self.game.keyboard_up)  # Teclas normais ao soltar
        glutSpecialFunc(self.game.special_input)  # Teclas especiais (moto2)
        glutSpecialUpFunc(self.game.special_input_up)  # Teclas especiais ao soltar

        # Cria o menu (chamado ANTES do loop principal)
        self.create_menu()

        # Atualiza o estado do jogo
        glutTimerFunc(16, self.game.update, 0)

        # Inicia o loop principal do GLUT
        glutMainLoop()

if __name__ == "__main__":
    menu = Menu()
    menu.start_game()

