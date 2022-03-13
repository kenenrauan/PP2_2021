import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
C = (100, 100, 100)

size = (400, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame example")

PI = 3.14

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(WHITE)
	pygame.draw.line(screen, BLUE, [0, 0], [100, 100], 5)

	for y in range(0, 100, 10):
		pygame.draw.line(screen, RED, [0, 10 + y], [100, 110 + y], 2)
	#rectangle
	pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
	#ellipse
	pygame.draw.ellipse(screen, GREEN, [20, 100, 250, 100], 2)
	#arc
	pygame.draw.arc(screen, C, [20, 200, 250, 100], 0, PI / 2, 2)
	pygame.draw.arc(screen, GREEN, [20, 200, 250, 100], PI/2 ,PI, 2)
	pygame.draw.arc(screen, RED, [20, 200, 250, 100], PI, 3 * PI / 2, 2)
	pygame.draw.arc(screen, BLUE, [20, 200, 250, 100], 3 * PI / 2, 2 * PI, 2)

	#text
	font = pygame.font.Font(None, 50)
	text1 = font.render("My text", True, RED)
	text2 = font.render("My text", False, GREEN)
	screen.blit(text1, (250, 250))
	screen.blit(text2, (250, 300))

	font = pygame.font.SysFont('Times New Roman', 25, True, False)
	text = font.render("Programming Tech", True, BLACK)
	text = pygame.transform.rotate(text, 90)
	screen.blit(text, (0, 0))
	pygame.display.flip()
pygame.quit()