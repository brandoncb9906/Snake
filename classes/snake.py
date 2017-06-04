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

	def move(self, grow = False):
		self.__pos.append(self.next_pos())
		if not grow:
			self.__pos.pop(0)

	def get_dir(self):
		return self.__dir

	def change_dir(self, dir):
		self.__dir = dir

	def next_pos(self):
		x, y = self.__pos[len(self.__pos) - 1]
		if self.__dir == RIGHT:
			return (x, y + 1)
		if self.__dir == LEFT:
			return (x, y - 1)
		if self.__dir == UP:
			return (x - 1, y)
		if self.__dir == DOWN:
			return (x + 1, y)


# Direcciones
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
