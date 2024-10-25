import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainLoop(self):

        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board=self.game.board

        while True:
            game.showBackground(screen)
            game.showMoves(screen)
            game.showPieces(screen)

            if dragger.dragging:
                dragger.updateBlit(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updateMouse(event.pos)
                    clickedRow=dragger.mouseY//SQUARE_SIZE
                    clickedCol=dragger.mouseX//SQUARE_SIZE
                    if board.squares[clickedRow][clickedCol].hasPiece():
                        piece = board.squares[clickedRow][clickedCol].piece
                        if piece.colour!=game.nextTurn:
                            continue
                        board.calcMoves(piece, clickedRow, clickedCol)
                        dragger.saveInitial(event.pos)
                        dragger.dragPiece(piece)
                        
                        game.showBackground(screen)
                        game.showMoves(screen)
                        game.showPieces(screen)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.updateMouse(event.pos)
                        game.showBackground(screen)
                        game.showMoves(screen)
                        game.showPieces(screen)
                        dragger.updateBlit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.updateMouse(event.pos)
                        releasedRow=dragger.mouseY//SQUARE_SIZE
                        releasedCol=dragger.mouseX//SQUARE_SIZE
                        initial = Square(dragger.initialRow, dragger.initialCol)
                        final = Square(releasedRow, releasedCol)
                        move = Move(initial, final)
                        if board.validMove(dragger.piece, move):
                            board.move(dragger.piece, move)
                            game.showBackground(screen)
                            game.showPieces(screen)
                            game.changeTurn()
                        else:
                            dragger.piece.validMoves=[]
                    dragger.undragPiece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()

main.mainLoop()