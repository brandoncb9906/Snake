from classes.map import Map
from classes.snake import Snake

class Game:
	def __init__(self, level):
		self.__ldata = level_data[level]
		self.__snake = Snake(self.__ldata["s_size"])
		size = self.__ldata["m_size"]
		self.__map = Map(size, size, self.__snake, self.__ldata["walls"])

	def print_map(self):
		print(self.__map.get_map())

	def test(self):
		self.print_map()
		self.__snake.move()
		self.print_map()
		self.__map.find_empty()

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
