import pygame
from pygame.locals import *
import time

if __name__=="__main__":
	pygame.init()

	surface=pygame.display.set_mode((500,500))
	flag=True
	while flag:
		for event in pygame.event.get():
			if event.type ==KEYDOWN :
				if event.type ==K_ESCAPE:
					
