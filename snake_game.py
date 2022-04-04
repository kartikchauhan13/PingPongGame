import pygame
from pygame.locals import *
import time

def draw():
	surface.fill((255,255,0))
	surface.blit(block, (block_x,block_y))
	pygame.display.flip()

if __name__=="__main__":
	pygame.init()

	surface=pygame.display.set_mode((500,500))
	surface.fill((255,255,0))

	block=pygame.image.load("images/square-16.jpg").convert()
	block_x=100
	block_y=100
	surface.blit(block, (block_x,block_y))

	pygame.display.flip()
	flag=True
	while flag:
		for event in pygame.event.get():
			if event.type ==KEYDOWN :
				if event.key ==K_ESCAPE:
					flag=False
				if event.key ==K_UP:
					block_y -=10
					draw()
				if event.key ==K_DOWN:
					block_y +=10
					draw()
				if event.key ==K_LEFT:
					block_x -=10
					draw()
				if event.key ==K_RIGHT:
					block_x +=10
					draw()
			elif event.type==pygame.QUIT:
				flag=False