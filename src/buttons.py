import pygame

class button:

	def __init__(self, name, x, y, width, color, height = 20):

		self.name = name
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color

		self.rect = pygame.Rect(x, y, width, height)
	
	def draw(self, surface):

		pygame.draw.rect(surface, self.color, self.rect)

	def isPressed(self):

		mouseX, mouseY = pygame.mouse.get_pos()

		if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouseX, mouseY):

			return True

		return False

	def isHover(self):

		mouseX, mouseY = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouseX, mouseY):

			self.color = (self.color[0], self.color[1], self.color[2], 0.4)
		
		else:

			self.color = (self.color[0], self.color[1], self.color[2])