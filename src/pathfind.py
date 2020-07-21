"""	
A pathfinding visualization of the A* Algorithm

Usage:

	python pathfind.py 

	optionally: 

		You may specify the width of the window, width must be divisible by 15, 
		if not the program will automatically adjust the width to be divisible by 15

		DEFAULT WIDTH: 600 

		python pathfind.py <WIDTH>
		python pathfind.py 900
	

Instructions:

	-> press ['s'] key to set your start node (DEFAULT -> TOP-LEFT)
	-> press ['e'] key to set your end node  (DEFAULT -> BOTTOM-RIGHT)
	
	-> press/hold [left-click] to set your walls
	-> press/hold [right-click] to remove walls
	
	-> press ['a'] to start visualization
	-> press ['0'] to stop visualization

	-> press ['o'] to set path to be across only
	-> press ['p'] to set path to be across and diagonal (DEFAULT)

	-> press ['q'] to reset back to before you clicked ['a']
	-> press ['r'] to reset grid back to it's initial state

	-> press ['1'] to evaluate 1 Node per frame
	-> press ['2'] to evaluate 5 Nodes per frame
	-> press ['3'] to evaluate 10 Nodes per frame (DEFAULT)

	-> press ['9'] to generate a random maze

COLOR REPRESENTATIONS:

	turquoise -> START NODE
	purple    -> END NODE
	black	  -> WALL
	white	  -> OPEN PATH
	green	  -> NODES IN OPEN SET
	red		  -> NODES IN CLOSED SET
	yellow	  -> PATH FROM START TO END

"""


import pygame
from node import Node
from math import sqrt
from random import randint
from sys import argv

WIDTH, HEIGHT = 600, 600

if len(argv) == 2:
	try:
		argv = int(argv[1])
		WIDTH = argv - (argv % 15)
		print(f"WIDTH SET TO {WIDTH}")
	except:
		print("Invalid Command line argument")

SPACE = 15
COLS = WIDTH // SPACE
ROWS = HEIGHT // SPACE 
GRID = []
SPEED = 10

pygame.init()
pygame.display.set_caption("A* PATHFINDING VISUALIZATION")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Creates GRID of Nodes
for i in range(ROWS):
	GRID.append([])
	for j in range(COLS):
		GRID[i].append(Node(i, j, SPACE))

# Default Start and End Nodes
GRID[0][0].isStart = True
GRID[-1][-1].isEnd = True

PATHFINDING = False

START = GRID[0][0]
END = GRID[-1][-1]

