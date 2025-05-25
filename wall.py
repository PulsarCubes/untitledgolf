import pygame as pg

class Wall(pg.sprite.Sprite):
    def __init__(self,length,x=0, y=0):
        super().__init__()
        self.length = length
        self.x = x
        self.y = y
        self.image = pg.Surface((length,10))
