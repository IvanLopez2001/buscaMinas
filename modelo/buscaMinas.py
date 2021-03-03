import pygame
from modelo.celda import Celda
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
class Buscaminas():
    rect = pygame.Rect((0, 20), (20, 20))
    image = pygame.Surface((19, 19))
    image .fill(BLACK)  
    detalles = pygame.Surface((720, 20))
    detalles .fill(RED)
    def __init__(self):
        screen.fill(WHITE)
        self.bBack = pygame.Surface((340, 40))
        self.bBack .fill(BLUE)
        self.celda = Celda()
        self.printMapa()
        self.printStats()
    def printStats(self):
        arial = pygame.font.SysFont("FrizQuadrata", 25)
        textoBack = arial.render("VOLVER AL MENU", True, WHITE)
        screen.blit(self.bBack , self.bBack.get_rect(center=(0,0)))
        screen.blit(textoBack, (10,2))
        self.mainLoop()

    def printMapa(self):
        self.celda.printearCuadros(screen, self.image)
        screen.blit(self.detalles, [0,0])
        pygame.display.update() #or pygame.display.flip()
    
    def volverMenu(self):
        return(1)

    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    backMenu =  self.bBack.get_rect(center=(0,0))
                    if backMenu.collidepoint(pos):
                        self.volverMenu()
                        return(1)
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    self.celda.consultaContenidos(pos, self.image)
                if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    pos = pygame.mouse.get_pos()
                    self.celda.mina(pos, self.image)
                    #self.celda.prueba(self.image, pos)
            pygame.display.update() #or pygame.display.flip()
