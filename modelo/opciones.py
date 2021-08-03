import pygame
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.
LEFT = 1
RIGHT = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE1 = (0, 0, 255)
BLUE = (0, 99, 120)


class Opciones():
    def __init__(self):
        self.image = pygame.image.load("imagenO.jpg").convert()
        screen .fill(BLACK)
        self.bBack = pygame.Surface((200, 40))
        self.bBack .fill(BLUE)
        self.bAcept = pygame.Surface((200, 40))
        self.bAcept . fill(BLUE)
        self.inicio()

    def inicio(self):
        screen.blit(self.image, (-420, -100))
        # Boton para volver
        arial = pygame.font.SysFont("FrizQuadrata", 25)
        textoBack = arial.render("VOLVER AL MENU", True, WHITE)
        screen.blit(self.bBack , self.bBack.get_rect(center=(360,450)))
        screen.blit(textoBack, (287,440))
        # Boton para guardar configuración
        textoAcept = arial.render("GUARDAR", True, WHITE)
        screen.blit(self.bAcept , self.bAcept.get_rect(center=(360,400)))
        screen.blit(textoAcept, (320,390))
        self.mainLoop()

    def mainLoop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    backMenu =  self.bBack.get_rect(center=(360,450))
                    if backMenu.collidepoint(pos):
                        return(1)
            pygame.display.update()
