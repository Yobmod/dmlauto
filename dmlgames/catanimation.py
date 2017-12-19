import os
import pygame		# type: ignore
import time
from pygame.locals import QUIT		# type: ignore
import sys

os.chdir(r'.')
pygame.init()

FPS: int = 30  # frames per second setting
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')


soundObj = pygame.mixer.Sound('match0.wav')


def loop() -> None:
	catx = 50
	caty = 20
	direction = 'right'
	while True:  # the main game loop
		DISPLAYSURF.fill(WHITE)
		if direction == 'right':
			catx += 5
			if catx == 350:
				direction = 'down'
				soundObj.play()
				time.sleep(0.5)  # wait and let the sound play for 1 second
				soundObj.stop()
		elif direction == 'down':
			caty += 5
			if caty == 220:
				direction = 'left'
		elif direction == 'left':
			catx -= 5
			if catx == 10:
				direction = 'up'
		elif direction == 'up':
			caty -= 5
			if caty == 10:
				direction = 'right'

		DISPLAYSURF.blit(catImg, (catx, caty))
		pygame.display.update()
		fpsClock.tick(FPS)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


def main_loop() -> None:
	loop()


main_loop()
