import pygame
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#rect = pygame.Rect((0, 20), (20, 20))
image = pygame.Surface((20, 20))
image .fill(WHITE)  
menu = pygame.Surface((720, 20))
menu .fill(RED)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(BLACK)
    for i in range(24):
        for x in range(36):
            rect = pygame.Rect((20*x, 20*(i+1)), (20, 20))
            screen.blit(image, rect)
    screen.blit(menu, [0,0])
    pygame.display.update() #or pygame.display.flip()




