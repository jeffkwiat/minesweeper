import unittest

from app import Minesweeper


class TestMinesweeper(unittest.TestCase):
    """
    Unit test class for Minesweeper.

    """

    def setUp(self):
        self.minesweeper = Minesweeper(7, 4, 4)

    @unittest.skip
    def test_width(self):
        """ Confirm our width is what we set. """
        for row in self.minesweeper.board:
            self.assertEqual(len(row), 7)

    @unittest.skip
    def test_height(self):
        """ Confirm our height is what we set. """
        self.assertEqual(len(self.minesweeper.board), 4)

    @unittest.skip
    def test_number_of_mines(self):
        """ Confirm the number of mines is what we set. """
        self.assertEqual(self.minesweeper.count_mines(), 4)

    @unittest.skip
    def test_get_surrounding_cells(self):
        """ Test the surrounding cells are returned accurately. """
        self.assertEqual(self.minesweeper.get_surrounding_cells((0, 0)),
                                                                 [(0, 1), (1, 0), (1, 1)])
        self.assertEqual(self.minesweeper.get_surrounding_cells((2, 2)),
                                                                [(1, 1), (1, 2), (1, 3), (2, 1),
                                                                (2, 3), (3, 1), (3, 2), (3, 3)])

        print(self.minesweeper)

    def test_is_on_board_true(self):
        """ Test these coordinates are on the board. """
        self.assertTrue(self.minesweeper._is_on_board((2, 4)))
        self.assertTrue(self.minesweeper._is_on_board((0, 0)))
        self.assertTrue(self.minesweeper._is_on_board((2, 2)))

    @unittest.skip
    def test_is_on_board_false(self):
        """ Test these coordinates are NOT on the board. """

        # x, y are both off the board.
        self.assertFalse(self.minesweeper._is_on_board((-1, -1)))

        # x is good, but y is off the board.
        self.assertFalse(self.minesweeper._is_on_board((3, 7)))

        # x is off the board, y is good
        self.assertFalse(self.minesweeper._is_on_board((4, 5)))


if __name__ == "__main__":
    unittest.main()