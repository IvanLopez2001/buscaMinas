import pygame
import time
from modelo.buscaMinas import *
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

class Juego():
    def __init__(self):
        self.imagenLose = pygame.image.load("imagenLose.jpg").convert()
        self.imgenWin = pygame.image.load("imagenWin.jpg").convert()
        self.bReturnGame = pygame.Surface((235, 35))
        self.bReturnGame .fill(BLACK) 
        self.bQuit = pygame.Surface((235, 35))
        self.bQuit .fill(BLACK) 
    def win(self):
        time.sleep(1)
        screen.blit(self.imgenWin, (0, 0))
        arial = pygame.font.SysFont("FrizQuadrata", 25)
        textoInicio = arial.render("Play again", True, WHITE)
        textoOpciones = arial.render("Quit Game", True, WHITE)
        screen.blit(self.bReturnGame , self.bReturnGame.get_rect(center=(330,375)))
        screen.blit(self.bQuit , self.bQuit.get_rect(center=(330,420)))
        screen.blit(textoOpciones, (280,410))
        screen.blit(textoInicio, (280,365))
        self.mainLoop()
    def lose(self):
        time.sleep(1)
        screen.blit(self.imagenLose, (0, 0))
        arial = pygame.font.SysFont("FrizQuadrata", 25)
        textoInicio = arial.render("Back menu", True, WHITE)
        textoOpciones = arial.render("Quit Game", True, WHITE)
        screen.blit(self.bReturnGame , self.bReturnGame.get_rect(center=(330,375)))
        screen.blit(self.bQuit , self.bQuit.get_rect(center=(330,420)))
        screen.blit(textoOpciones, (280,410))
        screen.blit(textoInicio, (280,365))
        self.mainLoop()
    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    startGame =  self.bReturnGame.get_rect(center=(330,375))
                    opciones = self.bQuit.get_rect(center=(330,420))
                    if startGame.collidepoint(pos):
                        return True
                    if opciones.collidepoint(pos):
                        quit()
                #if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    
            pygame.display.update() #or pygame.display.flip()

if __name__ == "__main__":
    juego = Juego()