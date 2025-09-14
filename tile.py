import pygame as pg
import wall


class Tile(pg.sprite.Sprite):
    def __init__(self, type, orientation=0, center=(0, 0)):
        super().__init__()
        self.image = pg.Surface((200, 200))
        self.image.fill((68, 234, 82))
        self.rect = self.image.get_rect()
        self.orientation = orientation
        #note that center is not using pygame coords its using a seperate system
        self.center = center
        self.type = type
        self.open_faces = []
        self.wallgroup = pg.sprite.Group()

        types = {"hallway": 2, "slanted_hallway": 2, "open": 3, "single": 1, "empty": 0, "triangle": 1}
        for i in range(types[type]):
            _wall = wall.Wall(200)
            self.wallgroup.add(_wall)
        wall_list = list(self.wallgroup)
        if self.type == "hallway":
            if orientation % 2 == 0:
                wall_list[1].rect.topleft = (190, 0)
            else:
                for _wall in wall_list:
                    _wall.image = pg.transform.rotate(_wall.image, self.orientation * 90)
                    _wall.rect = _wall.image.get_rect(center=_wall.rect.center)
                    wall_list[1].rect.topleft = (0, 190)
            wall_list[0].rect.topleft = (0, 0)
        if self.type == "single":
            self.open_faces = [i for i in range(orientation) if i != orientation]
            if orientation % 2 == 0:
                wall_list[0].rect.topleft = orientation * 95, 0
            else:
                wall_list[0].image = pg.transform.rotate(wall_list[0].image, self.orientation * 90)
                wall_list[0].rect.topleft = (0, (orientation - 1) * 95)
        if self.type == "open":
            if orientation % 2 == 0:

                wall_list[1].rect.topleft = (190, 0)
                wall_list[2].image = pg.transform.rotate(wall_list[2].image, (self.orientation + 1) * 90)
                wall_list[2].rect = wall_list[2].image.get_rect(center=wall_list[2].rect.center)
                wall_list[2].rect.topleft = (0, orientation * 95)
            else:
                for _wall in wall_list[:2]:
                    _wall.image = pg.transform.rotate(_wall.image, self.orientation * 90)
                    _wall.rect = _wall.image.get_rect(center=_wall.rect.center)
                    wall_list[1].rect.topleft = (0, 190)
                wall_list[2].rect.topleft = ((orientation - 1) * 95, 0) 
            wall_list[0].rect.topleft = (0, 0)
        if self.type == "triangle":
            wall_list[0].image = pg.Surface((int(200*1.4),15), pg.SRCALPHA)
            wall_list[0].image.fill(((250, 249, 246)))
            wall_list[0].image = pg.transform.rotate(wall_list[0].image,45)
            wall_list[0].rect = wall_list[0].image.get_rect()
            wall_list[0].rect.center = (100,100)
            if orientation % 2 == 0:
                wall_list[0].image = pg.transform.rotate(wall_list[0].image, 90)
                wall_list[0].rect = wall_list[0].image.get_rect()
                wall_list[0].topleft = 0,0
        if self.type == "slanted_hallway":
            self.image = pg.Surface((200, 400))
            pg.draw.polygon(self.image, (68, 234, 82), [(0, 200), (200, 0), (200, 200), (0, 400)])
            if orientation % 2 == 0:
                self.image = pg.transform.flip(self.image, True, False)
            for _wall in wall_list:
                _wall.image = pg.Surface((int(200 * 1.4), 15), pg.SRCALPHA)
                _wall.image.fill(((250, 249, 246)))
                _wall.image = pg.transform.rotate(_wall.image, 45+(self.orientation-1)  * 90)
                _wall.rect = _wall.image.get_rect(center=_wall.rect.center)
                _wall.rect.center = (100, 100)
            wall_list[0].rect.topleft = (0, 0)
            wall_list[1].rect.topright = (200,200)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.wallgroup.draw(surface)
