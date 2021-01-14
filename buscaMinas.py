import pygame
from modelo.celda import Celda
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Controlador():
    rect = pygame.Rect((0, 20), (20, 20))
    image = pygame.Surface((19, 19))
    image .fill(BLACK)  
    menu = pygame.Surface((720, 20))
    menu .fill(RED)
    def __init__(self):
        self.celda = Celda()
        self.printMapa()
    def printMapa(self):
        screen.fill(WHITE)
        self.celda.printearCuadros(screen, self.image)
        screen.blit(self.menu, [0,0])
        pygame.display.update() #or pygame.display.flip()
        self.mainLoop()
    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.celda.consultaContenidos(pos, self.image)
                    #self.celda.prueba(self.image, pos)
            pygame.display.update() #or pygame.display.flip()
if __name__ == "__main__":
    buscaMinas = Controlador()