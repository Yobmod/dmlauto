#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:31:44 2017

@author: yobmod
"""

import pygame
import sys
from pygame.locals import QUIT

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

ALPHASURF = DISPLAYSURF.convert_alpha()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, [(146, 0),
                                         (291, 106),
                                         (236, 277),
                                         (56, 277),
                                         (0, 106), ])
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[482][386] = BLACK
pixObj[484][388] = BLACK
del pixObj


while True:
    for event in pygame.event.get():  # gets list of event objects
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
