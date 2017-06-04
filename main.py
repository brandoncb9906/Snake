from classes.game import Game
from classes.block import *
from classes.snake import *
import pygame
import random

game = Game(2)
#-------------------------------------------------------------------
white = (255,255,255)
black = (0,0,0)
green = (13,151,34)
blue = (0,0,255)
red = (255,0,0)
grey = (105,107,112)
#-------------------------------------------------------------------
GAME_SIZE = 500
screen_size = [GAME_SIZE + 300, GAME_SIZE]
BLOCK_SIZE = GAME_SIZE / game.get_size()

watch = pygame.time.Clock()

apple_img = pygame.image.load("pixel_apple.png")
apple_img = pygame.transform.scale(apple_img, (int(BLOCK_SIZE), int(BLOCK_SIZE)))
bonus_img = pygame.image.load("pixel_bonus.png")
bonus_img = pygame.transform.scale(bonus_img, (int(BLOCK_SIZE), int(BLOCK_SIZE)))

pygame.init()


pygame.display.set_caption("THE BEST SNAKE EVER")
screen = pygame.display.set_mode(screen_size)


def draw_map():

	screen.fill(black)
	gmap = game.get_map()
	size = game.get_size()
	for y in range(size):
		for x in range(size):
			block = gmap[y][x]
			color = black
			if block == SNAKE:
				color = green
			elif block == WALL:
				pygame.draw.rect(screen, grey, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
			elif block == FOOD:
				pos = (x * BLOCK_SIZE, y * BLOCK_SIZE)
				screen.blit(apple_img, pos)
			elif block == BONUS:
				pos = (x * BLOCK_SIZE, y * BLOCK_SIZE)
				screen.blit(bonus_img, pos)
			pygame.draw.rect(screen,color,(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE,BLOCK_SIZE ),1)

def gameloop():
	introJuego = True
	steps = 0
	while introJuego:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			introJuego = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				game.snake_dir(DOWN)
			if event.key == pygame.K_UP:
				game.snake_dir(UP)
			if event.key == pygame.K_LEFT:
				game.snake_dir(LEFT)
			if event.key == pygame.K_RIGHT:
				game.snake_dir(RIGHT)
		if steps >= 15:
			game.tick()
			draw_map()
			steps = 0
		steps += 1
		pygame.display.flip()
		watch.tick(30)

gameloop()
pygame.quit()
