import ball
import pygame as pg
import random
import tile

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption('golf on that thing')
ball_clicked = False
ball = ball.Ball()

ball.rect.center = (random.randint(0, 500), random.randint(0, 500))

while True:
    screen.fill((68, 234, 82))

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            line_pos = mouse_pos
            if ball.rect.collidepoint(mouse_pos):
                moved = pg.math.Vector2(ball.rect.center) - mouse_pos
                ball_clicked = True
        elif event.type == pg.MOUSEMOTION:
            if ball_clicked:
                line_pos = moved+event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            if ball_clicked:
                ball.velocity.update(-dir.x/8, -dir.y/8)
                ball_clicked = False
        if event.type == pg.QUIT:
            pg.quit()
    screen.blit(ball.image, ball.rect)
    if ball_clicked:
        center = pg.math.Vector2(ball.rect.center)
        mouse_vector = pg.math.Vector2(line_pos)
        dir = mouse_vector - center

        if dir.length() > 200:
            dir.scale_to_length(200)
        end = center + dir
        pg.draw.line(screen, (255,222,89), center, end, 5)
    ball.update()
    pg.display.update()
    clock.tick(30)
