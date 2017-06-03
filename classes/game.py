from classes.map import Map
from classes.snake import Snake

class Game:
	def __init__(self, level):
		self.__ldata = level_data[level]
		self.__snake = Snake(self.__ldata["s_size"])
		size = self.__ldata["m_size"]
		self.__map = Map(size, size, self.__snake)

	def print_map(self):
		self.__map.print_map()

	def test(self):
		self.print_map()
		self.__snake.move()
		self.print_map()

level_data = [{
	"m_size": 5,
	"s_size": 1
}, {
	"m_size": 6,
	"s_size": 3
}, {
	"m_size": 7,
	"s_size": 3
}, {
	"m_size": 8,
	"s_size": 5
}, {
	"m_size": 9,
	"s_size": 5
}, {
	"m_size": 10,
	"s_size": 7
}]
