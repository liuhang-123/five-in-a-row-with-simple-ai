import pygame
import random
import tkinter as tk
class Five:
	def __init__(self):
		pygame.init()
		self.choice_mode=tk.Tk()
		self.b1=tk.Button(self.choice_mode,text='you vs ai',command=self.ai_mo)
		self.b2=tk.Button(self.choice_mode,text='left hand vs right hand',command=self.hand_mo)
		self.b1.pack()
		self.b2.pack()
		self.choice_mode.mainloop()
		self.screen = pygame.display.set_mode((740,740))
		self.running = True
		self.screen_w = self.screen.get_rect().width
		self.screen.fill([218,165,32])
		self.screen_h = self.screen.get_rect().height
		self.baord_rect = pygame.Rect(0,0,740,740)
		self.baord = pygame.draw.rect(self.screen,[255,222,173],self.baord_rect,100)
		self.x,self.s,self.baord_h, self.baord_w = self.baord_rect
		self.s = []
		self.t = []
		self.points = []
		self.point_list = []
		self.mouse_pos = pygame.mouse.get_pos()
		self.round = 1
		self.init_ = 0
		self.draws = []
		self.crowd =[]
		self.seed_size=12
		self.dec_w = ''
		#self.mode="ai"
		self.withdraw = True
		pygame.mixer.music.load('down.mp3')
		pygame.mixer.music.play()
		self.re = []
		self.ai_def_att_mode=[1,2]
		self.win_color=[250,250,0]
		
		self.directions_=[[+1,+2,+3,+4],[-1,-2,-3,-4],[+19,+19*2,+19*3,+19*4],[-19,-19*2,-19*3,-19*4],[+18,+18*2,+18*3,+18*4],[-18,-18*2,-18*3,-18*4],[+20,+20*2,+20*3,+20*4],[-20,-20*2,-20*3,-20*4]]
		
		
		#361 19*19
	def ai_mo(self):
		self.mode='ai'
		self.choice_mode.destroy()
	def hand_mo(self):
		self.mode='hand'
		self.choice_mode.destroy()
	def run_(self):
		self.draw_lines()
		
		while self.running == True:
			
			if self.check_event():
				pygame.display.flip()
				if self.withdraw==True and self.mode=="ai":

					self.ai_turn()
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
			for x in range(0,222):
				self.points.append([[1000,1000],0])

			
		
					
			
			
		
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

	def draw_seed(self):
		
		for d in self.point_list:
			pygame.draw.circle(d[0],d[1],d[2],d[3],d[4])
		
			
		#                                                radius,fill or line thickness
	'''def draw_white(self):
		pygmae.draw.rect(self.screen,[0,255,0],[100,10],5,0)
		pygame.mixer.music.play()'''

	
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:			
				self.running = False	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					if self.withdraw == True:
						
						self.withdraw_()
						
				#			print('withdraw forbiden')
					else:
						print('game over,no withdraw')
				
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				self.mouse_pos = pygame.mouse.get_pos()
				

				for points in self.points:
				
					

					if 7 >= abs(self.mouse_pos[0] - points[0][0]) and 7 >= abs(self.mouse_pos[1]-points[0][1]) and points[1] == 0 and self.withdraw==True:	
						
						#print(self.points)
						zz = str(points)
						sss = eval(zz)
						self.draws.append(sss)
					
					
						
						if self.round == 1 or self.mode=="ai":
							p = [self.screen,[50,50,50],[points[0][0],points[0][1]],self.seed_size,0]
							self.round = 0																
							points[-1] = 1


						
						elif self.mode!="ai":
							p = [self.screen,[225,235,240],[points[0][0],points[0][1]],self.seed_size,0]
							self.round = 1							
							points[-1] = 2
							
						self.point_list.append(p)
					
						self.draw_seed()
						pygame.mixer.music.play()
					
						self.re.append(points)

						try:
							self.judge()
						except:
							pass		

						return True		


	def ai_turn(self):
		#self.ai_think()
		#jz is position of points in self.points
		
		
		print(len(self.points[:-222]))
		
		pplist=[]
		
		self.jz = -1

		for points in self.points[:-222]:

			self.jz +=1
			pppp=0
			
			for mode in self.ai_def_att_mode[:2]:
				if points[1]==0:

					points[1] =mode
					for dire in self.directions_:
						
						

							
						#first level		
						if self.points[self.jz + dire[0]][1] ==mode:

							pppp+=10
							if self.points[self.jz-dire[0]][1]==mode*-1+3:
								pppp-=5
								if self.points[self.jz+(dire[0]*3)][1]==mode*-1 +3:
									pppp-=5
							elif self.points[self.jz-dire[0]][1]==0 and self.points[self.jz+dire[0]*2][1]==0:
								pppp+=40

							#second level
							if self.points[self.jz +dire[1]][1] ==mode or self.points[self.jz-dire[1]][1]==mode:
								
								pppp+=500
								if self.points[self.jz-dire[0]][1]==mode*-1+3:
									pppp-=250
									if self.points[self.jz+(dire[0]*4)][1]==mode*-1 +3:
										pppp-=280
								elif self.points[self.jz-dire[0]][1]==mode:
									pppp+=900
									if self.points[self.jz-dire[0]*2][1]==mode*-1 +3:
										pppp-=340
									elif self.points[self.jz-dire[0]*2][1]==mode:
										pppp+=6000
										if self.points[self.jz-dire[0]*3][1]==mode:
											pppp-=1000
								
								elif mode==1:
									pppp+=100
									if self.points[self.jz-dire[0]][1]==mode*-1+3:
										pppp-=70
										if self.points[self.jz+(dire[0]*4)][1]==mode*-1 +3:
											pppp-=30
									elif self.points[self.jz-dire[0]][1]==mode:
										pppp+=600
										if self.points[self.jz-dire[0]*2][1]==mode*-1 +3:
											pppp-=350
										elif self.points[self.jz-dire[0]*2][1]==mode:
											pppp+=1000
											if self.points[self.jz-dire[0]*3][1]==mode*-1+3:
												pppp-=600
											elif self.points[self.jz-dire[0]*3][1]==mode:
												pppp+=10000
								#third level
								if self.points[self.jz + dire[2]][1] ==mode:
									if mode==2:
										pppp+=5000
									pppp+=5000
									if self.points[self.jz-dire[0]][1]==mode*-1+3:
										if mode==2:
											pppp-=4000
										pppp-=4000
										if self.points[self.jz+(dire[0]*5)][1]==mode*-1 +3:
											if mode==2:
												pppp-=1000
											pppp-=200
									elif self.points[self.jz-dire[0]][1]==mode:
										if mode==2:
											pppp+=2000
										pppp+=6000
										if self.points[self.jz-dire[0]*2][1]==mode*-1 +3:
											if mode==2:
												pppp-=1400
											pppp-=500
										elif self.points[self.jz-dire[0]*2][1]==mode:
											if mode==2:
												pppp+=9000
											pppp+=10000
											if self.points[self.jz-dire[0]*3][1]==mode*-1+3:
												if mode==2:
													pppp-=8000
												pppp-=9000
											elif self.points[self.jz-dire[0]*3][1]==mode:
												if mode==2:
													pppp+=10000
												pppp+=1000

									#fourth level
									if self.points[self.jz + dire[3]][1] ==mode:

										if mode==2:
											pppp+=5000000
										else:
											pppp+=400000

								#if self.points[self.jz+4][1] ==1 and points[0][1] == self.points[self.jz+1][0][1] and points[0][1] == self.points[self.jz+2][0][1] and points[0][1] == self.points[self.jz+3][0][1] and points[0][1] == self.points[self.jz+4][0][1]:
					points[1]=0
			pplist.append(pppp)				
								
					
		
													
				
		

		print(max(pplist))
		loc_of_max_pp_inpplist=pplist.index(max(pplist))
		print(loc_of_max_pp_inpplist)
		points=self.points[loc_of_max_pp_inpplist]				

		zz = str(points)
		sss = eval(zz)
		self.draws.append(sss)
					
							
		p = [self.screen,[225,235,240],[points[0][0],points[0][1]],self.seed_size,0]
																		
		points[-1] = 2


						
		
						
		self.point_list.append(p)
					
		self.draw_seed()

		pygame.mixer.music.play()
					
		self.re.append(points)
		
		self.judge()
		
		
	

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
			self.baord = pygame.draw.rect(self.screen,[255,222,173],self.baord_rect,100)
			self.draw_lines()
			self.draw_seed()

		#else:
		#	if len(self.point_list)==1:
		#		showinfo(title='info',message='why do you withdraw the only seed?\nwe need it to continue the game')
		#	else:				
		#		showinfo(title='info',message='how can you withdraw the chess board!')
	
	def judge(self):
		self.jz = -1
		for points in self.points:
			self.jz +=1
			if points[1] ==1:
				if self.points[self.jz+1][1] ==1:
					if self.points[self.jz+2][1] ==1:
						if self.points[self.jz+3][1] ==1:
							if self.points[self.jz+4][1] ==1 and points[0][1] == self.points[self.jz+1][0][1] and points[0][1] == self.points[self.jz+2][0][1] and points[0][1] == self.points[self.jz+3][0][1] and points[0][1] == self.points[self.jz+4][0][1]:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+1][0][0],self.points[self.jz+1][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+2][0][0],self.points[self.jz+2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+3][0][0],self.points[self.jz+3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+4][0][0],self.points[self.jz+4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'black win'
								#showinfo(title='info',message='white win!')
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+19][1]==1:
					if self.points[self.jz+19*2][1]==1:
						if self.points[self.jz+19*3][1]==1:
							if self.points[self.jz+19*4][1]==1:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19][0][0],self.points[self.jz+19][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*2][0][0],self.points[self.jz+19*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*3][0][0],self.points[self.jz+19*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*4][0][0],self.points[self.jz+19*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'black win'
								#showinfo(title='info',message='white win!')
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+18][1]==1:
					if self.points[self.jz+18*2][1]==1:
						if self.points[self.jz+18*3][1]==1:
							if self.points[self.jz+18*4][1]==1 and self.points[self.jz+18][0][0] == points[0][0] -30 and self.points[self.jz+18*2][0][0] == self.points[self.jz+18][0][0]-30 and self.points[self.jz+18*3][0][0] == self.points[self.jz+18*2][0][0]-30 and self.points[self.jz+18*4][0][0] == self.points[self.jz+18*3][0][0]-30:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18][0][0],self.points[self.jz+18][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*2][0][0],self.points[self.jz+18*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*3][0][0],self.points[self.jz+18*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*4][0][0],self.points[self.jz+18*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'black win'
								#showinfo(title='info',message='white win!')
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+20][1]==1:
					if self.points[self.jz+20*2][1]==1:
						if self.points[self.jz+20*3][1]==1:
							if self.points[self.jz+20*4][1]==1 and self.points[self.jz+20][0][0] == points[0][0] +30 and self.points[self.jz+20*2][0][0] == self.points[self.jz+20][0][0]+30 and self.points[self.jz+20*3][0][0] == self.points[self.jz+20*2][0][0]+30 and self.points[self.jz+20*4][0][0] == self.points[self.jz+20*3][0][0]+30:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20][0][0],self.points[self.jz+20][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*2][0][0],self.points[self.jz+20*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*3][0][0],self.points[self.jz+20*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*4][0][0],self.points[self.jz+20*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'black win'

								#showinfo(title='info',message='white win!')
								self.enclose()
								self.withdraw = False
			
			if points[1] ==2:
				if self.points[self.jz+1][1] ==2:
					if self.points[self.jz+2][1] ==2:
						if self.points[self.jz+3][1] ==2:
							if self.points[self.jz+4][1] ==2 and points[0][1] == self.points[self.jz+1][0][1] and points[0][1] == self.points[self.jz+2][0][1] and points[0][1] == self.points[self.jz+3][0][1] and points[0][1] == self.points[self.jz+4][0][1]:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+1][0][0],self.points[self.jz+1][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+2][0][0],self.points[self.jz+2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+3][0][0],self.points[self.jz+3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+4][0][0],self.points[self.jz+4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'white win'
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+19][1]==2:
					if self.points[self.jz+19*2][1]==2:
						if self.points[self.jz+19*3][1]==2:
							if self.points[self.jz+19*4][1]==2:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19][0][0],self.points[self.jz+19][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*2][0][0],self.points[self.jz+19*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*3][0][0],self.points[self.jz+19*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+19*4][0][0],self.points[self.jz+19*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'white win'
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+18][1]==2:
					if self.points[self.jz+18*2][1]==2:
						if self.points[self.jz+18*3][1]==2:
							if self.points[self.jz+18*4][1]==2 and self.points[self.jz+18][0][0] == points[0][0] -30 and self.points[self.jz+18*2][0][0] == self.points[self.jz+18][0][0]-30 and self.points[self.jz+18*3][0][0] == self.points[self.jz+18*2][0][0]-30 and self.points[self.jz+18*4][0][0] == self.points[self.jz+18*3][0][0]-30:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18][0][0],self.points[self.jz+18][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*2][0][0],self.points[self.jz+18*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*3][0][0],self.points[self.jz+18*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+18*4][0][0],self.points[self.jz+18*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'white win'
								self.enclose()
								self.withdraw = False
				if self.points[self.jz+20][1]==2:
					if self.points[self.jz+20*2][1]==2:
						if self.points[self.jz+20*3][1]==2:
							if self.points[self.jz+20*4][1]==2 and self.points[self.jz+20][0][0] == points[0][0] +30 and self.points[self.jz+20*2][0][0] == self.points[self.jz+20][0][0]+30 and self.points[self.jz+20*3][0][0] == self.points[self.jz+20*2][0][0]+30 and self.points[self.jz+20*4][0][0] == self.points[self.jz+20*3][0][0]+30:
								self.point_list.append([self.screen,self.win_color,[points[0][0],points[0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20][0][0],self.points[self.jz+20][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*2][0][0],self.points[self.jz+20*2][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*3][0][0],self.points[self.jz+20*3][0][1]],9,0])
								self.point_list.append([self.screen,self.win_color,[self.points[self.jz+20*4][0][0],self.points[self.jz+20*4][0][1]],9,0])
								self.draw_seed()
								self.dec_w = 'white win'
								self.enclose()
								self.withdraw = False
	def enclose(self):
		font = pygame.font.SysFont('freesanbold.ttf',60)
		if self.dec_w=='white win':
			text = font.render(self.dec_w,True,(225,235,240))
		else:
			text=font.render(self.dec_w,True,(50,50,50))
		self.screen.blit(text,(self.screen_w/2-75,50))


x=Five()
x.run_()