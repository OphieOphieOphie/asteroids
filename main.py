import pygame
import constants
import player
import asteroids
import asteroidfield
import shot

def main():
	print("Starting asteroids!")
	pygame.init()

	start_flag = True

	scr_wdt, scr_hgt = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT 	# takes screen width and screen height
	screen = pygame.display.set_mode((scr_wdt, scr_hgt)) 				# sets

	timer = pygame.time.Clock() 										# sets a timer that allows us to control framerape
	dt = 0																# delta time

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	player.Player.containers = (updatable, drawable)
	asteroids.Asteroid.containers = (asteroid, updatable, drawable)
	asteroidfield.AsteroidField.containers = (updatable)
	shot.Shot.containers = (shots, updatable, drawable)

	pos_x, pos_y = scr_wdt/2, scr_hgt/2

	player_icon = player.Player(pos_x, pos_y)							# creates a Player instance and places it in the middle of the screen, gives it the preset radius

	ast_field = asteroidfield.AsteroidField()

	while start_flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start_flag = False

		pygame.Surface.fill(screen, (0,0,0))							# screen is black

		for drawable_icon in drawable:
			drawable_icon.draw(screen)

		for updatable_icon in updatable:
			updatable_icon.update(dt)

		for potential_collision in asteroid:
			if not -(2 * constants.ASTEROID_MAX_RADIUS) < potential_collision.position.y <= constants.SCREEN_HEIGHT + (2 * constants.ASTEROID_MAX_RADIUS) or not -(2 * constants.ASTEROID_MAX_RADIUS) < potential_collision.position.x <= constants.SCREEN_WIDTH + (2 * constants.ASTEROID_MAX_RADIUS):
				potential_collision.kill()
			elif potential_collision.collision(player_icon):
				start_flag = False
				break
			for potential_destruction in shots:
				if not -5 <= potential_destruction.position.y <= constants.SCREEN_HEIGHT + 5 or not -5 < potential_destruction.position.x <= constants.SCREEN_WIDTH + 5:
					potential_destruction.kill()
				elif potential_destruction.collision(potential_collision):
					potential_collision.split(), potential_collision.kill(), potential_destruction.kill()

		pygame.display.flip()											# updates the screen
		
		dt = timer.tick(60) / 1000 										# updates delta time, stored in milliseconds 
	print("Game over!")

if __name__ == "__main__":
	main()
