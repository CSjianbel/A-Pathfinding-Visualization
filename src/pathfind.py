import pygame
from node import Node


WIDTH, HEIGHT = (600, 600)

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

SPACE = 20
DIMENSION = WIDTH // SPACE

PATHFINDING = False
PATH = []

openSet = set()
closedSet = set()

GRID = []

for i in range(DIMENSION):
	GRID.append([])
	for j in range(DIMENSION):
		GRID[i].append(Node(i, j, SPACE))

for row in GRID:
	for node in row:
		node.getNeighbors(GRID)

# Default Start and End Nodes
GRID[0][0].isStart = True
GRID[-1][-1].isEnd = True

START = GRID[0][0]
END = GRID[-1][-1]

def draw():

	for i in range(DIMENSION):
		for j in range(DIMENSION):
			GRID[i][j].draw(SCREEN)


def update():

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
	x1, y1 = node.row, node.column
	x2, y2 = goal.column, goal.column

	return abs(x1 - x2) + abs(y1 - y2)


def resetGrid():
	"""
	Resets grid back to its default state
	PARAMS: None
	RETURN: None
	"""

	global START, END, PATH

	PATH = []
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


while True:

	SCREEN.fill((255,255,255))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		PATHFINDING = True
		openSet.enqueue(START)
		START.f = heuristic(START, END)

	if not PATHFINDING:
		update()
		draw()
		if keys[pygame.K_r]:
			resetGrid()
	else:
		
		if not openSet.isEmpty():
			current = openSet.lowestFScore()

			if current == END:
				#reconstruct path
				print("here")
				input()
				#PATHFINDING = False
				pass
			
			closedSet.add(current)
			for neighbor in current.neighbors:

				tGscore = current.g + 1
				if tGscore < neighbor.g:

					neighbor.previous = current
					neighbor.g = tGscore
					neighbor.f = neighbor.g + heuristic(neighbor, END)
					if openSet.includes(neighbor):
						openSet.enqueue(neighbor)


		else:

			print("No solution")
			input()
			#PATHFINDING = False

		print(len(closedSet))
		for i in closedSet:
			draw()
			pygame.draw.rect(SCREEN, (0,255,0), i.rect)


	pygame.display.update()





# def Astar(start, goal):
	
# 	global PATH

# 	# SET NEIGHBORS
# 	for row in GRID:
# 		for node in row:
# 			node.getNeighbors(GRID)


# 	# GCOST -> cost to reach node
# 	# HCOST -> distance from end node
# 	openSet = QueueFrontier()

# 	openSet.enqueue(start)

# 	start.g = 0

# 	start.f = heuristic(start, goal)

# 	while not openSet.isEmpty():

# 		current = openSet.lowestFScore()
# 		PATH.append(current)

# 		if current == GRID[END[0]][END[1]]:
# 			# reconstruct path

# 			while current.previous:
				
# 				PATH.append(current.previous)
# 				current = current.previous

# 			return True

# 		for neighbor in current.neighbors:
			
# 			tGscore = current.g + 1

# 			if tGscore < neighbor.g:

# 				neighbor.previous = current
# 				neighbor.g = tGscore
# 				neighbor.f = neighbor.g + heuristic(neighbor, goal)
# 				if neighbor not in openSet.queue:
# 					openSet.queue.append(neighbor)

# 	return False


