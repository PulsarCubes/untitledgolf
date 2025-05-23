import pygame as pg

import ball
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption('golf on that thing')
clicked = False
ball = ball.Ball()

ball.rect.center = (random.randint(0, 500), random.randint(0, 500))

while True:
    screen.fill((68, 234, 82))

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            clicked = True
            if ball.rect.collidepoint(mouse_pos):
                moved = pg.math.Vector2(ball.rect.center) - mouse_pos
        elif event.type == pg.MOUSEMOTION:
            if clicked:
                #line_pos = moved+event.pos
                pg.draw.line(screen, (0, 0, 0), ball.rect.center, moved+event.pos, 10)
        elif event.type == pg.MOUSEBUTTONUP:
            clicked = False
        if event.type == pg.QUIT:
            pg.quit()
    screen.blit(ball.image, ball.rect)
    # if clicked:
    #     pg.draw.line(screen, (0, 0, 0), ball.rect.center, line_pos, 10)
    pg.display.update()
    clock.tick(30)
