import pygame
import random
from modelo.juego import Juego
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((720, 500))
class Celda():

    def __init__(self):
            self.juego = Juego()
            m = 0
            self.contenidos = {}
            self.minas = m
            self.ayuda = {}
            self.click = {}
            self.sospecha = {}
            self.win = 138    #minimo es 40 lo recomendado es 138
            self.win2 = 138


    def printearCuadros(self, screen, image):
        for i in range(24):
            for x in range(36):
                rect = pygame.Rect((20*x, 20*(i+1)), (19, 19))
                screen.blit(image, rect)
                #v = random.randint(0 , 1000)
                self.ayuda.setdefault(str([20*x, 20*(i+1)]), 0)
                self.click.setdefault(str([20*x, 20*(i+1)]), 0)
                self.sospecha.setdefault(str([20*x, 20*(i+1)]), 0)
                #if v == 20:
                    #self.contenidos.setdefault(str([20*x, 20*(i+1)]), 1)
                    #self.minas = self.minas + 1
                    #self.consultaVecinas([20*x, 20*(i+1)])
                #elif v != 20:
                self.contenidos.setdefault(str([20*x, 20*(i+1)]), 0)
        while self.minas < self.win:
        #while self.minas < 50:
                x = random.randint(0,35)*20
                y = random.randint(1,24)*20
                if self.contenidos[str([x, y])] !=1:
                    self.contenidos[str([x, y])] = 1
                    self.consultaVecinas([x, y])
                    self.minas = self.minas + 1
        print(self.minas)

    def mina(self, pos, image):
        suma = 0
        x = pos[0]
        y = pos[1]
        auxX = x % 20   
        auxY = y % 20
        lugar = [(x-auxX), (y-auxY)]
        auxiliar =str(lugar)
        if self.sospecha.get(auxiliar) == 0 and self.click.get(auxiliar) == 0:
            image = pygame.Surface((19, 19))
            image .fill(RED) 
            #Aux . fill(BLUE)
            self.sospecha[auxiliar] = 1
            self.click[auxiliar] = 1
            screen.blit(image, lugar)
            if self.contenidos.get(auxiliar) == 1:
                self.win = self.win - 1
        elif self.sospecha.get(auxiliar) == 1:
            image = pygame.Surface((19, 19))
            image .fill(BLACK) 
            #Aux . fill(BLUE)
            self.sospecha[auxiliar] = 0
            self.click[auxiliar] = 0
            screen.blit(image, lugar)
            if self.contenidos.get(auxiliar) == 1:
                self.win = self.win + 1
        for i in range(24):
            for x in range(36):
                suma = suma + self.sospecha.get(str([20*x, 20*(i+1)]))
        if self.win == 0 and suma == self.win2:
            self.juego.win()
            

    def cambiarColor(self, image, lugar):
        
        pygame.font.init()
        auxiliar = str(lugar)
        if self.click.get(auxiliar) == 0:
            if self.ayuda.get(auxiliar) != 0:
                image = pygame.Surface((19, 19))
                image .fill(BLUE) 
                self.click[auxiliar] = 1
                screen.blit(image, lugar)
                fontObj = pygame.font.Font('freesansbold.ttf', 19)
                texto = fontObj.render(str(self.ayuda[auxiliar]), True, GREEN, BLUE)
                auxiliarPos = (lugar[0] + 3, lugar[1])
                screen.blit(texto, auxiliarPos)
                self.click[auxiliar] = 1
            else:
                image = pygame.Surface((19, 19))
                image .fill(BLUE) 
                self.click[auxiliar] = 1
                screen.blit(image, lugar)
    
    def clickAutomatico(self, pos, image):
        #auxiliarAyuda = str(pos)
        listaAyuda = []
        listaAyuda =  listaAyuda + pos
        for x in [(-1), 0, 1]:
            for y in [(-1), 0, 1]:
                listaAyuda[0] = listaAyuda[0] + 20 * x
                listaAyuda[1] = listaAyuda[1] + 20 * y
                auxiliarDiccionario = str(listaAyuda)
                if listaAyuda[0] >= 0 and listaAyuda[1] >= 20:
                    if listaAyuda[0] <= 700 and listaAyuda[1] <= 480:
                        if self.click.get(auxiliarDiccionario) == 0:
                            if self.contenidos.get(auxiliarDiccionario) != 1:
                                #if self.ayuda.get(auxiliarDiccionario) == 0:
                                self.cambiarColor(image, listaAyuda)
                                self.consultaContenidos(listaAyuda, image)
                listaAyuda = []
                listaAyuda = listaAyuda + pos

    def consultaContenidos(self, pos, image):
        x = pos[0]
        y = pos[1]
        auxX = x % 20
        auxY = y % 20
        lugar = [(x-auxX), (y-auxY)]
        auxiliar =str(lugar)
        print(auxiliar)
        if self.contenidos.get(auxiliar) == 0:
            self.cambiarColor(image, lugar)
            if self.ayuda[auxiliar] == 0:
                self.clickAutomatico(lugar, image)
                print(self.ayuda[auxiliar])
        if self.contenidos.get(auxiliar) == 1:
            self.juego.lose()
    
    def consultaVecinas(self, pos):
        auxiliarAyuda = str(pos)
        listaAyuda = []
        listaAyuda =  listaAyuda + pos
        for x in [(-1), 0, 1]:
            for y in [(-1), 0, 1]:
                listaAyuda[0] = listaAyuda[0] + 20 * x
                listaAyuda[1] = listaAyuda[1] + 20 * y
                auxiliarDiccionario = str(listaAyuda)
                if listaAyuda[0] >= 0 and listaAyuda[1] >= 20:
                    if listaAyuda[0] <= 700 and listaAyuda[1] <= 480:
                        if self.contenidos.get(auxiliarAyuda) == 1:
                            self.ayuda[auxiliarDiccionario] = self.ayuda[auxiliarDiccionario] + 1
                listaAyuda = []
                listaAyuda = listaAyuda + pos
                    
                
                    

    def prueba(self, image, pos):
        for i in range(24):
            for a in range(36):
                x = pos[0]
                y = pos[1]
                auxX = x % 20
                auxY = y % 20
                lugar = [(x-auxX)+(a*20), (y-auxY)+(i*20)]
                auxiliar =str(lugar)

                image = pygame.Surface((19, 19))
                image .fill(BLUE) 
                #Aux . fill(BLUE)
                if self.contenidos.get(auxiliar) == 0:
                    screen.blit(image, lugar)



if __name__ == "__main__":
    celda = Celda()