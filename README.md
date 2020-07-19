# A-Pathfinding-Visualization
A pathfinding visualization of A* using python's pygame module

## Clone
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
* RESET: 'q'
* RESET GRID: 'r'

## COLOR REPRESENTATIONS:

* Turquoise ![#40e0d0](https://via.placeholder.com/15/f03c15/000000?text=+)  
	* _START NODE_
* Purple ![#9400d3](https://via.placeholder.com/15/f03c15/000000?text=+)  
	* _END NODE_
* Black ![#000](https://via.placeholder.com/15/f03c15/000000?text=+)  
	* _WALL_
* White ![#ffffff](https://via.placeholder.com/15/f03c15/000000?text=+)  
   * _OPEN PATH_
* Green ![#00ff00](https://via.placeholder.com/15/f03c15/000000?text=+)  
    * _NODES IN OPEN SET_
* Red  ![#ff0000](https://via.placeholder.com/15/f03c15/000000?text=+)  
	* _NODES IN CLOSED SET_
* Yellow ![#f0ff00](https://via.placeholder.com/15/f03c15/000000?text=+)  
	* _PATH FROM START TO END_

## Usage

```bash
cd src

python pathfind.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change


## License
[MIT](https://choosealicense.com/licenses/mit/)

*A Project by Jiankarlo A. Belarmino*
