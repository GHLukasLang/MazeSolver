import unittest

from objects import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )


    def test_visited_false(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for j in range(m1.num_cols):
            for i in range(m1.num_rows):
                self.assertEqual(m1._cells[i][j].visited, False)

if __name__ == "__main__":
    unittest.main()