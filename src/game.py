import pygame
from const import *

class Game:
    def __init__(self):
        pass

    def showBackground(self, surface):
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if (row+col)%2==0:
                    colour=(234, 235, 200) #dark square
                else:
                    colour=(119, 154, 88)  #light square

                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, colour, rect)