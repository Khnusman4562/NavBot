import pygame, sys 
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from secrets import choice
import pyttsx3 
import speech_recognition as sr
from PIL import Image
from secrets import choice
import pyttsx3 
import speech_recognition as sr
from PIL import Image
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


Assistance=pyttsx3.init('sapi5')
voices=Assistance.getProperty('voices')
rate=Assistance.getProperty('rate')
Assistance.setProperty('rate',130)
Assistance.setProperty('voices',voices[0].id)

    #    list of Stores
Store=["zara","cricket","football","basketball","basket","bowling","bikeridding","mufti","pepejeans","reliance","uspolo","us","polo","allen","solly","allen solly","flying","machine","puma","vanheusen","levi's","reebok","diesel","gas","mcdonald","subway","dominos","kfc","natural","pizza hut","khiva","dunkin donuts","don","malgudi"]
Electronics=["croma","reliance digital","cex","helios","titan","rolex","fastrack","hublot"]
Eat=["burger","pizza","shawarma","icecream","dosa","juice","fries","cake","donuts","eat"]
games=["cricket","football","basketball","bowling","bikeridding"]


#   list of Products

playtimes=["cricket","football","basketball","bowling","bikeridding"]
Food=["mcdonald","subway","dominos","kfc","natural","pizza","hut","khiva","dunkin donuts","malgudi"]
Fashion=["shirt","jeans","tshirt","innerwear","slippers","casualshoes","formalshoes","sandals","clothes","cloth"]
Accessories=["headphones","smartwatches","pendrives","memorycards","camera","wacthes"]

    #  extra list

Store1=["zara","mufti","pepejeans","uspolo","allen solly","flying machine","puma","vanheusen","levi's","reebok","diesel","gas"]
Food1=["mcdonald","subway","dominos","kfc","natural","pizza hut","khiva","dunkin donuts","malgudi"]
# Electronic=["croma","reliance","cex","helios","titan","rolex","fastrack","hublot"]

game=["timezone","game","games"]


def token(shopname): 
  word_data = shopname
  nltk_tokens = nltk.word_tokenize(word_data)
#   print (nltk_tokens)
  return nltk_tokens



def speak(audio):
    print("   ")
    Assistance.say(audio)
    print(f"{audio}")
    Assistance.runAndWait()

speak("welcome to pheonix mall")

speak("how may i assist you ")

def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        command.energy_threshold=10000
        command.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = command.listen(source)
        

        try:
            print("Recognizing..")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said:{query}")
        
        except Exception as Error:
            return "none"

        return query
inputs=takecommand()


word_data = inputs
nltk_tokens = nltk.word_tokenize(word_data)
en_stops = set(stopwords.words('english'))
all_words = nltk_tokens
for word in all_words: 
    if word not in en_stops:
       
       x = word.lower()
       if x in Fashion:
           speak('which store do you want to visit  ')
           speak(Store1)

           shopname=takecommand().lower()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words:
             if word  in Store:
              find=word.lower()


       if x in Accessories:
           speak('which store do you want to visit  ')
           speak(Electronics)

           shopname=takecommand().lower()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in Store:
              find=word.lower()
       if x in game:
           speak('which game you wish to Play ')
           speak(games)
           shopname=takecommand().lower()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in games:
              find=word.lower()
        #    print("i want to play games")
       if x in Eat:
           speak('from were you want to eat  ')

           speak(Food1)
           shopname=takecommand().lower()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in Store:
              find=word.lower()
       if x in Store:
            print(x)
            find=x
       if x in Eat:
            print(x)
            find=x
    #    if x in Eat:
    #         print(x)
    #         find=x

       if x in Food:
            find=x
	      
       if x in Electronics:
            find=x


    #    else:
	# 	    # break
	#    	    speak("this is not available now")
    #         print(x)

# if find=="xxx":
# 	speak("this is not available")
# # input=takecommand()


