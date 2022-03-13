import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

pygame.mixer.music.load('prosti.mp3')
pygame.mixer.music.play(15)

#pygame.mixer.music.play(-1) beskonechno
#pygame.mixer.music.stop()
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == SONG_END:
			print('Song Ended')
	screen.fill((255, 255, 255))
	pygame.display.flip()

pygame.quit()