TEMP_PATH = []
PATH = []
foundPath = False
ACROSS = False

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
	Updates the state of the window every frame
	PARAMS: None
	RETURN: None
	"""

	global START, END

	for i in range(ROWS):
		for j in range(COLS):

			if GRID[i][j].rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
				keys = pygame.key.get_pressed()

				if keys[pygame.K_s] and not GRID[i][j].isEnd:
					setStart(i, j)

				elif keys[pygame.K_e] and not GRID[i][j].isStart:
					setEnd(i, j)

			GRID[i][j].update()


def heuristic(node, goal):
	"""
	Returns the Euclidean Distance from node to goal
	PARAMS: Node, Node
	RETURN: Int
	"""
	x1, y1 = node.column, node.row
	x2, y2 = goal.column, goal.row
	
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def resetPath():
	"""
	Resets grid keeping start and end and walls the same as when visualized
	PARAMS: None
	RETURN: None
	"""
	global PATH, TEMP_PATH, openSet, closedSet

	PATH = []
	TEMP_PATH = []
	closedSet = []
	openSet = []

	for i in range(ROWS):
		for j in range(COLS):
			GRID[i][j].neighbors = []

	print("Grid was reset")


def resetGrid():
	"""
	Resets grid back to its default state
	PARAMS: None
	RETURN: None
	"""

	global START, END, PATH, TEMP_PATH, openSet, closedSet, ACROSS

	PATH = []
	TEMP_PATH = []
	closedSet = []
	openSet = []
	ACROSS = False
	START = GRID[0][0]
	END = GRID[-1][-1]

	for i in range(ROWS):
		for j in range(COLS):
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

	print("Grid was reset back to initial state")


def lowestFScore():
	"""
	Returns the index of the node in openSet which has the lowest FScore
	PARAMS: None
	RETURN: Int
	"""

	lowest = 0
	for index in range(len(openSet)):
		if openSet[index].f < openSet[lowest].f:
			lowest = index

	return lowest


def stopFindingPath():
	"""
	Stops the visualization
	PARAMS: None
	RETURN: None
	"""
	global openSet

	openSet = []
	print("Finding path was stopped")


def setPathing(pathing): 
	"""
	Sets pathing to be either across & diagonal or across only
	PARAMS: Boolean
	Return: None

	"""

	global ACROSS

	if pathing:
		ACROSS = True
		print("Set to ACROSS ONLY")

	else:
		ACROSS = False
		print("Set to ACROSS & DIAGONAL")


def setSpeed(speed):
	"""
	Sets the speed of the algorithm
	PARAMS: Int
	RETURN: None
	"""

	global SPEED

	if speed == 1:
		SPEED = 1
		print("Set speed to SLOW")

	elif speed == 2:
		SPEED = 5
		print("Set speed to MEDIUM")

	elif speed == 3:
		SPEED = 10 
		print("Set speed to FAST")


def setStart(i, j):
	"""	
	Sets the Start Node
	PARAMS: Int, Int
	RETURN: None
	"""

	global START, GRID

	START.isStart = False
	GRID[i][j].isWall = False
	GRID[i][j].isStart = True
	START = GRID[i][j]



def setEnd(i, j):
	"""	
	Sets the End Node
	PARAMS: Int, Int
	RETURN: None
	"""

	global END, GRID

	END.isEnd = False
	GRID[i][j].isWall = False
	GRID[i][j].isEnd = True
	END = GRID[i][j]


def randomMaze():
	"""
	Generates a random maze 
	PARAMS: None
	RETURN: None
	"""

	global GRID, START, END

	for row in GRID:
		for node in row:
			if node == START or node == END:
				continue
			node.isWall = False
			if randint(0, 100) < 25:
				node.isWall = True


while True:

	SCREEN.fill((255,255,255))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			
			print("THANK YOU!")
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

		elif keys[pygame.K_q]:
			resetPath()

		elif keys[pygame.K_o]:
			setPathing(True)

		elif keys[pygame.K_p]:
			setPathing(False)

		elif keys[pygame.K_1]:
			setSpeed(1)

		elif keys[pygame.K_2]:
			setSpeed(2)

		elif keys[pygame.K_3]:
			setSpeed(3)

		elif keys[pygame.K_9]:
			randomMaze()

	else:
		
		if keys[pygame.K_0]:
			stopFindingPath()
				
		for row in GRID:
			for node in row:
				node.getNeighbors(GRID, ACROSS)

		if len(openSet) > 0:
			mult = SPEED
			while mult > 0 and len(openSet) > 0:
				
				mult -= 1

				winner = lowestFScore()
				current = openSet[winner]

				if current == END:

					tmp = current

					TEMP_PATH.append(current)

					while tmp.previous:
						TEMP_PATH.append(tmp.previous)
						tmp = tmp.previous
					
					PATHFINDING = False
					foundPath = True
					print("FOUND PATH")

				openSet.pop(winner)
				closedSet.append(current)

				for neighbor in current.neighbors:
					
					if neighbor in closedSet:
						continue
					
					tGscore = current.g + heuristic(current,  neighbor)

					newPath = False
					if neighbor in openSet:
						if tGscore < neighbor.g:
							neighbor.g = tGscore
							newPath = True
					
					else:
						neighbor.g = tGscore
						openSet.append(neighbor)
						newPath = True

					if newPath:
						neighbor.previous = current
						neighbor.h = heuristic(neighbor, END)
						neighbor.f = neighbor.g + neighbor.h

		else:

			print("NO PATH")
			PATHFINDING = False

	if foundPath and len(TEMP_PATH) != 0:

		PATH.append(TEMP_PATH.pop())
	
	draw()

	pygame.display.update()





