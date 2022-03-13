import pygame
import json
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
# pygame.mixer.music.load('sound.mp3')
# pygame.mixer.music.play(-1)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
difficult = 0
timer = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")


background = pygame.image.load("area.png")

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
        
def save1(snake1, difficult):
    data = {
        "snake1": snake1,
        "difficult": difficult
    }
    data = json.dumps(data, cls=MyEncoder)
    with open("save.txt", "w+") as f:
        f.write(data)

def save2(snake1, snake2, difficult):
    data = {
        "snake1": snake1,
        "snake2": snake2,
        "difficult": difficult
    }
    data = json.dumps(data, cls=MyEncoder)
    with open("save.txt", "w+") as f:
        f.write(data)                

def load_save():
    with open("save.txt", "r") as f:
        data = json.loads(f.read())
        print(data)
        difficult = data["difficult"]
        if difficult == 4:
            snake1 = Snake(0, 0)
            snake2 = Snake(0, 0)
            snake1.elements = data["snake1"]["elements"]
            snake2.elements = data["snake2"]["elements"]
            return [snake1, snake2], difficult
        else:
            snake1 = Snake(0, 0)
            snake1.elements = data["snake1"]["elements"]
            return [snake1], difficult

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (13, 162, 58)
        self.active_clr = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_clr, (x, y, self.width, self.height))

            if click[0] == 1:
                pygame.time.delay(300)
                if action is not None:
                    action()
        else:
            pygame.draw.rect(screen, self.inactive_clr, (x, y, self.width, self.height))

        print_text(message=message, x=x + 20, y=y, font_size=font_size)

class Food:
    def __init__(self):
        self.x = random.randint(60, 740)
        self.y = random.randint(60, 540)

    def gen(self):
        self.x = random.randint(60, 740)
        self.y = random.randint(60, 540)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 20, 20))

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5  # right
        self.dy = 0
        self.is_add = False
        self.speed = 10
        self.random_color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    # [x0, y0], [x1, y1], [x2, y2], [x3, y3] i -> i - 1

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, self.random_color, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if difficult == 2:
            if self.size % 2 == 0:
                self.speed += 10
        elif difficult == 3:
            if self.size % 2 == 0:
                self.speed += 15
        else:
            if self.size % 3 == 0:
                self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            # print(i)
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 20 and foody <= y <= foody + 20:
            self.random_color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            return True
        return False

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, GREY,(self.x, self.y, 40, 40))

    def collide(self, snakes):
        for snake in snakes:
            x, y = snake.elements[-1]
            x -= snake.radius
            y -= snake.radius
            w = snake.radius * 2
            h = snake.radius * 2
            if x < self.x + 40 and x + w > self.x and y < self.y + 40 and y + h > self.y:
                return True
        return False

def print_text(message, x, y, font_color=(0, 0, 0), font_size=30):
    font = pygame.font.SysFont('Comic Sans MS', 45)
    screen.blit(font.render(message, True, font_color), (x, y))

def show_menu():
    menu_bckgr = pygame.image.load('snake1.jpeg')
    show = True
    level_btn = Button(250, 55)
    level_btn2 = Button(300, 55)
    level_btn3 = Button(250, 55)
    multi_btn = Button(250, 55)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    snakes, difficult = load_save()
                    if difficult == 1:
                        easy_level(True, snakes)
                    elif difficult == 2:
                        meduim_level(True, snakes)
                    elif difficult == 3:
                        hard_level(True, snakes)
                    else:
                        start_2player(True, snakes)
        screen.blit(menu_bckgr, (0, 0))
        level_btn.draw(275, 200, 'Easy level', easy_level)
        level_btn2.draw(275, 270, 'Meduim level', meduim_level)
        level_btn3.draw(275, 340, 'Hard level', hard_level)
        multi_btn.draw(275, 410, '2 players', start_2player)
        pygame.display.update()
        clock.tick(60)

def easy_level(is_load = False, Snakes = None):
    
    difficult = 1
    snake1 = Snake(150, 100)
    food = Food()
    # wall = Wall()
    walls = []
    snakes = []
    snakes.append(snake1)
    if is_load == True:
        snake1 = Snakes[0]
        snakes = Snakes
    for x in range(0, 800):
        walls.append(Wall(x, 0))
    for x in range(0, 800):
        walls.append(Wall(x, 560))
    for y in range(0, 600):
        walls.append(Wall(0, y))
    for y in range(0, 600):
        walls.append(Wall(760, y))

    running = True

    d = 5
    FPS = 60

    clock = pygame.time.Clock()

    while running:
        clock.tick(snake1.speed)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d
                if event.key == pygame.K_k:
                    save1(snake1, difficult)
                    running = False
        if snake1.elements[-1][0] > 740 or snake1.elements[-1][0] < 50:
            running = False
        if snake1.elements[0][-1] > 540 or snake1.elements[0][-1] < 50:
            running = False
        
        if snake1.eat(food.x, food.y):
            snake1.is_add = True
            food.gen()

        snake1.move()
        snake1.draw()
        for wall in walls:
            wall.draw()
        food.draw()
        pygame.display.flip()

