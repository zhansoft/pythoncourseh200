import pygame, sys, random as rn
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)

# this is bullshit
def contact(cir, rect):
    if (cir.center[0] > rect.loc[0]) and (cir.center[0] < rect.loc[0]+40) and (cir.center[1] > rect.loc[1]-7) and (cir.center[1] < rect.loc[1]-7):
        return True
    else:
        return False

class Circle:
    def __init__(self, center, rad, color):
        self.center = center
        self.rad = rad
        self.color = color
    
    def my_draw(self,screen):
        pygame.draw.circle(screen, self.color, self.center, self.rad)
    
    def my_move(self,xoffset,yoffset):
        self.center = [self.center[0]+xoffset,self.center[1]+yoffset] + self.center[2:]

class Guard:
    def __init__(self, loc, color):
        self.loc = loc
        self.color = color
    
    def my_draw(self, screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]

size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong for losers")

moveRight = False
moveLeft = False

MOVEMENT = 5

g = Guard([130, 290, 40, 5], BLACK) #290
b = Circle([0, 0], 7, BLUE)

while True:
    
    pygame.time.wait(40)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True

 
    screen.fill(WHITE)
 
    g.my_draw(screen)
    b.my_draw(screen)

    if b.center[0] > 280:
        xd_b = -rn.randint(3,6)

    if b.center[0] < 10:
        xd_b = rn.randint(3,6)

    if b.center[1] < 10:
        yd_b = rn.randint(3,6)
    
    if contact(b, g):
        b.my_move(-xd_b, -xd_b)
    
    b.my_move(xd_b, yd_b)

    if moveLeft and g.loc[0] > 0:
        g.my_move(-MOVEMENT,0)
    if moveRight and g.loc[0] < 260:
        g.my_move(MOVEMENT,0)

    

    pygame.display.flip()