import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.yVelocity = 0
        self.xVelocity = 0
        self.image = pg.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y



