class Snake:
	def __init__(self, size):
		self.__size = size
		self.__dir = RIGHT
		self.__pos = self.get_init_pos(size)

	def get_init_pos(self, size):
		pos = []
		for y in range(size):
			pos.append((0, y))
		return pos

	def get_pos(self):
		return self.__pos

# Direcciones
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

tupla = (1, 2, "alonso")
