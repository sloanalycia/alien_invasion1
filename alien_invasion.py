


import pygame
from pygame.sprite import Group

from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	
	#Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#make a ship*
	ship = Ship(ai_settings,screen)
	#make a group to store bullets in
	bullets = Group() 
	aliens = Group()
	
	#create a fleet of aliens
	gf.create_fleet(ai_settings, screen,ship, aliens)
	
	#Set the background color
	bg_color = (230,230,230)
	
	#make an alien
	alien = Alien(ai_settings,screen)
	
	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings,ship, aliens)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		
		
		
		
				
			
run_game()
