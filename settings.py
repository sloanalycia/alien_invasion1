class Settings():
	#A class to store all settings for Alien Invasion
	
	
	def __init__(self):
		#initialize game settings
		#Screen Settings
		
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (190, 190, 190)
		
		#ship settings
		self.ships_limit = 3
		
		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 80,60,60
		self.bullets_allowed = 3
		
		#alien speed settings
		self.fleet_drop_speed = 10
		#fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
		#how quickly the game speeds up
		self.speedup_scale = 1.2
		
		#how quickly the alien point values increase
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.alien_points = 50
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
	
	def increase_speed(self):
		#increase speed settings
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		
		
		
		
		
		
		
