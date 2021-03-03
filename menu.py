import pygame
from modelo.buscaMinas import Buscaminas
from modelo.opciones import Opciones
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
BLUE1 = (0, 99, 120)


class Menu():
    def __init__(self):
        self.image = pygame.image.load("imagen.jpg").convert()
        self.bInicio = pygame.Surface((235, 35))
        self.bInicio .fill(BLUE1) 
        self.bOpciones = pygame.Surface((235, 35))
        self.bOpciones .fill(BLUE1) 
        pygame.font.init()
        self.inicio()


    def inicio(self):
        rect = pygame.Rect((20, 20), (19, 19))
        screen.blit(self.image, (-200, -50))
        arial = pygame.font.SysFont("FrizQuadrata", 25)
        #fontObj = pygame.font.Font('freesansbold.ttf', 19)
        textoInicio = arial.render("JUGAR LIGA DE LAS MINAS", True, WHITE)
        textoOpciones = arial.render("OPCIONES", True, WHITE)
        screen.blit(self.bInicio , self.bInicio.get_rect(center=(124,48)))
        screen.blit(self.bOpciones , self.bInicio.get_rect(center=(124,88)))
        screen.blit(textoOpciones, (10,80))
        screen.blit(textoInicio, (10,40))
        self.mainLoop()
            
    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    startGame =  self.bInicio.get_rect(center=(124,48))
                    opciones = self.bOpciones.get_rect(center=(124,88))
                    if startGame.collidepoint(pos):
                        Buscaminas()
                        Menu()
                    if opciones.collidepoint(pos):
                        Opciones()
                #if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    
            pygame.display.update() #or pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()