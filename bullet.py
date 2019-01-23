import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	
	#initializes the bullet. the class calls upon Sprite which appears to help group common elements
	#Sprite is intended to be a base class for obejcts, while the group class stores them
	def __init__(self,ai_settings, screen,ship):
		#create a bullet object at the ships current position
		#I believe this calls the bullet class, using super and appears to initialize it.
		super(Bullet, self).__init__()
		self.screen = screen
	
		#create a bullet rect at (0,0) and then set correct position, it uses the called settings to create the rectangle
		self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
		#this places the rectangle in the center bottom of the screen along the x-axis, at the same spot as the ships
		self.rect.centerx = ship.rect.centerx
		#looks like this is to make sure it appears from the top of the ship rectangle
		self.rect.top = ship.rect.top
	
		#store the bullet's position as a decimal, this makes it so the bullet's position is a decimal number
		self.y=float(self.rect.y)
		#sets the bullet color
		self.color = ai_settings.bullet_color
		#sets the speed factor
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		#move the bullet up the screen
		#update the decimal position of the bullet, this moves the bullet up the screen coresponding to a decreasing y coordinate
		self.y -= self.speed_factor
	
		#update rectangle position, by referencing the above self.y
		self.rect.y = self.y
	
	def draw_bullet(self):
		#draw bullets on the screen
		pygame.draw.rect(self.screen,self.color,self.rect)
