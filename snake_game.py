import pygame
from pygame.locals import *
import time

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
			elif event.type==QUIT:
				flag=False