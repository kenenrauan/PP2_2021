import pygame as pg
import math
from math import sin, cos, pi

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (800, 600)
screen = pg.display.set_mode(size)

pg.display.set_caption("TSIS7 sin and cos wave")
font = pg.font.SysFont('calibri', 16)

PI = math.pi

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill(WHITE)
    pg.draw.rect(screen, BLACK, (50, 50, 650, 450), 2)
    pg.draw.line(screen, BLACK, (50, 275), (700, 275), 3)
    pg.draw.line(screen, BLACK, (375, 50), (375, 500), 3)
    pg.draw.line(screen, BLACK, (75, 50), (75, 500), 1)
    pg.draw.line(screen, BLACK, (675, 50), (675, 500), 1)
    pg.draw.line(screen, BLACK, (50, 75), (700, 75), 1)
    pg.draw.line(screen, BLACK, (50, 475), (700, 475), 1)
    
    for x in range(75, 375, 100):
        pg.draw.line(screen, BLACK, (x, 50), (x, 500), 1)
    for x in range(475, 576, 100):
        pg.draw.line(screen, BLACK, (x, 50), (x, 500), 1)
    
    screen.blit(font.render('-3π', False, BLACK), (65, 500))
    screen.blit(font.render('-2π', False, BLACK), (165, 500))
    screen.blit(font.render('-π', False, BLACK), (275, 500))
    screen.blit(font.render('0', False, BLACK), (375, 500))
    screen.blit(font.render('π', False, BLACK), (475, 500))
    screen.blit(font.render('2π', False, BLACK), (575, 500))
    screen.blit(font.render('3π', False, BLACK), (675, 500))

    screen.blit(font.render('1', False, BLACK), (25, 65))
    screen.blit(font.render('0', False, BLACK), (25, 265))
    screen.blit(font.render('-1', False, BLACK), (25, 465))

    screen.blit(font.render('sin(x)', False, BLACK), (25, 530))
    pg.draw.line(screen, RED, (70, 540), (100, 540), 1)
    screen.blit(font.render('cos(x)', False, BLACK), (25, 550))
    pg.draw.line(screen, BLUE, (73, 560), (103, 560), 1)
    for x in range(75, 675):
        sin1 = 200 * math.sin((x - 75) / 100 * PI)
        sin2 = 200 * math.sin((x - 74) / 100 * PI)
        pg.draw.aalines(screen, RED, False, [(x, 275 + sin1), ((x + 1), 275 + sin2)])
    for x in range(75, 675):
        cos1 = 200 * math.cos((x - 75) / 100 * PI)
        cos2 = 200 * math.cos((x - 74) / 100 * PI)
        pg.draw.aalines(screen, BLUE, False, [(x, 275 + cos1), ((x + 1), 275 + cos2)])
    pg.display.update()
pg.quit()