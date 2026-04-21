'''import pygame
import random
import math
class Mine:
	code = 233286
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((722,722))
		self.running = True
		self.screen_w = self.screen.get_rect().width
		self.screen.fill([218,165,32])
		self.screen_h = self.screen.get_rect().height
		self.init_ = 0
		self.s = []
		self.t=[]
		self.points=[]
		self.bombs=[]
		self.bomb_n=200
		self.action=True
		self.font = pygame.font.SysFont('freesanbold.ttf',30)
		
		self.screen.blit(self.font.render('',True,(100,145,255)),(600,600))
	def draw_lines(self):

		hor_line = self.screen_h//30
		ver_line = self.screen_w//30
		for x in list(range(hor_line)):
			w = pygame.draw.rect(self.screen,[255,255,25],[0,x*30,self.screen_w-31,1],0)
			if self.init_ == 0:
				self.s.append(range(x*30,x*30+29))
			
		for x in list(range(ver_line)):
			w = pygame.draw.rect(self.screen,[255,255,25],[x*30,0,1,self.screen_h-31],0)
			if self.init_==0:
				self.t.append(range(x*30,x*30+29))
			
		if self.init_ == 0:
			for t in self.t:
				for s in self.s:
					self.points.append([[s,t],0,0])
					for points in self.points:
						if 718 in points[0][0] or 718 in points[0][1]:
							self.points.remove(points)
			self.p_len = len(self.points)
			print(self.p_len)
			for a in range(1,self.p_len+1):
				if self.bomb_n>0:
					a=1
				if self.bomb_n<=0:
					a=0
				self.bombs.append(a)
				self.bomb_n=self.bomb_n-1
			random.shuffle(self.bombs)
			self.n=0
			for points in self.points:
				points[1]=self.bombs[self.n]
				self.n = self.n+1
				pygame.draw.rect(self.screen,[225,235,0],[points[0][0][0],points[0][1][0],28,28],0)
			print(self.points)
			print(self.bombs)

		self.init_ = 1
	def run(self):
		self.draw_lines()
		while self.running:
			self.check_event()
			pygame.display.flip()
	
	
		
	
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:			
				self.running = False	
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.mouse_pos = pygame.mouse.get_pos()
				loc_=0
				hint=[]
				for points in self.points:
					

					if self.mouse_pos[0] in points[0][0] and self.mouse_pos[1] in points[0][1]: #and self.action==True:
						if points[1] == 0:

							pygame.draw.rect(self.screen,[218,165,32],[points[0][0][0],points[0][1][0],28,28],0)
							
							try:
								
								if self.points[loc_-1][1]==1 and self.points[loc_-1][0][0][0]==points[0][0][0]-30:
									hint.append(1)
							except:
								pass
							try:	
								if self.points[loc_-int(math.sqrt(len(self.points)))][1]==1 and self.points[loc_-int(math.sqrt(len(self.points)))][0][0][0]==points[0][0][0]:
									hint.append(1)
							except:
								pass
							try:
								if self.points[loc_-int(math.sqrt(len(self.points)))+1][1]==1 and self.points[loc_-int(math.sqrt(len(self.points)))+1][0][0][0]==points[0][0][0]+30:
									hint.append(1)
							except:
								pass
							try:
								if self.points[loc_-int(math.sqrt(len(self.points)))-1][1]==1 and self.points[loc_-int(math.sqrt(len(self.points)))-1][0][0][0]==points[0][0][0]-30:
									hint.append(1)
							except:
								pass	
							try:
								if self.points[loc_+1][1]==1 and self.points[loc_+1][0][0][0]==points[0][0][0]+30:
									hint.append(1)
							except:
								pass
							try:
								if self.points[loc_+int(math.sqrt(len(self.points)))-1][1]==1 and self.points[loc_+int(math.sqrt(len(self.points)))-1][0][0][0]==points[0][0][0]-30:
									hint.append(1)
							except:
								pass	
							try:
								if self.points[loc_+int(math.sqrt(len(self.points)))+1][1]==1 and self.points[loc_+int(math.sqrt(len(self.points)))+1][0][0][0]==points[0][0][0]+30:
									hint.append(1)
							except:
								pass
							try:
								if self.points[loc_+int(math.sqrt(len(self.points)))][1]==1 and self.points[loc_+int(math.sqrt(len(self.points)))][0][0][0]==points[0][0][0]:
									hint.append(1)
							except:
								pass
							self.screen.blit(self.font.render(f'{len(hint)}',True,(100,145,255)),(points[0][0][10],points[0][1][10]))

									
							
							
						if points[1] == 1:
							for points in self.points:
								if points[1]==1:
									pygame.draw.rect(self.screen,[225,0,0],[points[0][0][0],points[0][1][0],28,28],0)
							self.action=False
					loc_=loc_+1
				

mine = Mine()
mine.run()'''
from pynput.mouse import Controller,Button
mouse=Controller()
mouse
mouse.click(Button.left)