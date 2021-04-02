import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
YELLOW = (225, 225, 0)
WHITE = (255,255,255)

# DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
DISPLAYSURF = pygame.display.set_mode((1000, 800), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    #TODO: Implement function
    z = math.sqrt(math.pow(width, 2) - math.pow(width/2, 2)) # height
    pointL = (loc[0], loc[1]+z)
    pointT = (loc[0] + width/2, loc[1])
    pointR = (loc[0] + width, loc[1]+z)
    return (pointL, pointT, pointR)

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    dictColors = {0: BLUE, 1: RED, 2: YELLOW, 3: GREEN}
    pygame.draw.polygon(DISPLAYSURF, dictColors[rn.randint(0, 3)], (triangle(loc, w)), 1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    #TODO: Implement Function
    points = triangle(loc, width)
    midpointL = ((points[0][0] + points[1][0])/2, (points[0][1] + points[1][1])/2)
    midpointB = ((points[0][0] + points[2][0])/2, (points[0][1] + points[2][1])/2)
    midpointR = ((points[1][0] + points[2][0])/2, (points[1][1] + points[2][1])/2)
    if width > 1:
        s(midpointL, width/2)
        s(midpointB, width/2)
        s(midpointR, width/2)
    else:
        return draw_triangle(loc, width)


s((0,0),440)

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()