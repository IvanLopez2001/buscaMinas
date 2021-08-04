import pygame
from io import open
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
pygame.font.init()
arial = pygame.font.SysFont("FrizQuadrata", 25)
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
        self.bMas = pygame.Surface((50, 50))
        self.bMas .fill(BLUE)
        self.bMenos = pygame.Surface((50, 50))
        self.bMenos .fill(BLUE)
        self.bMinimo = pygame.Surface((50, 50))
        self.bMinimo .fill(BLUE)
        self.bRecomendado = pygame.Surface((50, 50))
        self.bRecomendado .fill(BLUE)
        self.bMaximo = pygame.Surface((50, 50))
        self.bMaximo .fill(BLUE)
        self.bAcept = pygame.Surface((200, 40))
        self.bAcept . fill(BLUE)
        self.inicio()

    def inicio(self):
        archivo = open("Minas.txt","r")
        minas = int(archivo.read())
        archivo.close()
        self.dibujo(minas)
        self.mainLoop()
    def dibujo(self, minas):
        screen .fill(BLACK)
        screen.blit(self.image, (-420, -100))
        #Boton minimo
        textoMinimo = arial.render("50", True, WHITE)
        screen.blit(self.bMinimo , self.bMinimo.get_rect(center=(150,200)))
        screen.blit(textoMinimo, (140,190))
        #Boton recomendado
        textoMaximo = arial.render("138", True, WHITE)
        screen.blit(self.bMaximo , self.bRecomendado.get_rect(center=(350,200)))
        screen.blit(textoMaximo, (340,190))
        #Boton maximo
        textoMaximo = arial.render("863", True, WHITE)
        screen.blit(self.bMaximo , self.bMaximo.get_rect(center=(600,200)))
        screen.blit(textoMaximo, (590,190))
        # Boton para volver
        textoBack = arial.render("VOLVER AL MENU", True, WHITE)
        screen.blit(self.bBack , self.bBack.get_rect(center=(360,450)))
        screen.blit(textoBack, (287,440))
        # Boton para guardar configuración
        textoAcept = arial.render("GUARDAR", True, WHITE)
        screen.blit(self.bAcept , self.bAcept.get_rect(center=(360,400)))
        screen.blit(textoAcept, (320,390))
        # Boton para subir cantidad de minas
        textoMas = arial.render("+", True, WHITE)
        screen.blit(self.bMas , self.bMas.get_rect(center=(600,100)))
        screen.blit(textoMas, (595,90))
        # Boton para bajar cantidad de minas
        textoMenos = arial.render("-", True, WHITE)
        screen.blit(self.bMenos , self.bMas.get_rect(center=(150,100)))
        screen.blit(textoMenos, (145,90))
        textoMinas = arial.render("Cantidad de minas: " + str(minas),True,WHITE,BLACK)
        screen.blit(textoMinas , (275,90))
        return
    def mainLoop(self):
        archivo = open("Minas.txt","r")
        minas = int(archivo.read())
        archivo.close()
        self.dibujo(minas)
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    backMenu =  self.bBack.get_rect(center=(360,450))
                    mas = self.bMas.get_rect(center=(600,100))
                    menos = self.bMenos.get_rect(center=(150,100))
                    guardar = self.bAcept.get_rect(center=(360,400))
                    minimo = self.bMinimo.get_rect(center=(150,200))
                    maximo = self.bMaximo.get_rect(center=(600,200))
                    recomendado = self.bRecomendado.get_rect(center=(350,200))
                    if minimo.collidepoint(pos):
                        minas = 50
                        self.dibujo(minas)
                    if maximo.collidepoint(pos):
                        minas = 863
                        self.dibujo(minas)
                    if recomendado.collidepoint(pos):
                        minas = 138
                        self.dibujo(minas)
                    if mas.collidepoint(pos):
                        if minas == 863:
                            minas = 863
                        else:
                            minas = minas + 1
                            self.dibujo(minas)
                    if menos.collidepoint(pos):
                        if minas == 50:
                            minas = 50
                        else:
                            minas = minas - 1
                            self.dibujo(minas)
                    if backMenu.collidepoint(pos):
                        return(1)
                    if guardar.collidepoint(pos):
                        archivo = open("Minas.txt","w")
                        archivo.write(str(minas))
                        archivo.close()
                        return(1)
            pygame.display.update()
