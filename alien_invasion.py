


import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	
	#Initialize game and create a screen object
	
	pygame.init() # this initializes background settings for pygame to work properly
	ai_settings = Settings()# This puts the Settings class into ai_settings variable. You can call this then and access settings
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))#display is a module and set_mode is a function that initializes pygames Surface class.
	#It then gives it the variable name 'screen'
	#It also calls the ai_settings from settings import of Settings, called above, and calls the height and width
	pygame.display.set_caption("Alien Invasion")# this sets the windows caption title, it's visible when you run the game
	
	#make a ship
	ship = Ship(ai_settings,screen) #ship class has been imported above, this calls the ships settings and to the screen
	#make a group to store bullets in
	bullets = Group() # here we make an instance of Group and call it bullets
	
	
	#Set the background color
	bg_color = (230,230,230)
	
	#Start the main loop for the game
	#I believe this runs through the functions in other files and runs them thru for the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()#updates the ship as necessary
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets)
		
		
		
		
				
			
run_game()# this runs the whole thing
