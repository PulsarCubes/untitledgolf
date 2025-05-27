import pygame as pg

class Wall(pg.sprite.Sprite):
    def __init__(self,length,x=0, y=0):
        super().__init__()
        self.length = length
        self.image = pg.Surface((length,10))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
