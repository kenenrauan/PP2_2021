# Paint
import pygame, random

# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

def main():
    screen = pygame.display.set_mode((800, 600))
    mode = 'random'
    tool_mode = 'pencil'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    first_pos = (-1, -1)
    tools = ['pencil', 'rectangle', 'circle', 'erase', 'color-selection']
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_1:
                    tool_mode = tools[0]
                if event.key == pygame.K_2:
                    tool_mode = tools[1]
                if event.key == pygame.K_3:
                    tool_mode = tools[2]
                if event.key == pygame.K_4:
                    tool_mode = tools[3]
                if event.key == pygame.K_5:
                    tool_mode = tools[4]
                if event.key == pygame.K_6:
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                if event.key == pygame.K_s:
                    pygame.image.save(screen, "image.png")
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool_mode in [tools[0], tools[3]]:
                    if tool_mode == tools[3]:
                        color = (0, 0, 0)
                    else:
                        if mode == 'random':
                            color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        elif mode != 'custom':
                            color = colors[mode]
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True
                elif tool_mode in [tools[1], tools[2]]:
                    first_pos = event.pos
                else:
                    print(color)
                    color = screen.get_at(event.pos)
                    print(color)
                    mode = 'custom'
            if event.type == pygame.MOUSEBUTTONUP:
                if tool_mode in [tools[0], tools[3]]:
                    draw_on = False
                elif tool_mode == tools[1]:
                    if mode == 'random':
                         color = (random.randrange(256), random.randrange(256), random.randrange(256))
                    elif mode != 'custom':
                        color = colors[mode]
                    x = min(first_pos[0], event.pos[0])
                    y = min(first_pos[0], event.pos[0])
                    w = abs(first_pos[0] - event.pos[0])
                    h = abs(first_pos[1] - event.pos[1])
                    pygame.draw.rect(screen, color, ((x, y), (w, h)))
                elif tool_mode == tools[2]:
                    if mode == 'random':
                         color = (random.randrange(256), random.randrange(256), random.randrange(256))
                    elif mode != 'custom':
                        color = colors[mode]
                    x = min(first_pos[0], event.pos[0])
                    y = min(first_pos[1], event.pos[1])
                    w = abs(first_pos[0] - event.pos[0])
                    h = abs(first_pos[1] - event.pos[1])
                    pygame.draw.ellipse(screen, color, ((x, y), (w, h)))

            if event.type == pygame.MOUSEMOTION:
                if tool_mode in [tools[0], tools[3]]:
                    if draw_on:
                        drawLine(screen, last_pos, event.pos, radius, color)
                     # pygame.draw.circle(screen, color, event.pos, radius)
                    last_pos = event.pos
        pygame.display.flip()

    pygame.quit()

main()

# rect = pygame.Rect(10, 20, 30, 50)
# print(rect.bottom)
# print(rect.top)
# print(rect.left)
# print(rect.right)
# print(rect.bottomleft)
# print(rect.bottomright)
# print(rect.center)