import pygame as pg
import sys
from settings import *
from board import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.board = Board(self)
    
    def update(self):
        pg.display.flip()
    
    def draw(self):
        self.screen.fill("black")
        self.board.draw()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.checkEvents()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()    