import pygame as pg
from settings import *

class Label:
    def __init__(self, text, game, fontSize):
        self.text = text
        self.font = pg.font.SysFont('times new roman', fontSize)
        self.game = game

    def draw(self, x, y):
        self.label = self.font.render(self.text, 1, WHITE)
        self.game.screen.blit(self.label, (x,y))
    
    def getSize(self):
        return self.font.size(self.text)