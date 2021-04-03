import pygame 
from config import SCREEN_SIZE, WIDTH, HEIGHT, MAP
from boundary import Boundary
from ray import Ray
from particle import Particle
import random

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)

	walls = []

	for i in range(5):
		x1 = random.randint(0, WIDTH)
		x2 = random.randint(0, WIDTH)
		y1 = random.randint(0, HEIGHT)
		y2 = random.randint(0, HEIGHT)
		walls.append(Boundary(x1, y1, x2, y2))
	
	walls.append(Boundary(0, 0, WIDTH, 0))
	walls.append(Boundary(WIDTH, 0, WIDTH, HEIGHT))
	walls.append(Boundary(WIDTH, HEIGHT, 0, HEIGHT))
	walls.append(Boundary(0, HEIGHT, 0, 0))


	particle = Particle()

	key = None

	while True:

		screen.fill((0,0,0))

		particle.draw(screen)
		for wall in walls:
			wall.draw(screen)

		scene = particle.look(walls, screen)
		w =  int(WIDTH / len(scene))

		for i in range(len(scene)):
			sq = scene[i] * scene[i]
			wSq = WIDTH * WIDTH
			x = int(i*w) + WIDTH
			b = remap(sq, 0, wSq, 255, 0)
			h = remap(scene[i], 0, WIDTH, HEIGHT, 0)
			y = (HEIGHT - h)/2
			try:
				pygame.draw.rect(screen, (b, b, b), (x, y, w, h))
			except:
				# print('error', x, y, w, h)
				pass


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				key = event.key

			if event.type == pygame.KEYUP:
				key = None

		# if key == pygame.K_UP:
		# 	particle.move(10)
		# elif key == pygame.K_DOWN:
		# 	particle.move(-10)			
		if key == pygame.K_RIGHT:
			particle.rotate(0.2)
		elif key == pygame.K_LEFT:
			particle.rotate(-0.2)
					

		x, y = pygame.mouse.get_pos()
		if x >= WIDTH-1:
			x = WIDTH-1
		elif x <= 0:
			x = 0
		if y >= HEIGHT-1:
			y = HEIGHT-1
		elif y <= 0:
			y = 0
		particle.update(x, y)

		pygame.display.update()

main()