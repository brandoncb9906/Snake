from classes.map import Map
from classes.snake import *
from classes.block import *


class Game:
	def __init__(self, level):
		self.__ldata = level_data[level]
		self.init_game()

	def init_game(self):
		self.__snake = Snake(self.__ldata["s_size"])
		size = self.__ldata["m_size"]
		self.__map = Map(size, size, self.__snake, self.__ldata["walls"])
		self.__bonus_count = 100

	def snake_move(self, grow = False):
		self.__snake.move(grow)

	def snake_dir(self, dir):
		current_dir = self.__snake.get_dir()
		if (current_dir == RIGHT and dir == LEFT) or \
			(current_dir == LEFT and dir == RIGHT) or \
			(current_dir == UP and dir == DOWN) or \
			(current_dir == DOWN and dir == UP):
			return
		self.__snake.change_dir(dir)


	def get_map(self):
		return self.__map.get_map()

	def get_size(self):
		return self.__ldata["m_size"]

	def tick(self):
		#lleva el contador del bonus
		self.__bonus_count -= 1
		if self.__bonus_count == 0:
			self.__map.put_bonus()

		next_pos = self.__snake.next_pos()
		if self.is_offmap(next_pos):
			# lose life
			self.lose()
		elif self.is_wall(next_pos):
			# lose life
			self.lose()
		elif next_pos in self.__snake.get_pos():
			# lose life
			self.lose()
		elif self.is_apple(next_pos):
			x, y = next_pos
			block = self.__map.get_block(x, y)
			block.set_type(EMPTY)
			self.__map.put_apple()
			self.snake_move(grow = True)
		elif self.is_bonus(next_pos):
			x, y = next_pos
			block = self.__map.get_block(x, y)
			block.set_type(EMPTY)
			self.__bonus_count = 100
			self.snake_move(grow = True)

		else:
			self.snake_move()

	def is_wall(self, pos):
		x, y = pos
		block = self.__map.get_block(x, y)
		return block.get_type() == WALL


	def is_offmap(self, pos):
		x, y = pos
		return self.__map.is_offmap(x, y)

	def is_apple(self,pos):
		x, y = pos
		block = self.__map.get_block(x, y)
		return block.get_type() == FOOD

	def is_bonus(self, pos):
		x, y = pos
		block = self.__map.get_block(x, y)
		return block.get_type() == BONUS

	def lose(self):
		self.init_game()




level_data = [{
	"m_size": 5,
	"s_size": 1,
	"walls": 1
}, {
	"m_size": 6,
	"s_size": 3,
	"walls": 3
}, {
	"m_size": 7,
	"s_size": 3,
	"walls": 5
}, {
	"m_size": 8,
	"s_size": 5,
	"walls": 7
}, {
	"m_size": 9,
	"s_size": 5,
	"walls": 9
}, {
	"m_size": 10,
	"s_size": 7,
	"walls": 11
}]
