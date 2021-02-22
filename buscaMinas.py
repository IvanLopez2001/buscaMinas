import pygame
from modelo.celda import Celda
from modelo.menu import Menu
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.
LEFT = 1
RIGHT = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Controlador():
    rect = pygame.Rect((0, 20), (20, 20))
    image = pygame.Surface((19, 19))
    image .fill(BLACK)  
    detalles = pygame.Surface((720, 20))
    detalles .fill(RED)
    def __init__(self):
        self.celda = Celda()
        self.menu = Menu()
        self.printMapa()
    def inicioJuego(self):
        self.menu.inicio()
    def printMapa(self):
        screen.fill(WHITE)
        self.celda.printearCuadros(screen, self.image)
        screen.blit(self.detalles, [0,0])
        pygame.display.update() #or pygame.display.flip()
        self.mainLoop()
    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    self.celda.consultaContenidos(pos, self.image)
                if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    pos = pygame.mouse.get_pos()
                    self.celda.mina(pos, self.image)
                    #self.celda.prueba(self.image, pos)
            pygame.display.update() #or pygame.display.flip()
if __name__ == "__main__":
    buscaMinas = Controlador()