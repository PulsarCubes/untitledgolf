import pygame as pg
import wall


class Tile(pg.sprite.Sprite):
    def __init__(self, type, center=(0, 0)):
        super().__init__()
        self.image = pg.Surface((200, 200))
        self.image.fill((68, 234, 82))
        self.rect = self.image.get_rect()
        self.center = center
        self.type = type
        self.wallgroup = pg.sprite.Group()
        types = {"hallway": 2, "slanted_hallway": 2, "open": 3, "single": 1, "empty": 0, "triangle": 1}
        for i in range(types[type]):
            _wall = wall.Wall(200)
            self.wallgroup.add(_wall)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.wallgroup.draw(surface)