import unittest

from app import Minesweeper


class TestMinesweeper(unittest.TestCase):
    """
    Unit test class for Minesweeper.

    """

    def setUp(self):
        self.minesweeper = Minesweeper(7, 4, 4)

    def test_width(self):
        """ Confirm our width is what we set. """
        for row in self.minesweeper.board:
            self.assertEqual(len(row), 7)

    def test_height(self):
        """ Confirm our height is what we set. """
        self.assertEqual(len(self.minesweeper.board), 4)

    def test_number_of_mines(self):
        """ Confirm the number of mines is what we set. """
        self.assertEqual(self.minesweeper.count_mines(), 4)

    def test_flag_surrounding_cells(self):
        """ Test the surrounding cells are returned accurately. """
        # self.assertEqual(self.minesweeper.get_surrounding_cells((0, 0)),
        #                                                         [(0, 1), (1, 0), (1, 1)])
        self.assertEqual(self.minesweeper.get_surrounding_cells((2, 2)),
                                                                [(1, 1), (1, 2), (1, 3), (2, 1),
                                                                 (2, 3), (3, 1), (3, 2), (3, 3)])

        print(self.minesweeper)


if __name__ == "__main__":
    unittest.main()