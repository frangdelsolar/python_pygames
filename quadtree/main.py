import pygame
import sys
from quad.constants import SCREEN_SIZE, WIDTH, HEIGHT
from quad.quadtree import QuadTree, Rectangle, Point, Circle

import random


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

run = True

boundary = Rectangle(0, 0, WIDTH, HEIGHT)
qt = QuadTree(boundary, 4)

for i in range(500):
	qt.insert(Point(random.randint(0, WIDTH), random.randint(0, HEIGHT)))   

while run:
	screen.fill((0, 0, 0))   
	qt.draw(screen)

	posx, posy = pygame.mouse.get_pos()
	pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
	if pressed1:
		qt.insert(Point(posx, posy))
	
	# rango = Rectangle(posx, posy, 200, 100)
	# pygame.draw.rect(screen, (255, 0, 255), (rango.x, rango.y, rango.w, rango.h), 1)

	rango = Circle(posx, posy, 100)
	pygame.draw.circle(screen, (255, 0, 255), (rango.x, rango.y), rango.r, 1)

	points = qt.query(rango, [])
	for point in points: 
		pygame.draw.circle(screen, (255, 0, 255), (point.x, point.y), 3)

	print(len(points))


	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				qt.insert(Point(posx, posy))

			if event.key == pygame.K_UP:
				print(len(points))