class Pathfinder:
	def __init__(self,matrix):

		# setup
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)
		self.select_surf = pygame.image.load('selection.png').convert_alpha()

		# pathfinding
		self.path = []

		# Roomba
		self.roomba = pygame.sprite.GroupSingle(Roomba(self.empty_path))

	def empty_path(self):
		self.path = []

	def draw_active_cell(self,hm):
		mouse_pos = pygame.mouse.get_pos()		
		row =  mouse_pos[1] // 32
		col =  mouse_pos[0] // 32
		current_cell_value = self.matrix[row][col]
		if current_cell_value == 1:
			rect = pygame.Rect((col * 32,row * 32),(32,32))
			screen.blit(self.select_surf,rect)

	def create_path(self,hm):

		# start
		start_x, start_y = self.roomba.sprite.get_coord()
		start = self.grid.node(start_x,start_y)

		# end
		end_x,end_y =hm[find]
		end = self.grid.node(end_x,end_y) 

		# path
		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
		self.path,_ = finder.find_path(start,end,self.grid)
		# print(self.path)
		self.grid.cleanup()
		self.roomba.sprite.set_path(self.path)

	def draw_path(self):
		if self.path:
			points = []
			for point in self.path:
				x = (point[0] * 32) + 16
				y = (point[1] * 32) + 16
				points.append((x,y))

			pygame.draw.lines(screen,'#4a4a4a',False,points,5)

	def update(self,hm):
		self.draw_active_cell(hm)
		self.draw_path()

		# roomba updating and drawing
		self.roomba.update()
		self.roomba.draw(screen)

class Roomba(pygame.sprite.Sprite):
	def __init__(self,empty_path):

		# basic
		super().__init__()
		self.image = pygame.image.load('roomba.png').convert_alpha()
		self.rect = self.image.get_rect(center = (85,240))

		# movement 
		self.pos = self.rect.center
		self.speed = 3
		self.direction = pygame.math.Vector2(0,0)

		# path
		self.path = []
		self.collision_rects = []
		self.empty_path = empty_path

	def get_coord(self):
		col = self.rect.centerx // 32
		row = self.rect.centery // 32
		return (col,row)

	def set_path(self,path):
		self.path = path
		self.create_collision_rects()
		self.get_direction()

	def create_collision_rects(self):
		if self.path:
			self.collision_rects = []
			for point in self.path:
				x = (point[0] * 32) + 16
				y = (point[1] * 32) + 16
				rect = pygame.Rect((x - 2,y - 2),(4,4))
				self.collision_rects.append(rect)

	def get_direction(self):
		if self.collision_rects:
			start = pygame.math.Vector2(self.pos)
			end = pygame.math.Vector2(self.collision_rects[0].center)
			self.direction = (end - start).normalize()
		else:
			self.direction = pygame.math.Vector2(0,0)
			self.path = []

	def check_collisions(self):
		if self.collision_rects:
			for rect in self.collision_rects:
				if rect.collidepoint(self.pos):
					del self.collision_rects[0]
					self.get_direction()
		else:
			self.empty_path()

	def update(self):
		self.pos += self.direction * self.speed
		self.check_collisions()
		self.rect.center = self.pos

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()

# game setup
bg_surf = pygame.image.load('mall_map2.png').convert()
matrix = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0],
	[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0],
	[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0],
	[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

hm={'zara':(19,7),"mufti":(36,16),'uspolo':(9,3),'polo':(9,3),'solly':(25,2),'allen':(36,9),'machine':(7,10),'diesel':(1,14),'puma':(13,19),'diesel':(20,15),'gas':(27,20),"reebok":(36,16),
    'croma':(19,7),'reliance':(36,16),'digital':(36,16),'helios':(9,3),'titan':(25,2),'fastrack':(36,9),'hublot':(13,19),
    'mcdonald':(19,7),'subway':(36,16),'kfc':(9,3),'natural':(25,2),'pizzahut':(36,9),'hut':(36,9),'khiva':(7,10),'malgudi':(13,19),"dominos":(36,16),
    'cricket':(19,7),'football':(36,16),'bowling':(25,2),'bikeridding':(36,9),'ridding':(36,9),'basket':(36,9),'basketball':(36,9)}

pathfinder = Pathfinder(matrix)
# if(query in a):
while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# if event.type == pygame.MOUSEBUTTONDOWN:
			pathfinder.create_path(hm)

		screen.blit(bg_surf,(0,0))
		pathfinder.update(hm)

		pygame.display.update()
		clock.tick(60)
