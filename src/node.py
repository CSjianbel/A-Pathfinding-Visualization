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

		mouseX, mouseY = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouseX, mouseY):
			if pygame.mouse.get_pressed()[0]:
				self.isWall = True
			
			elif pygame.mouse.get_pressed()[2]:
				self.isWall = False


	def getNeighbors(self, grid, across):
		"""
		Appends to self.neighbors if it is not a wall and is in window
		PARAMS: Self, List->List->Node, Boolean
		RETURN: None
		"""

		if not across:
			
			for i in range(-1, 2):
				for j in range(-1, 2):

					Y = self.row + i
					X = self.column + j

					if Y > -1 and Y < len(grid) and X > -1 and X < len(grid[0]) and not grid[Y][X].isWall:
						self.neighbors.append(grid[Y][X])
		
		else:

			i = self.row
			j = self.column

			if i > 0 and not grid[i - 1][j].isWall:
					self.neighbors.append(grid[i - 1][j])

			if i < len(grid) - 1 and not grid[i + 1][j].isWall:
					self.neighbors.append(grid[i + 1][j])

			if j > 0 and not grid[i][j - 1].isWall:
					self.neighbors.append(grid[i][j - 1])

			if j < len(grid[i]) - 1 and not grid[i][j + 1].isWall:
					self.neighbors.append(grid[i][j + 1])

