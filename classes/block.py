class Block:
	def __init__(self, type):
		self.__type = type
	
	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type

EMPTY = "empty"
FOOD = "food"
LIFE = "life"
BONUS = "bonus"
WALL = "wall"

# Bloque especial usado en UI para indicar que el snake está aquí
SNAKE = "snake"
