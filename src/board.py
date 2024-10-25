from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares = [[0 for j in range(0, COLS)] for i in range(0, ROWS)]
        self._create()
        self._addPieces('white')
        self._addPieces('black')

    def _create(self):
        for row in range(0, ROWS):
            for col in range(0, COLS):
                self.squares[row][col] = Square(row, col)

    def _addPieces(self, colour):
        if colour=='white':
            pawnsRow = 6
            otherRow = 7
        else:
            pawnsRow = 1
            otherRow = 0
        
        for col in range(0, COLS):
            self.squares[pawnsRow][col] = Square(pawnsRow, col, Pawn(colour))
        self.squares[otherRow][1] = Square(otherRow, 1, Knight(colour))
        self.squares[otherRow][6] = Square(otherRow, 6, Knight(colour))
        self.squares[otherRow][0] = Square(otherRow, 0, Rook(colour))
        self.squares[otherRow][7] = Square(otherRow, 7, Rook(colour))
        self.squares[otherRow][2] = Square(otherRow, 2, Bishop(colour))
        self.squares[otherRow][5] = Square(otherRow, 5, Bishop(colour))
        self.squares[otherRow][3] = Square(otherRow, 3, Queen(colour))
        self.squares[otherRow][4] = Square(otherRow, 4, King(colour))