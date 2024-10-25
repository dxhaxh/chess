from colour import Colour

class Theme:
    def __init__(self, lightBg, darkBg, lightTrace, darkTrace, lightMoves, darkMoves):
        self.bg = Colour(lightBg, darkBg)
        self.trace = Colour(lightTrace, darkTrace)
        self.moves = Colour(lightMoves, darkMoves)