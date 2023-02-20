import pygame as pg
import sys
from settings import *
from board import *
from label import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.newgame()
    

    def newgame(self):
        self.board = Board(self)
        self.Title = Label("TETRIS", self, 20)
        self.Author = Label("BY OTSUTE", self, 20)
        self.message1 = Label("Press any key to start playing", self, 15)
        self.draw()
        self.Title.draw(144-self.Title.getSize()[0]/2, 50)
        self.Author.draw(144-self.Author.getSize()[0]/2, 75)
        self.message1.draw(144-self.message1.getSize()[0]/2, 100)
        self.update()
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.KEYUP:
                    waiting = False

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