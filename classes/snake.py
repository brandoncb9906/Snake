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

	def move(self):
		x, y = self.__pos[len(self.__pos) - 1]
		if self.__dir == RIGHT:
			self.__pos.append((x, y + 1))
		if self.__dir == LEFT:
			self.__pos.append((x, y - 1))
		if self.__dir == UP:
			self.__pos.append((x - 1, y))
		if self.__dir == DOWN:
			self.__pos.append((x + 1, y))

		self.__pos.pop(0)


# Direcciones
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

tupla = (1, 2, "alonso")
