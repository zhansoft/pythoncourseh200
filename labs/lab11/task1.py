import pygame
import sys
import numpy as np
import random as rn

pygame.init()
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
GREEN = (0,255,0)
RED =   (255,0,0)
YELLOW = (255,255,0)
DARK_GREEN = (85,107,47)

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        if ((isPointInsideRect(a.loc[0], a.loc[1], b)) or isPointInsideRect(a.loc[0], a.loc[1]+20, b) or isPointInsideRect(a.loc[0]+20, a.loc[1], b) or isPointInsideRect(a.loc[0]+20, a.loc[1]+20, b)):
            return True
    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.loc[0]) and (x < rect.loc[0]+20) and (y > rect.loc[1]) and (y < rect.loc[1]+20):
        return True
    else:
        return False



class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def get_loc(self):
        return self.loc

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
  
        
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("C200 CHANGE")


r = Rectangle(RED, [0, 0, 20, 20])
b = Rectangle(DARK_GREEN, [290, 290, 20, 20])

while True:
    
    pygame.time.wait(40)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
 
    screen.fill(WHITE)
 
    r.my_draw(screen)
    b.my_draw(screen)
    
    if r.loc[0] > 280:
        xd_r = -rn.randint(3,6)
        r.color = DARK_GREEN

    if b.loc[0] > 280:
        xd_b = -rn.randint(3,6)
        b.color = RED

    if r.loc[1] > 280:
        yd_r = -rn.randint(3,6)
        r.color = BLUE

    if b.loc[1] > 280:
        yd_b = -rn.randint(3,6)
        b.color = YELLOW

    if r.loc[0] < 10:
        xd_r = rn.randint(3,6)
        r.color = RED

    if b.loc[0] < 10:
        xd_b = rn.randint(3,6)
        b.color = BLUE

    if r.loc[1] < 10:
        yd_r = rn.randint(3,6)
        r.color = YELLOW

    if b.loc[1] < 10:
        yd_b = rn.randint(3,6)
        b.color = GREEN

    if doRectsOverlap(r, b):
        xd_r = -rn.randint(3,6)
        yd_r = rn.randint(6,9)
        xd_b = rn.randint(6,9)
        yd_b = -rn.randint(3,6)
    
    r.my_move(xd_r, yd_r)
    b.my_move(xd_b, yd_b)
    

    pygame.display.flip()