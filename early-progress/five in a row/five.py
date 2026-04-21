import pygame
colors={'CRIMSON':[220,20,60],'WHITE':[255,255,255],'BLACK':[0,0,0],'PINK':[255,192,203],'BLUE':[0,0,255],'LIME':[0,255,0],'GOLDENROD':[218,165,32],'NAVAJOWHITE':[255,222,173]}

Bools=[False,True]
class Five:
	def __init__(self):
		pygame.init()
		self.board_color=colors['NAVAJOWHITE']
		self.screen = pygame.display.set_mode((740,740))
		self.running = True
		self.screen_w = self.screen.get_rect().width
		self.screen.fill([218,165,32])
		self.screen_h = self.screen.get_rect().height
		self.baord_rect = pygame.Rect(0,0,740,740)
		self.baord = pygame.draw.rect(self.screen,self.board_color,self.baord_rect,100)
		self.x,self.s,self.baord_h, self.baord_w = self.baord_rect
		self.s = []
		self.t = []
		self.bool_c=0
		self.points = []
		self.point_list = []
		self.mouse_pos = pygame.mouse.get_pos()
		self.round = 0
		self.init_ = 0
		self.draws = []
		self.settings=False

		self.settings_im=pygame.image.load('images/settings.png')
		self.im_rect=self.settings_im.get_rect()
		self.crowd =[]
		self.withdraw = True
	
		self.re = []
	
		
		#361 19*19

	def run_(self):
		self.draw_lines()
		
		#self.draw_seed()
		while self.running == True:
			self.check_event()
			
					
			pygame.display.flip()



			
	def draw_lines(self):

		hor_line = 19
		ver_line = 19
		for x in list(range(hor_line)):
			w = pygame.draw.rect(self.screen,[255,255,255],[100,100+x*30,self.baord_w-200,1],0)
			if self.init_ == 0:
				self.s.append(100+x*30)
			
		for x in list(range(ver_line)):
			w = pygame.draw.rect(self.screen,[255,255,255],[100+x*30,100,1,self.baord_h-200],0)
			if self.init_==0:
				self.t.append(100+x*30)

			
		if self.init_ == 0:
			for t in self.t:
				for s in self.s:
					self.points.append([[s,t],0])
			
		
					
			
			
		
		self.init_ = 1
		

		pygame.draw.circle(self.screen,[0,0,0],[550, 190],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[550,550],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[190,550],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[190,190],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[self.screen_h/2, self.screen_w/2],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[370,190],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[370,550],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[550,370],3,0)
		pygame.draw.circle(self.screen,[0,0,0],[190,370],3,0)

	def draw_items(self):
		self.screen.blit(self.settings_im,self.im_rect)
	def draw_seed(self):
		
		for d in self.point_list:
			pygame.draw.circle(d[0],d[1],d[2],d[3],d[4])
			
		#                                                radius,fill or line thickness
	
	def init_baord(self):
		pass
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:			
				self.running = False	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE and self.settings==False:
					if self.withdraw == True:
						
						self.withdraw_()
						
				#			print('withdraw forbiden')
					else:
						print('game over,no withdraw')
				
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				self.mouse_pos = pygame.mouse.get_pos()
				
				if self.mouse_pos[0] in range(0,40) and self.mouse_pos[1] in range(0,40):
					self.bool_c+=1
					self.settings=Bools[self.bool_c%2]
					if self.settings==False:
						self.screen.fill([218,165,32])
						self.baord = pygame.draw.rect(self.screen,self.board_color,self.baord_rect,100)
						self.draw_lines()
						self.draw_seed()
				if self.settings==False:	
					for points in self.points:
				
					

						if 5 >= abs(self.mouse_pos[0] - points[0][0]) and 5 >= abs(self.mouse_pos[1]-points[0][1]) and points[1] == 0:	
							zz = str(points)
							sss = eval(zz)
							self.draws.append(sss)
					
					
						
							if self.round == 1:
								p = [self.screen,[225,235,240],[points[0][0],points[0][1]],11,0]
								self.round = 0																
								points[-1] = 1


						
							else:
								p = [self.screen,[50,50,50],[points[0][0],points[0][1]],11,0]
								self.round = 1							
								points[-1] = 2
							
							self.point_list.append(p)
					
							self.draw_seed()
						
							self.re.append(points)
						

							try:
								self.judge()
							except:
								pass
				if self.settings==True:
					pygame.draw.rect(self.screen,[254,225,253],[0,0,self.screen_w,self.screen_h/2])
					
					
					
						
		self.draw_items()
						
				
					
						
						

	

	def withdraw_(self):
		
		if len(self.point_list)>1:
			self.draws = self.draws[:]
			
			self.index = self.points.index(self.re[-1])
			self.index_2 = self.points.index(self.re[-2])
			self.points.remove(self.points[self.index])
			self.points.insert(self.index,self.draws[-1])
			self.points.remove(self.points[self.index_2])
			self.points.insert(self.index_2,self.draws[-2])
			self.re.remove(self.re[-1])
			self.re.remove(self.re[-1])
			self.draws.remove(self.draws[-1])
			self.draws.remove(self.draws[-1])
			
		
			
		

			
	
			self.point_list.remove(self.point_list[-1])
			self.point_list.remove(self.point_list[-1])
			self.screen.fill([218,165,32])
			self.baord = pygame.draw.rect(self.screen,self.board_color,self.baord_rect,100)
			self.draw_lines()
			self.draw_seed()
	def judge(self):
		self.jz = -1
		for points in self.points:
			self.jz +=1
			if points[1] ==1:
				if self.points[self.jz+1][1] ==1:
					if self.points[self.jz+2][1] ==1:
						if self.points[self.jz+3][1] ==1:
							if self.points[self.jz+4][1] ==1 and points[0][1] == self.points[self.jz+1][0][1] and points[0][1] == self.points[self.jz+2][0][1] and points[0][1] == self.points[self.jz+3][0][1] and points[0][1] == self.points[self.jz+4][0][1]:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+1][0][0],self.points[self.jz+1][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+2][0][0],self.points[self.jz+2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+3][0][0],self.points[self.jz+3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+4][0][0],self.points[self.jz+4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+19][1]==1:
					if self.points[self.jz+19*2][1]==1:
						if self.points[self.jz+19*3][1]==1:
							if self.points[self.jz+19*4][1]==1:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19][0][0],self.points[self.jz+19][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*2][0][0],self.points[self.jz+19*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*3][0][0],self.points[self.jz+19*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*4][0][0],self.points[self.jz+19*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+18][1]==1:
					if self.points[self.jz+18*2][1]==1:
						if self.points[self.jz+18*3][1]==1:
							if self.points[self.jz+18*4][1]==1 and self.points[self.jz+18][0][0] == points[0][0] -30 and self.points[self.jz+18*2][0][0] == self.points[self.jz+18][0][0]-30 and self.points[self.jz+18*3][0][0] == self.points[self.jz+18*2][0][0]-30 and self.points[self.jz+18*4][0][0] == self.points[self.jz+18*3][0][0]-30:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18][0][0],self.points[self.jz+18][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*2][0][0],self.points[self.jz+18*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*3][0][0],self.points[self.jz+18*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*4][0][0],self.points[self.jz+18*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+20][1]==1:
					if self.points[self.jz+20*2][1]==1:
						if self.points[self.jz+20*3][1]==1:
							if self.points[self.jz+20*4][1]==1 and self.points[self.jz+20][0][0] == points[0][0] +30 and self.points[self.jz+20*2][0][0] == self.points[self.jz+20][0][0]+30 and self.points[self.jz+20*3][0][0] == self.points[self.jz+20*2][0][0]+30 and self.points[self.jz+20*4][0][0] == self.points[self.jz+20*3][0][0]+30:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20][0][0],self.points[self.jz+20][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*2][0][0],self.points[self.jz+20*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*3][0][0],self.points[self.jz+20*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*4][0][0],self.points[self.jz+20*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
			
			if points[1] ==2:
				if self.points[self.jz+1][1] ==2:
					if self.points[self.jz+2][1] ==2:
						if self.points[self.jz+3][1] ==2:
							if self.points[self.jz+4][1] ==2 and points[0][1] == self.points[self.jz+1][0][1] and points[0][1] == self.points[self.jz+2][0][1] and points[0][1] == self.points[self.jz+3][0][1] and points[0][1] == self.points[self.jz+4][0][1]:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+1][0][0],self.points[self.jz+1][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+2][0][0],self.points[self.jz+2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+3][0][0],self.points[self.jz+3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+4][0][0],self.points[self.jz+4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+19][1]==2:
					if self.points[self.jz+19*2][1]==2:
						if self.points[self.jz+19*3][1]==2:
							if self.points[self.jz+19*4][1]==2:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19][0][0],self.points[self.jz+19][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*2][0][0],self.points[self.jz+19*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*3][0][0],self.points[self.jz+19*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+19*4][0][0],self.points[self.jz+19*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+18][1]==2:
					if self.points[self.jz+18*2][1]==2:
						if self.points[self.jz+18*3][1]==2:
							if self.points[self.jz+18*4][1]==2 and self.points[self.jz+18][0][0] == points[0][0] -30 and self.points[self.jz+18*2][0][0] == self.points[self.jz+18][0][0]-30 and self.points[self.jz+18*3][0][0] == self.points[self.jz+18*2][0][0]-30 and self.points[self.jz+18*4][0][0] == self.points[self.jz+18*3][0][0]-30:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18][0][0],self.points[self.jz+18][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*2][0][0],self.points[self.jz+18*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*3][0][0],self.points[self.jz+18*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+18*4][0][0],self.points[self.jz+18*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False
				if self.points[self.jz+20][1]==2:
					if self.points[self.jz+20*2][1]==2:
						if self.points[self.jz+20*3][1]==2:
							if self.points[self.jz+20*4][1]==2 and self.points[self.jz+20][0][0] == points[0][0] +30 and self.points[self.jz+20*2][0][0] == self.points[self.jz+20][0][0]+30 and self.points[self.jz+20*3][0][0] == self.points[self.jz+20*2][0][0]+30 and self.points[self.jz+20*4][0][0] == self.points[self.jz+20*3][0][0]+30:
								self.point_list.append([self.screen,[255,0,0],[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20][0][0],self.points[self.jz+20][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*2][0][0],self.points[self.jz+20*2][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*3][0][0],self.points[self.jz+20*3][0][1]],9,0])
								self.point_list.append([self.screen,[255,0,0],[self.points[self.jz+20*4][0][0],self.points[self.jz+20*4][0][1]],9,0])
								self.draw_seed()
								self.withdraw = False							
x=Five()
x.run_()
pygame.quit()
