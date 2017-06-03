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

	def initialize(self, width, height):
		the_map = []
		for x in range(width):
			line = []
			for y in range(height):
				block = Block(EMPTY)
				line.append(block)
			the_map.append(line)
		return the_map

	def print_map(self):
		pos = self.__snake.get_pos()

		for x in range(self.__width):
			str_line = ""
			for y in range(self.__height):
				block = self.__map[x][y]

				if (x, y) in pos:
					str_line += "x "
				else:
					btype = block.get_type()
					if btype == EMPTY:
						str_line += ". "
					elif btype == FOOD:
						str_line += "y "
					elif btype == LIFE:
						str_line += "u "
					elif btype == WALL:
						str_line += "[]"
			print(str_line)

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



