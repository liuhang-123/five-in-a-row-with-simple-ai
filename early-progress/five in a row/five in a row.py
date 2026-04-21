import numpy as np
import pygame
from ai_ import Five
mode='ai'
five=Five()
def run_():
		five.draw_lines()
		
		while five.running == True:
			five.check_event()
			pygame.display.flip()
			if mode=='ai':
				for loc,seed in five.points:
					if seed ==0:
						
						seed=1
run_()
points=five.points
a=[]
for y,z in points:
	print(z)

	
