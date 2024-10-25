from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0 for j in range(0, COLS)] for i in range(0, ROWS)]
        self.lastMove = None
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
        

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        #console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece=piece

        piece.moved=True

        #clear valid moves
        piece.validMoves = []

        #set last move
        self.lastMove = move

    def validMove(self, piece, move):
        #of course we could use a hashset here to use in efficiently
        #but since validMoves array is never too large, we can consider this operation as an O(1) operation
        return move in piece.validMoves

    def calcMoves(self, piece, row, col):
        #this method is huge and there is some repeated code, this could be simplified by creating some functions
        #to accomplish what the repeating code does

        def knightMoves():
            for i in [-2, -1, 1, 2]:
                for j in [-2, -1, 1, 2]:
                    if abs(i)==abs(j):
                        continue
                    poss=(row+i, col+j)
                    if Square.inrange(poss[0], poss[1]) and self.squares[poss[0]][poss[1]].isEmptyOrRival(piece.colour):
                        initial = Square(row, col)
                        final = Square(poss[0], poss[1])
                        move = Move(initial, final)
                        piece.addMoves(move)

        def pawnMoves():
            if piece.moved:
                steps=1
            else:
                steps=2
            
            #vertical moves
            start=row+piece.direction
            end=row+(piece.direction*(1+steps))
            for possRow in range(start, end, piece.direction):
                if Square.inrange(possRow) and not self.squares[possRow][col].hasPiece():
                    #create initial and final move squares 
                    initial=Square(row, col)
                    final=Square(possRow, col)
                    #now create move
                    move=Move(initial, final)
                    piece.addMoves(move)
                #either blocked or goes out of bounds
                else:
                    break

            #diagonal moves
            possRow = row + piece.direction
            possCols = [col-1, col+1]
            for possCol in possCols:
                if Square.inrange(possCol) and self.squares[possRow][possCol].hasRivalPiece(piece.colour):
                    initial=Square(row, col)
                    final=Square(possRow, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)

            
        def lineMoves():
            for i in range(1, 8):
                possRow = row+i
                if Square.inrange(possRow):
                    if self.squares[possRow][col].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][col].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, col)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, col)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for i in range(1, 8):
                possRow = row-i
                if Square.inrange(possRow):
                    if self.squares[possRow][col].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][col].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, col)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, col)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for j in range(1, 8):
                possCol = col+j
                if Square.inrange(possCol):
                    if self.squares[row][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[row][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(row, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(row, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for j in range(1, 8):
                possCol = col-j
                if Square.inrange(possCol):
                    if self.squares[row][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[row][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(row, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(row, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break

        def diagMoves():
            for i in range(1, 8):
                possRow = row - i
                possCol = col + i
                if Square.inrange(possRow, possCol):
                    if self.squares[possRow][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for i in range(1, 8):
                possRow = row - i
                possCol = col - i
                if Square.inrange(possRow, possCol):
                    if self.squares[possRow][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for i in range(1, 8):
                possRow = row + i
                possCol = col - i
                if Square.inrange(possRow, possCol):
                    if self.squares[possRow][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            for i in range(1, 8):
                possRow = row + i
                possCol = col + i
                if Square.inrange(possRow, possCol):
                    if self.squares[possRow][possCol].hasTeamPiece(piece.colour):
                        break
                    if self.squares[possRow][possCol].hasRivalPiece(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)
                        break
                    initial=Square(row, col)
                    final=Square(possRow, possCol)
                    move=Move(initial, final)
                    piece.addMoves(move)
                else:
                    break
            
        
        def kingMoves():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i==0 and j==0:
                        continue
                    possRow=row+i
                    possCol=col+j
                    if Square.inrange(possRow, possCol) and self.squares[possRow][possCol].isEmptyOrRival(piece.colour):
                        initial=Square(row, col)
                        final=Square(possRow, possCol)
                        move=Move(initial, final)
                        piece.addMoves(move)

            #kingside castle

            #queenside castle



        if piece.name=='Pawn':
            pawnMoves()

        if piece.name=='Bishop':
            diagMoves()

        if piece.name=='Knight':
            knightMoves()

        if piece.name=='Rook':
            lineMoves()

        if piece.name=='Queen':
            lineMoves()
            diagMoves()
        
        if piece.name=='King':
            kingMoves()