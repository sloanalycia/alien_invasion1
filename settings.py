class Settings():
	#A class to store all settings for Alien Invasion
	
	
	def __init__(self):
		#initialize game settings
		#Screen Settings
		
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (190, 190, 190)
		
		#ship settings
		self.ship_speed_factor = 1.5
		
		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 80,60,60
		self.bullets_allowed = 3
		
		
		
		
