import pygame

class Ship():
	
	def __init__(self,ai_settings,screen):
		#initialize the ship and set its starting position
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the ship image and get its rect.
		#this returns a surface representing the ship, it then loads the image
		self.image = pygame.image.load('images/ship.bmp')
		#this then accesses the images rect atrributes
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		#movement flags, these are set to false to prevent them from moving on their own until a key is pressed
		self.moving_right = False
		self.moving_left = False
		
	def blitme(self):
		#draw the ship at its current location, above the screen itself, above the color, this is the blit()
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		#Update the ship's position based on the movement flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			#if the coordinates of the ship are less than the screens farthest coordinates, then at the speed of the bullet set, the ship will move
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		self.rect.centerx = self.center
			
			
