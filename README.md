# A Pathfinding Visualization

A pathfinding visualization of _A\*_ Algorithm using python's pygame module.

_A\*_ is a famous algorithm for search problems in Computer Science. _A\*_ guarantees the shortest path from 2 nodes.
It uses heuristics to decide which node to explore next, prioritizing nodes that are known to be closer to the goal based on the Euclidean distance that is returned by a heuristic function.

To visualize the algorithm a 2d grid in pygame was created, and represented each cell of the grid as a node. A node can either be a wall, start, or end. The pathing can either be both diagonal and across (default), or it can only be across. Usage and Basic Controls may be found below and in src/pathfind.py.

## Clone

```bash
git clone https://github.com/CSjianbel/A-Pathfinding-Visualization.git
```

## Setup

Install Dependencies through package manager [pip](https://pip.pypa.io/en/stable/installing/)

```bash
pip install -r requirements.txt
```

## Basic Controls

- **START:** 's'
- **END:** 'e'<br /><br />

- **WALL:** left click
- **REMOVE WALL:** right click<br /><br />

- **FIND PATH:** 'a'
- **STOP FINDING PATH:** '0'<br /><br />

- **SET PATHING:**

  - **SET ACROSS AND DIAGONAL:** 'p' _(DEFAULT)_
  - **SET ACROSS ONLY:** 'o'<br /><br />

- **SET SPEEDS:**

  - **3:** FAST (DEFAULT)
  - **2:** MEDIUM
  - **1:** SLOW<br /><br />

- **GENERATE RANDOM MAZE:** '9'<br /><br />

- **RESETS:**
  - **SOFT RESET:** 'q'
  - **HARD RESET:** 'r'<br /><br />

## COLOR REPRESENTATIONS:

- **Turquoise** ![#40e0d0](https://via.placeholder.com/15/40e0d0/000000?text=+)
  - _START NODE_
- **Purple** ![#9400d3](https://via.placeholder.com/15/9400d3/000000?text=+)
  - _END NODE_
- **Black** ![#000](https://via.placeholder.com/15/000/000000?text=+)
  - _WALL_
- **White** ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)
  - _OPEN PATH_
- **Green** ![#00ff00](https://via.placeholder.com/15/00ff00/000000?text=+)
  - _NODES IN OPEN SET_
- **Red** ![#ff0000](https://via.placeholder.com/15/ff0000/000000?text=+)
  - _NODES IN CLOSED SET_
- **Yellow** ![#f0ff00](https://via.placeholder.com/15/f0ff00/000000?text=+)
  - _PATH FROM START TO END_

## Usage

```bash
python pathfind.py
```

Optionally you may change the WIDTH of the window. Width must be divisible by 15,
if not the program will automatically adjust the specified width to be divisible by 15.
Invalid command line arguments will result to default width of 600.

```bash
python pathfind.py --width

python pathfind.py --width 900

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
  			Enter width of the pygame window : default - 600
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)

_A Project by Jiankarlo A. Belarmino_
