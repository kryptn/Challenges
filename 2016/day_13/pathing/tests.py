import unittest

from path import itergrid, Directions, Cell, Grid

class TestBase(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(1, 1)
        self.grid = Grid(3, 3, [(0, 1)])

class TestCell(TestBase):
    def test_surrounding_empty_positions(self):
        dirs = [(0, 1), (1, 0), (2, 1), (1, 2)]
        sur = dict(self.cell.surrounding())
        
        self.assertEqual(sur['up'], (1, 2))
        self.assertEqual(len(sur.values()), len(dirs))
        for d in sur.values():
            self.assertIn(d, dirs)

    def test_surrounding_grid_positions(self):
        cell = self.grid[1][1]
        self.assertNotIn((0, 1), cell.neighbors.values())

    def test_cell_position(self):
        self.assertEqual((1, 1), self.cell.pos)

class TestGrid(TestBase):
    def test_neighbors(self):
        self.assertEqual(self.grid[0][0], self.grid[1][0].neighbors['left'])
        self.assertNotIn(self.grid[0][1], self.grid[0][0].neighbors.values())

    def test_walls(self):
        self.assertFalse(self.grid[0][1].passable)
        self.assertEqual(len(list(self.grid.traversable)), 8)




if __name__ == '__main__':
    unittest.main()
