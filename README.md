# A-Pathfinding-Visualization
A pathfinding visualization of _A*_ Algorithm using python's pygame module. 

_A*_ is a famous algorithm for search problems in Computer Science. _A*_ guarantess the shortest path from 2 nodes. 
It uses heuristics to decide which nodes to explore next prioritizing nodes that are known to be closer to the goal based on the heuristic function. 

To visualize this I created a 2d grid in pygame, and represented each cell of the grid as a node. A node can be a wall, start, or end. The path can either be both diagonal and across, or it can only be across. For my heuristic function I just calculated the Eucldiean distance given from 2 nodes.  


```bash
git clone https://github.com/CSjianbel/A-Pathfinding-Visualization.git
```

## Setup

Install Dependencies through package manager [pip](https://pip.pypa.io/en/stable/installing/)
And clone repository

```bash
pip install pygame
```

## Basic Controls

* START: 's' 
* END: 'e' 
* WALL: left click
* REMOVE WALL: right click
* FIND PATH: 'a'
* SET ACROSS ONLY: 'o'
* SET ACROSS AND DIAGONAL: 'p' (default)
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change


### License
[MIT](https://choosealicense.com/licenses/mit/)

*A Project by Jiankarlo A. Belarmino*
