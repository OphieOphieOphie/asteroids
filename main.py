import pygame
import constants
import player

def main():

	pygame.init()

	start_flag = True

	scr_wdt, scr_hgt = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT 	# takes screen width and screen height
	screen = pygame.display.set_mode((scr_wdt, scr_hgt)) 				# sets

	timer = pygame.time.Clock() 										# sets a timer that allows us to control framerape
	dt = 0																# delta time

	pos_x, pos_y = scr_wdt/2, scr_hgt/2

	player_icon = player.Player(pos_x, pos_y)					# creates a Player instance and places it in the middle of the screen, gives it the preset radius

	while start_flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start_flag = False

		pygame.Surface.fill(screen, (0,0,0))							# screen is black

		player_icon.draw(screen)
		player_icon.update(dt)

		pygame.display.flip()											# updates the screen
		
		dt = timer.tick(60) 											# updates delta time, stored in milliseconds 

if __name__ == "__main__":
	main()
