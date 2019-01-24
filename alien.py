import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	# A class to represent a single alien in the fleet
	
	def __init__(self,ai_settings,screen):
		#initialize the alien and set its starting position
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the alien image and set its rect attributes
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the alien's exact position
		self.x = float(self.rect.x)
		
	def blitme(self):
		#draws the alien at its current location
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		#move alien to the right
		self.x += self.ai_settings.alien_speed_factor
		self.rect.x = self.rect
		
		