def meduim_level(is_load = False, Snakes = None):

    difficult = 2
    global timer
    timer = 0
    snake1 = Snake(150, 100)
    food = Food()
    snakes = []
    snakes.append(snake1)
    if is_load == True:
        snake1 = Snakes[0]
        snakes = Snakes
    walls = []
    for x in range(0, 800):
        walls.append(Wall(x, 0))
    for x in range(0, 800):
        walls.append(Wall(x, 560))
    for y in range(0, 600):
        walls.append(Wall(0, y))
    for y in range(0, 600):
        walls.append(Wall(760, y))
    for i in range(325, 445):
        walls.append(Wall(i, 120))
    for i in range(325, 445):
        walls.append(Wall(i, 440))
    for j in range(240, 320):
        walls.append(Wall(200, j))
    for j in range(240, 320):
        walls.append(Wall(570, j))
    running = True

    d = 5
    FPS = 60

    clock = pygame.time.Clock()

    while running:
        clock.tick(snake1.speed)
        screen.blit(background, (0, 0))
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d
                if event.key == pygame.K_k:
                    save1(snake1,difficult)
                    running = False
        if snake1.elements[-1][0] > 740 or snake1.elements[-1][0] < 50:
            running = False
        if snake1.elements[0][-1] > 540 or snake1.elements[0][-1] < 50:
            running = False
        
        if snake1.eat(food.x, food.y):
            snake1.is_add = True
            timer = 0
            food.gen()
        for wall in walls:
            if wall.collide(snakes):
                running = False
        # print(timer)
        if timer % 150 == 0:
            food.gen()
            timer = 0
        snake1.move()
        snake1.draw()
        for wall in walls:
            wall.draw()
        food.draw()
        pygame.display.flip()

def hard_level(is_load = False, Snakes = None):

    difficult = 3
    global timer
    timer = 0
    snake1 = Snake(150, 100)
    food = Food()
    snakes = []
    snakes.append(snake1)
    if is_load == True:
        snake1 = Snakes[0]
        snakes = Snakes
    walls = []
    for x in range(0, 800):
        walls.append(Wall(x, 0))
    for x in range(0, 800):
        walls.append(Wall(x, 560))
    for y in range(0, 600):
        walls.append(Wall(0, y))
    for y in range(0, 600):
        walls.append(Wall(760, y))
    for i in range(125, 225):
        walls.append(Wall(i, 120))
    for i in range(125, 225):
        walls.append(Wall(i, 440))
    for i in range(545, 635):
        walls.append(Wall(i, 120))
    for i in range(545, 635):
        walls.append(Wall(i, 440))
    for j in range(160, 240):
        walls.append(Wall(125, j))
    for j in range(325, 405):
        walls.append(Wall(125, j))
    for j in range(160, 240):
        walls.append(Wall(634, j))
    for j in range(325, 405):
        walls.append(Wall(634, j))
    for k in range(320, 440):
        walls.append(Wall(k, 280))
    for n in range(220, 340):
        walls.append(Wall(380, n))
    running = True

    d = 5
    FPS = 60

    clock = pygame.time.Clock()

    while running:
        timer += 1
        clock.tick(snake1.speed)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d
                if event.key == pygame.K_k:
                    save1(snake1, difficult)
                    running = False
        if snake1.elements[-1][0] > 740 or snake1.elements[-1][0] < 50:
            running = False
        if snake1.elements[0][-1] > 540 or snake1.elements[0][-1] < 50:
            running = False
        
        if snake1.eat(food.x, food.y):
            snake1.is_add = True
            timer = 0
            food.gen()
        for wall in walls:
            if wall.collide(snakes):
                running = False
        # print(timer)
        if timer % 200 == 0:
            food.gen()
            timer = 0
        snake1.move()
        snake1.draw()
        for wall in walls:
            wall.draw()
        food.draw()
        pygame.display.flip()

def start_2player(is_load = False, Snakes = None):
    # screen.fill((0, 0, 0))
    difficult = 4
    snake1 = Snake(150, 100)
    snake2 = Snake(150, 100)
    food = Food()
    walls = []
    snakes = []
    snakes.append(snake1)
    snakes.append(snake2)
    if is_load == True:
        snake1 = Snakes[0]
        snake2 = Snakes[1]
        snakes = Snakes
    for x in range(0, 800):
        walls.append(Wall(x, 0))
    for x in range(0, 800):
        walls.append(Wall(x, 560))
    for y in range(0, 600):
        walls.append(Wall(0, y))
    for y in range(0, 600):
        walls.append(Wall(760, y))

    running = True

    d = 5
    FPS = 60

    clock = pygame.time.Clock()

    while running:
        clock.tick(snake1.speed)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d

                if event.key == pygame.K_d and snake2.dx != -d:
                    snake2.dx = d
                    snake2.dy = 0
                if event.key == pygame.K_a and snake2.dx != d:
                    snake2.dx = -d
                    snake2.dy = 0
                if event.key == pygame.K_w and snake2.dy != d:
                    snake2.dx = 0
                    snake2.dy = -d
                if event.key == pygame.K_s and snake2.dy != -d:
                    snake2.dx = 0
                    snake2.dy = d
                if event.key == pygame.K_k:
                    save2(snake1, snake2, difficult)
                    running = False
        if snake1.elements[-1][0] > 740 or snake1.elements[-1][0] < 50:
            running = False
        if snake1.elements[0][-1] > 540 or snake1.elements[0][-1] < 50:
            running = False
        if snake2.elements[-1][0] > 740 or snake2.elements[-1][0] < 50:
            running = False
        if snake2.elements[0][-1] > 540 or snake2.elements[0][-1] < 50:
            running = False
        
        if snake1.eat(food.x, food.y):
            snake1.is_add = True
            food.gen()

        if snake2.eat(food.x, food.y):
            snake2.is_add = True
            food.gen()

        snake1.move()
        snake2.move()
        snake1.draw()
        snake2.draw()
        for wall in walls:
            wall.draw()
        food.draw()
        pygame.display.flip()


show_menu()
# pygame.display.flip()
pygame.quit()
