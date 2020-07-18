import pygame
from node import Node


WIDTH, HEIGHT = (600, 600)
SPACE = 10
DIMENSION = WIDTH // SPACE
GRID = []

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Creates GRID of Nodes
for i in range(DIMENSION):
	GRID.append([])
	for j in range(DIMENSION):
		GRID[i].append(Node(i, j, SPACE))

# Default Start and End Nodes
GRID[0][0].isStart = True
GRID[-1][-1].isEnd = True


PATHFINDING = False

START = GRID[0][0]
END = GRID[-1][-1]

PATH = []

openSet = list()
closedSet = list()


def draw():
	"""
	Draws to the window
	PARAMS: None
	RETURN: None
	"""

	for row in GRID:
		for node in row:
			if node.isWall:
				node.draw(SCREEN, (0,0,0))
			else:
				node.draw(SCREEN, (255,255,255))

	for node in openSet:
		node.draw(SCREEN, (0,255,0))

	for node in closedSet:
		node.draw(SCREEN, (255,0,0))

	for node in PATH:
		node.draw(SCREEN, (240, 255, 0, 1))

	START.draw(SCREEN, (64,224,208))
	END.draw(SCREEN, (148,0,211))

	
def update():
	"""
	Updates the state of the board
	PARAMS: None
	RETURN: None
	"""

	global START, END

	for i in range(DIMENSION):
		for j in range(DIMENSION):

			if GRID[i][j].rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
				keys = pygame.key.get_pressed()

				if keys[pygame.K_s] and not GRID[i][j].isEnd:
					START.isStart = False
					GRID[i][j].isWall = False
					GRID[i][j].isStart = True
					START = GRID[i][j]

				elif keys[pygame.K_e] and not GRID[i][j].isStart:
					END.isEnd = False
					GRID[i][j].isWall = False
					GRID[i][j].isEnd = True
					END = GRID[i][j]

			GRID[i][j].update()


def heuristic(node, goal):
	"""
	Returns the Manhattan Distance from node to goal
	PARAMS: Node, Node
	RETURN: Int
	"""
	x1, y1 = node.column, node.row
	x2, y2 = goal.column, goal.row

	return abs(x1 - x2) + abs(y1 - y2)


def resetGrid():
	"""
	Resets grid back to its default state
	PARAMS: None
	RETURN: None
	"""

	global START, END, PATH, openSet, closedSet

	PATH = []
	closedSet = []
	openSet = []
	START = GRID[0][0]
	END = GRID[-1][-1]

	for i in range(DIMENSION):
		for j in range(DIMENSION):
			if GRID[i][j] == START:
				GRID[i][j].isStart = True
			elif GRID[i][j] == END:
				GRID[i][j].isEnd = True

			if GRID[i][j].isStart and not GRID[i][j] == START: 
				GRID[i][j].isStart = False

			elif GRID[i][j].isEnd and not GRID[i][j] == END: 
				GRID[i][j].isEnd = False

			GRID[i][j].isWall = False	
			GRID[i][j].neighbors = []	


def lowestFScore():
	"""
	Returns the index of the node in openSet which has the lowest FScore
	PARAMS: None
	RETURN: Int
	"""

	lowest = 0
	for i in range(len(openSet)):
		if openSet[lowest].f > openSet[i].f:
			lowest = i

	return lowest


while True:

	SCREEN.fill((255,255,255))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a] and len(openSet) == 0:
		PATHFINDING = True
		openSet.append(START)
		START.f = heuristic(START, END)

	if not PATHFINDING:
		update()
		if keys[pygame.K_r]:
			resetGrid()

	else:
				
		for row in GRID:
			for node in row:
				node.getNeighbors(GRID)

		if len(openSet) > 0:
			
			winner = lowestFScore()
			current = openSet[winner]

			if current == END:

				tmp = current

				PATH.append(current)

				while tmp.previous:
					PATH.append(tmp.previous)
					tmp = tmp.previous
				
				PATHFINDING = False

			openSet.pop(winner)
			closedSet.append(current)

			for neighbor in current.neighbors:
				
				if neighbor in closedSet:
					continue
				
				tGscore = current.g + 1

				if neighbor in openSet:
					if tGscore < neighbor.g:
						neighbor.g = tGscore
				
				else:
					neighbor.g = tGscore
					openSet.append(neighbor)

				neighbor.previous = current
				neighbor.h = heuristic(neighbor, END)
				neighbor.f = neighbor.g + neighbor.h

		else:
			# No solution
			print("NO PATH")
			PATHFINDING = False


	draw()

	pygame.display.update()





