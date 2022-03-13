import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0)) #white

pygame.draw.rect(screen, (0, 100, 100), (20,30,100,100), 5) #x, y, width, height

done = False
while not done:
	# draw smth
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pygame.display.flip()

pygame.quit()


