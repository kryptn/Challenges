# Pathing
Just playing with some pathing 


## Basics

```python3

>>> import path

>>> path.itergrid(2,2) # generator for x-y coordinate blocks
<generator object itergrid at 0x7fb911aa0990>

>>> list(_)
[(0, 0), (0, 1), (1, 0), (1, 1)]

>>> list(path.itergrid(2,2, 2, 2)) # Has offset arguments too (x, y, x-offset, y-offset)
[(2, 2), (2, 3), (3, 2), (3, 3)]

>>> grid = path.Grid(5, 5)

>>> print(grid)
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .

>>> grid[2][2]
<Cell 2, 2>

>>> pprint(grid[2][2].neighbors)
{'down': <Cell 2, 1>,
 'left': <Cell 1, 2>,
 'right': <Cell 3, 2>,
 'up': <Cell 2, 3>}

>>> grid[2][1] is grid[2][2].neighbors['down']
True

>>> print(path.Grid(5, 5, path.itergrid(2, 2))) #Walls
█ █ . . .
█ █ . . .
. . . . .
. . . . .
. . . . .

>>> print(path.Grid(5, 5, path.itergrid(3, 3, 1, 1))) #offset walls
. . . . .
. █ █ █ .
. █ █ █ .
. █ █ █ .
. . . . .

```

## Some pathfinding

```python3
>>> import path

>>> grid = path.Grid(5, 5, path.itergrid(3, 3, 1, 1))

>>> grid[0][2].visited = True

# I couldn't think of a name.
>>> list(grid.somename) #Next path finding iteration
[<Cell 0, 1>, <Cell 0, 3>]


```
