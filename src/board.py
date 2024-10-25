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

        if piece.name=='Pawn':
            self.checkPromotion(piece, final)

        if piece.name=='King':
            if self.castled(initial, final):
                diff=final.col-initial.col
                if diff<0:
                    rook = piece.leftRook
                    rookInitial = Square(initial.row, 0)
                    rookFinal = Square(final.row, 3)
                else:
                    rook = piece.rightRook
                    rookInitial = Square(initial.row, 7)
                    rookFinal = Square(final.row, 5)
                
                self.move(rook, Move(rookInitial, rookFinal))

        piece.moved=True

        #clear valid moves
        piece.validMoves = []

        #set last move
        self.lastMove = move

    def validMove(self, piece, move):
        #of course we could use a hashset here to use in efficiently
        #but since validMoves array is never too large, we can consider this operation as an O(1) operation
        return move in piece.validMoves
    
    def checkPromotion(self, piece, final):
        if final.row==0 or final.row==7:
            self.squares[final.row][final.col].piece=Queen(piece.colour)

    def castled(self, initial, final):
        return abs(final.col-initial.col)==2 #return True if king castled

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
                if Square.inrange(possRow, possCol) and self.squares[possRow][possCol].hasRivalPiece(piece.colour):
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

            if not piece.moved:
            #kinside castling
                rightRook = self.squares[row][7].piece
                if rightRook.name=='Rook' and not rightRook.moved:
                    canCastleRight=False
                    for c in range(col+1, 7):
                        if self.squares[row][c].hasPiece():
                            break
                        if c==7-1:
                            canCastleRight=True
                    if canCastleRight:
                        piece.rightRook = rightRook

                        #kingMove
                        initial=Square(row, col)
                        final=Square(row, 6)
                        move=Move(initial, final)
                        piece.addMoves(move)

            #queenside castle
                leftRook = self.squares[row][0].piece
                if leftRook.name=='Rook' and not leftRook.moved:
                    canCastleLeft=False
                    for c in range(1, col):
                        if self.squares[row][c].hasPiece():
                            break
                        if c==col-1:
                            canCastleLeft=True
                    if canCastleLeft:
                        piece.leftRook = leftRook

                        #kingMove
                        initial=Square(row, col)
                        final=Square(row, 2)
                        move=Move(initial, final)
                        piece.addMoves(move)



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