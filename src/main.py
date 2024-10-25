import pygame
import sys
from const import *
from game import Game

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
                    dragger.undragPiece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()

main.mainLoop()