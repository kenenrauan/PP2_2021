import pygame

screen = pygame.display.set_mode((300, 200))
surf = pygame.Surface((200, 150))
surf.fill((255, 255, 255))
surf.set_alpha(200)

pygame.draw.rect(screen, (0, 255, 0), (0, 80, 300, 40))
screen.blit(surf, (50, 25))

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
pygame.quit()

