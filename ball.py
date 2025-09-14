import pygame as pg
import os


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = pg.math.Vector2(0, 0)
        ball_image_path = os.path.join(os.path.dirname(__file__), 'ball.png')
        self.image = pg.image.load(ball_image_path)
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.radius = self.rect.width / 2

    def update(self):
        if self.rect.left<=0:
            self.velocity.x*=-.9
        elif self.rect.right>=500:
            self.velocity.x*=-.9

        if self.rect.top<=0:
            self.velocity.y*=-.9
        elif self.rect.bottom>=500:
            self.velocity.y*=-.9

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if abs(self.velocity.x) > 0 or abs(self.velocity.y) > 0:
            if self.velocity.length() > 2:
                self.velocity *= .9
            else:
                self.velocity.x = 0
                self.velocity.y = 0
