import pygame
from const import *

class Dragger:
    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0
        self.piece = None
        self.dragging = False

    def updateMouse(self, position):
        self.mouseX, self.mouseY = position

    def saveInitial(self, position):
        self.initialRow = position[1]//SQUARE_SIZE
        self.initialCol = position[0]//SQUARE_SIZE

    def dragPiece(self, piece):
        self.piece = piece
        self.dragging = True

    def undragPiece(self):
        self.piece = None
        self.dragging = False
    
    def updateBlit(self, surface):
        self.piece.setImage(size=128)
        image = pygame.image.load(self.piece.image)
        imageCenter = (self.mouseX, self.mouseY)
        self.piece.textureRect = image.get_rect(center=imageCenter)
        surface.blit(image, self.piece.textureRect)