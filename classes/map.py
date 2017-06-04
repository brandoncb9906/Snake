from classes.block import *
import random

class Map:
	def __init__(self, width, height, snake, walls):
		self.__width = width
		self.__height = height
		self.__snake = snake
		self.__walls = walls
		self.__map = self.initialize(width, height)
		self.create_walls()
		self.put_apple()

	def initialize(self, width, height):
		the_map = []
		for x in range(width):
			line = []
			for y in range(height):
				block = Block(EMPTY)
				line.append(block)
			the_map.append(line)
		return the_map

	def get_map(self):
		pos = self.__snake.get_pos()

		map = []

		for x in range(self.__width):
			line = []
			for y in range(self.__height):
				block = self.__map[x][y]

				if (x, y) in pos:
					# Aquí esta coordenada pertenece al snake
					line.append(SNAKE)
				else:
					line.append(block.get_type())

			map.append(line)
		return map

	def get_block(self, x, y):
		return self.__map[x][y]

	def is_offmap(self, x, y):
		if x < 0 or y < 0 or x >= self.__width or y >= self.__height:
			return True
		else:
			return False

	def find_empty(self):
		while True:
			x = random.randrange(0, self.__width)
			y = random.randrange(0, self.__height)

			# Revisar que el bloque sea vacio
			block = self.__map[x][y]
			if block.get_type() != EMPTY:
				continue
			# Revisar que el bloque no sea del snake
			pos = self.__snake.get_pos()
			if (x, y) in pos:
				continue

			return block

	def create_walls(self):
		for x in range(0, self.__walls):
			block = self.find_empty()
			block.set_type(WALL)

	def put_apple(self):
		block = self.find_empty()
		block.set_type(FOOD)

	def put_bonus(self):
		block = self.find_empty()
		block.set_type(BONUS)
