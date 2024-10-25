class Square:
    def __init__(self, row, col, piece=None):
        self.row=row
        self.col=col
        self.piece=piece

    def __eq__(self, other):
        return self.row==other.row and self.col==other.col
    
    def hasPiece(self):
        return self.piece!=None
    
    @staticmethod
    def inrange(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    
    def isEmptyOrRival(self, colour):
        return not self.hasPiece() or self.hasRivalPiece(colour)

    def hasRivalPiece(self, colour):
        return self.hasPiece() and self.piece.colour!=colour

    def hasTeamPiece(self, colour):
        return self.hasPiece() and self.piece.colour==colour