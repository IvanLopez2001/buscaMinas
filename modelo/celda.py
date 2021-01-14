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
            self.contenidos = {}

    def printearCuadros(self, screen, image):
        for i in range(24):
            for x in range(36):
                rect = pygame.Rect((20*x, 20*(i+1)), (19, 19))
                screen.blit(image, rect)

                if random.randint(0 , 25) == 20:
                    self.contenidos.setdefault(str([20*x, 20*(i+1)]), 1)
                elif random.randint(0 , 25) != 20:
                    self.contenidos.setdefault(str([20*x, 20*(i+1)]), 0)





    def cambiarColor(self, pos, image):
        x = pos[0]
        y = pos[1]
        auxX = x % 20
        auxY = y % 20
        lugar = [(x-auxX), (y-auxY)]
        print (lugar)
        auxiliar =str(lugar)
        if self.contenidos.get(auxiliar) == 0:
            image = pygame.Surface((19, 19))
            image .fill(BLUE) 
            #Aux . fill(BLUE)
            screen.blit(image, lugar)


if __name__ == "__main__":
    celda = Celda()