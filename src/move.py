class Move:
    def __init__(self, initial, final):
        #initial and final are Squares
        self.initial=initial
        self.final=final

    def __eq__(self, other):
        #added in order to check if a move is in validMoves array
        #of course in the line where we use in to check if a move is a valid move, we could use a hashset
        #to make the lookup quicker, but since there arent too many valid moves for each piece we could consider 
        #the using in with the array as O(1) time
        return self.initial==other.initial and self.final==other.final