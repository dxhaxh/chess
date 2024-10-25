import os

class Piece:
    def __init__(self, name, colour, value, image=None, textureRect=None):
        self.name=name
        self.colour=colour
        self.value=value
        if self.colour=='black':
            self.value*=-1
        self.validMoves=[] #valid moves
        self.moved=False
        self.image = image
        self.setImage()
        self.textureRect=textureRect

    def setImage(self, size=80):
        self.image = os.path.join(f'misc/images/imgs-{size}px/{self.colour}_{self.name}.png')

    def addMoves(self, move):
        self.validMoves.append(move)

class Pawn(Piece):
    def __init__(self, colour):
        if colour == 'white':
            self.direction=-1
        else:
            self.direction=1

        super().__init__('Pawn', colour, 1)

class Knight(Piece):
    def __init__(self, colour):
        super().__init__('Knight', colour, 3)

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__('Bishop', colour, 3.1) #bishops are a bit better in endgame, 3.1 is used to reflect that 

class Rook(Piece):
    def __init__(self, colour):
        super().__init__('Rook', colour, 5)

class Queen(Piece):
    def __init__(self, colour):
        super().__init__('Queen', colour, 9)

class King(Piece):
    def __init__(self, colour):
        super().__init__('King', colour, 10**9)  #very high value since king is the most important piece of the game

