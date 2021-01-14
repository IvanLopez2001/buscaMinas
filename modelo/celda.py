import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((720, 500))
class Celda():

    def __init__(self):
            m = 0
            self.contenidos = {}
            self.minas = m
            self.ayuda = {}


    def printearCuadros(self, screen, image):

        for i in range(24):
            for x in range(36):
                rect = pygame.Rect((20*x, 20*(i+1)), (19, 19))
                screen.blit(image, rect)
                #v = random.randint(0 , 1000)
                self.ayuda.setdefault(str([20*x, 20*(i+1)]), 0)
                #if v == 20:
                    #self.contenidos.setdefault(str([20*x, 20*(i+1)]), 1)
                    #self.minas = self.minas + 1
                    #self.consultaVecinas([20*x, 20*(i+1)])
                #elif v != 20:
                self.contenidos.setdefault(str([20*x, 20*(i+1)]), 0)
        while self.minas < 50:
                x = random.randint(1,35)*20
                y = 20*random.randint(1,23)
                if self.contenidos[str([x, y])] !=1:
                    self.contenidos[str([x, y])] = 1
                    self.consultaVecinas([x, y])
                    self.minas = self.minas + 1
        print(self.minas)



    def cambiarColor(self, image, lugar):
        image = pygame.Surface((19, 19))
        image .fill(BLUE) 
        #Aux . fill(BLUE)
        screen.blit(image, lugar)
    

    def consultaContenidos(self, pos, image):
        x = pos[0]
        y = pos[1]
        auxX = x % 20
        auxY = y % 20
        lugar = [(x-auxX), (y-auxY)]
        print (lugar)
        auxiliar =str(lugar)
        if self.contenidos.get(auxiliar) == 0:
            self.cambiarColor(image, lugar)
            print(self.ayuda[auxiliar])
        if self.contenidos.get(auxiliar) == 1:
            quit()
    
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