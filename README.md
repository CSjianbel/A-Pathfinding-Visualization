# A-Pathfinding-Visualization
A pathfinding visualization of _A*_ Algorithm using python's pygame module. 

_A*_ is a famous algorithm for search problems in Computer Science. _A*_ guarantess the shortest path from 2 nodes. 
It uses heuristics to decide which node to explore next, prioritizing nodes that are known to be closer to the goal based on the Euclidean distance that is returned by a heuristic function. 

To visualize the algorithm I created a 2d grid in pygame, and represented each cell of the grid as a node. A node can either be qvwall, start, or end. The path can either be both diagonal and across (default), or it can only be across. Usage and Basic Controls may be found below and in src/pathfind.py.  
  
## Clone
```bash
git clone https://github.com/CSjianbel/A-Pathfinding-Visualization.git
```

## Setup

Install Dependencies through package manager [pip](https://pip.pypa.io/en/stable/installing/)

```bash
pip install pygame
```

## Basic Controls
  
* START: 's' 
* END: 'e' 
* WALL: left click
* REMOVE WALL: right click
  
* FIND PATH: 'a'
* STOP FINDING PATH: '0'
  
* SET PATHING:  
	* SET ACROSS AND DIAGONAL: 'p' (DEFAULT)  
	* SET ACROSS ONLY: 'o'
  
* SET SPEEDS: 
	* '3' FAST (DEFAULT)
	* '2' MEDIUM 
	* '1' SLOW
  
* GENERATE RANDOM MAZE: '9'

* RESET: 'q'
* RESET GRID: 'r'


## COLOR REPRESENTATIONS:

* Turquoise ![#40e0d0](https://via.placeholder.com/15/40e0d0/000000?text=+)  
	* _START NODE_
* Purple ![#9400d3](https://via.placeholder.com/15/9400d3/000000?text=+)  
	* _END NODE_
* Black ![#000](https://via.placeholder.com/15/000/000000?text=+)  
	* _WALL_
* White ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)  
   * _OPEN PATH_
* Green ![#00ff00](https://via.placeholder.com/15/00ff00/000000?text=+)  
    * _NODES IN OPEN SET_
* Red  ![#ff0000](https://via.placeholder.com/15/ff0000/000000?text=+)  
	* _NODES IN CLOSED SET_
* Yellow ![#f0ff00](https://via.placeholder.com/15/f0ff00/000000?text=+)  
	* _PATH FROM START TO END_

## Usage

```bash
cd src

python pathfind.py
```
  
Optionally you may change the WIDTH of the window. Width must be divisible by 15, 
if not the program will automatically adjust the specified width to be divisible by 15.
Invalid command line arguments will result to default width of 600.

```bash
python pathfind.py <WIDTH>
  
python pathfind.py 900
```
  
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
  
  
### License
[MIT](https://choosealicense.com/licenses/mit/)

*A Project by Jiankarlo A. Belarmino*
