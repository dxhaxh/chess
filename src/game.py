import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board=Board()
        self.dragger=Dragger()

    def showBackground(self, surface):
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if (row+col)%2==0:
                    colour=(234, 235, 200) #dark square
                else:
                    colour=(119, 154, 88)  #light square

                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, colour, rect)

    def showPieces(self, surface):
        for row in range(0, ROWS):
            for col in range(0, COLS):
                #check if there is a piece on (row, col)
                if self.board.squares[row][col].hasPiece():
                    piece = self.board.squares[row][col].piece
                    if piece!=self.dragger.piece:
                        piece.setImage(size=80)
                        image = pygame.image.load(piece.image)
                        imageCenter = (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2)
                        piece.textureRect = image.get_rect(center = imageCenter)
                        surface.blit(image, piece.textureRect)

    def showMoves(self, surface):
        if self.dragger.dragging:
            piece=self.dragger.piece

            for move in piece.validMoves:
                if (move.final.row + move.final.col)%2==0:
                    colourToBlit='#C86464'
                else:
                    colourToBlit='#C84646'

                rect = (move.final.col*SQUARE_SIZE, move.final.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, colourToBlit, rect)