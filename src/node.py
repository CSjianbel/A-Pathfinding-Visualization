import pygame

class Node:

	def __init__(self, row, column, dimension):

		self.row = row
		self.column = column
		self.dimension = dimension

		self.x = column * dimension
		self.y = row * dimension

		self.isWall = False
		self.isStart = False
		self.isEnd = False

		self.h = 0
		self.g = 0
		self.f = 0
		self.previous = None

		self.neighbors = []

		self.rect = pygame.Rect(self.x, self.y, self.dimension, self.dimension)

	
	def draw(self, screen, color):
		"""
		Draws the squares to screen given a color
		PARAMS: Self, pygame.Surface, Tupple->(int, int, int)
		RETURN: None
		"""

		pygame.draw.rect(screen, color, self.rect)
		pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

	
	def update(self):
		"""
		Updates states if left-clicked isWall if right-clicked not isWall
		PARAMS: Self
		RETURN: None
		"""


		if self.isStart or self.isEnd:
			return

		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]

		if self.rect.collidepoint(mouseX, mouseY):
			if pygame.mouse.get_pressed()[0]:
				self.isWall = True
			
			elif pygame.mouse.get_pressed()[2]:
				self.isWall = False


	def getNeighbors(self, grid):
		"""
		Appends to self.neighbors if it is not a wall and is in window
		PARAMS: Self, List->List->Node
		RETURN: None
		"""

		# up
		if self.row > 0 and not grid[self.row - 1][self.column].isWall:
			self.neighbors.append(grid[self.row - 1][self.column])
		# down
		if self.row < len(grid) - 1 and not grid[self.row + 1][self.column].isWall:
			self.neighbors.append(grid[self.row + 1][self.column])
		# left
		if self.column > 0 and not grid[self.row][self.column - 1].isWall:
			self.neighbors.append(grid[self.row][self.column - 1])
		# right
		if self.column < len(grid[0]) - 1 and not grid[self.row][self.column + 1].isWall:
			self.neighbors.append(grid[self.row][self.column + 1])
			




