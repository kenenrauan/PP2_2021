import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 400))

_image_library = {}

def get_image(path):
	global _image_library
	image = _image_library.get(path)
	if image is None:
		_path = path.replace('/', os.sep)
		image = pygame.image.load(_path)
		_image_library[path] = image
	return image


done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))
	screen.blit(get_image('page.png'), (120, 100))
	pygame.display.flip()

pygame.quit()