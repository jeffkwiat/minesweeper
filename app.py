import random
import unittest


class Minesweeper(object):
    """
    Minesweeper game.

    """

    def __init__(self, width, height, number_of_mines):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines
        self.board = self.generate_board()

    def generate_board(self):
        board = []
        available_positions = []
        for row_index in range(self.height):
            row = []
            for col_index in range(self.width):
                row.append('0')
                available_positions.append((row_index, col_index))
            board.append(row)

        mines = random.sample(available_positions, self.number_of_mines)
        for mine_x, mine_y in mines:
            board[mine_x][mine_y] = '*'
        return board

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    def count_mines(self, cell):
        # TODO: implement
        pass


    def flag_number_of_mines(self):
        for row_index in range(self.height):
            for col_index in range(self.width):




class TestMinesweeper(unittest.TestCase):
    """
    Comment for this test

    """

    def setUp(self):
        self.minesweeper = Minesweeper(7, 4, 4)

    def test_example(self):
        pass

if __name__ == "__main__":
    game = Minesweeper(7, 4, 4)
    game.generate_board()
    game.print_board()