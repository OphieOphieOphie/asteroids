import pygame
import constants

def main():
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	pygame.init()
	start_flag = True
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	while start_flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start_flag = False
		pygame.Surface.fill(screen, (0,0,0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
