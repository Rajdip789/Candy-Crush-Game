import pygame as pg
import random

width = 0
height = 0
screen = None

font = None
score = '0'
moves = '0'
target = '0'

g_state = 0

rows = 10
cols = 10
grid_obj = []

def welcomeScreen():
	global width
	global font
	
	screen.blit(pg.image.load('assets/background.jpeg'),(0,0))

	font = pg.font.Font("MochiyPopPOne-Regular.ttf", 33)
	screen.blit(font.render("By Rajdip", True, (0,0,0)), (width-352, 420))
	screen.blit(font.render("By Rajdip", True, (51,122,58)), (width-350, 420))

	font = pg.font.Font("MochiyPopPOne-Regular.ttf", 23)
	tarr = ["Score Board","New Game","Exit Game"]
	pos = pg.mouse.get_pos()
	for i in range(1,4):
		col1 = ()
		col2 = ()
		col3 = ()
		if (pos[0] >= width/3*i - 300 and pos[0] <= width/3*i - 100) and (pos[1] >= 525 and pos[1] <= 585):
			col1 = (168, 50, 107)
			col2 = (51, 0, 0)
			col3 = (255, 102, 0)
		else:
			col1 = (248, 7, 49)
			col2 = (66, 40, 16)
			col3 = (244,209,75)

		pg.draw.rect(screen,col1,(width/3*i - 300,525,200,60),border_radius=height//2)
		pg.draw.rect(screen,col2,(width/3*i - 300,525,200,60),3,border_radius=height//2)
		screen.blit(font.render(tarr[i-1], True, (0,0,0)), (width/3*i - 279 if (i==1) else width/3*i - 269, 535))
		screen.blit(font.render(tarr[i-1], True, col3), (width/3*i - 280 if (i==1) else width/3*i - 270, 535))

def scoreboard():
	print("showing scoreboard")

def initgame():
	global rows
	global cols
	global grid_obj

	for i in range(rows):
		temp = []
		for j in range(cols):
			obj = Candy(random.randint(0,5),0)
			temp.append(obj)
		grid_obj.append(temp)

def game():
	global width
	global height
	global font
	global score
	global moves
	global target
	global g_state

	global rows
	global cols
	global grid_obj

	font = pg.font.Font("MochiyPopPOne-Regular.ttf", 28)

	screen.blit(pg.image.load('assets/game_bg.jpeg'),(0,0))

	c1_arr = [(171, 110, 48),(51, 204, 51),(0, 153, 204)]
	c2_arr = [(95, 22, 22),(0, 102, 0),(0, 51, 204)]
	t1_arr = ["Score","Moves","Target"]
	t2_arr = []
	t2_arr = [*t2_arr, score, moves, target]
	
	for i in range(1,4):
		pg.draw.rect(screen,c2_arr[i-1],(25,height/4.5*i-70,450,75),border_radius=15)
		pg.draw.rect(screen,(0,0,0),(25,height/4.5*i-70,450,75),2,border_radius=15)
		pg.draw.rect(screen,c1_arr[i-1],(25,height/4.5*i-70,150,75),border_radius=15)
		pg.draw.rect(screen,(0,0,0),(25,height/4.5*i-70,150,75),2,border_radius=15)

		screen.blit(font.render(t1_arr[i-1], True, c2_arr[i-1]), (40,height/4.5*i-55))
		screen.blit(font.render(t1_arr[i-1], True, (255,255,255)), (38,height/4.5*i-55))
		screen.blit(font.render(t2_arr[i-1], True, c1_arr[i-1]), (190,height/4.5*i-55))
		screen.blit(font.render(t2_arr[i-1], True, (255,255,255)), (188,height/4.5*i-55))


	pos = pg.mouse.get_pos()
	if (pos[0] >= 45 and pos[0] <= 445) and (pos[1] >= height-150 and pos[1] <= height-50):
		pg.draw.rect(screen,(255, 204, 0),(45,height-150,400,100),border_radius=height//2)
		pg.draw.rect(screen,(0, 0, 255),(45,height-150,400,100),4,border_radius=height//2)
		screen.blit(font.render("Back to Main Menu", True, (0, 0, 255)), (115,height-125))
		screen.blit(pg.image.load('assets/home_1.png').convert_alpha(),(75,height-120))
	else:
		pg.draw.rect(screen,(255, 255, 153),(45,height-150,400,100),border_radius=height//2)
		pg.draw.rect(screen,(102, 0, 255),(45,height-150,400,100),4,border_radius=height//2)
		screen.blit(font.render("Back to Main Menu", True, (102, 0, 255)), (115,height-125))
		screen.blit(pg.image.load('assets/home_1.png').convert_alpha(),(75,height-120))


	pg.draw.rect(screen,(255,255,255),(width-660, 15, 600, 600),border_radius=10)
	pg.draw.rect(screen,(51, 153, 255),(width-660, 15, 600, 600),3,border_radius=10)

	for i in range(rows):
		for j in range(cols):
			grid_obj[i][j].show(width-715 + 600/rows*(j+1), 0 + 600/cols*(i+1) - 40)

class Candy:
	def __init__(self, t, p):
		self.type = t
		if t==0:
			self.img_type = pg.image.load('assets/red_basic.png')
			# self.power = 0
		elif t==1:
			self.img_type = pg.image.load('assets/orange_basic.png')
			# self.power = 0
		elif t==2:
			self.img_type = pg.image.load('assets/yellow_basic.png')
			# self.power = 0
		elif t==3:
			self.img_type = pg.image.load('assets/green_basic.png')
			# self.power = 0
		elif t==4:
			self.img_type = pg.image.load('assets/blue_basic.png')
			# self.power = 0
		elif t==5:
			self.img_type = pg.image.load('assets/purple_basic.png')
			# self.power = 0
		self.img_type = pg.transform.scale(self.img_type,(50,50))

	def show(self,x,y):
		screen.blit(self.img_type,(x,y))

def main():
	pg.init()

	global width
	global height
	global screen
	global font
	global g_state

	width = 1200
	height = 630
	screen = pg.display.set_mode([width, height])
	pg.display.set_caption('Candy Crush by Rajdip, Hritwick & Akash')
	pg.display.set_icon(pg.image.load("CandyIco.jpg"))
	# font = pg.font.SysFont(None, 22)

	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			if event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				if (pos[0] >= width/3 - 300 and pos[0] <= width/3 - 100) and (pos[1] >= 525 and pos[1] <= 585):
					g_state = 1
				elif (pos[0] >= width/3*2 - 300 and pos[0] <= width/3*2 - 100) and (pos[1] >= 525 and pos[1] <= 585):
					g_state = 2
				elif (pos[0] >= width - 300 and pos[0] <= width - 100) and (pos[1] >= 525 and pos[1] <= 585):
					running = False

				if (pos[0] >=45 and pos[0] <= 445) and (pos[1] >= height-150 and pos[1] <= height-50) and g_state==2:
					g_state=0

		if g_state==0:
			welcomeScreen()
		elif g_state==1:
			scoreboard()
		elif g_state==2:
			initgame()
			game()

		pg.display.flip()

	# Time to end the Game
	pg.quit()


if __name__ == "__main__":
	main()