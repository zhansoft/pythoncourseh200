import math
import pygame
import sys

MAX_ITER = 80

def mandelbrot(c, z,cnt):
    # so you can use complex hahahahah i want to cry
    if abs(z) < 2 and cnt < MAX_ITER:
        z = z*z + c
        cnt += 1
        return mandelbrot(c, z,cnt)
    else:
        return cnt

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

size = [900, 600] # 900, 600 later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mandelbrot")
screen.fill(WHITE)

# creating array of pixels
pixAr = pygame.PixelArray(screen)

for a in range (-600, 300):
    for b in range(-300, 300):
        c = complex(a/300, b/300)
        v = mandelbrot(c,0,0)
        if v < MAX_ITER:
            pixAr[a + 600, b + 300] = RED
        else:
            pixAr[a + 600, b + 300] = BLACK

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
    pygame.display.update()