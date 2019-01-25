import sys
from time import sleep

import pygame

from bullet import Bullet

from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	#this shuts down the game
	elif event.key == pygame.K_q:
		sys.exit()
		
def fire_bullet(ai_settings,screen,ship,bullets):
	#fire a bullet if limit not yet reached
	#create a new bullet and add it to the bullets group
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
		
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False	
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
	#respond to keypresses and mouse events
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings,screen, ship, bullets)
			
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
				

				
def update_screen(ai_settings, screen, ship,aliens, bullets):
	
	#update images on the screen and flip to the new screen
	
	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)	
	
	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#draw automatically draws each element in the group in its defined rect position
	aliens.draw(screen)
				
	#Make the most recently drawn screen visible	
	pygame.display.flip()
	
def update_bullets(ai_settings, screen, ship, aliens, bullets):
	#Update position of bullets and get rid of old bullets
	#Get rid of bullets that have disappeared
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#check for bullets that have hit the alien, if it has, delete the bullet and the alien
	
	check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		#destroy existing bullets and create a new fleet
		#the empty method removes and remaining sprites from a group
		bullets.empty()
		#this creates a new fleet by calling create_fleet
		create_fleet(ai_settings, screen,ship, aliens)
		

def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	#this calculates the num of aliens
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	#this will determine the number of rows for the screen
	available_space_y = (ai_settings.screen_height - (3 * alien_height)-ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens,alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	#this calculation helps determine the each aliens spot on the screen
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	#this is to move the row farther down the screen
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
			
def create_fleet(ai_settings, screen, ship, aliens):
	#create a fleet of aliens
	#this alien is to help figure out how many aliens to put on screen and doesn't itself get put on screen
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	
	#create first row of aliens
	#this is a loop that counts from 0 to the num of aliens we need
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen, aliens, alien_number,row_number) 

def check_fleet_edges(ai_settings, aliens):
	#respond appropriately if aliens have reached the edge of the screen
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
			
def change_fleet_direction(ai_settings,aliens):
	#drop the fleet and change direction
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats, screen, ship, aliens, bullets):
	if stats.ships_left > 0:
		#respond to ships being hit
		stats.ships_left -= 1
		#empty bullets and aliens
		aliens.empty()
		bullets.empty()
	
		#create a new fleet and center the ship
		creat_fleet(ai_settings, screen,ship, aliens)
		ship.center_ship()
	
		#pause
		sleep(0.5)
	else:
		stats.game_active = False
	
def check_aliens_bottom(ai_settings,stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats, screen, ship, aliens, bullets)
			break
			
	
def update_aliens(ai_settings,stats,screen,ship, aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()#this calls the update from the alien method and runs each of the update parts
	
	#look for alien ship collisions
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats, screen, ship, aliens, bullets)
	check_aliens_bottom(ai_settings,stats, screen, ship, aliens, bullets)
		
	
	
		
