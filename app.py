import random


class Minesweeper(object):
    """
    Implementing a simple Minesweeper board.

    """

    def __init__(self, width, height, number_of_mines):
        self.width = width
        self.height = height
        self.number_of_mines = number_of_mines
        self.board = self.generate_board()

    def get_coordinates(self):
        """ Get coordinates for this board. """
        coordinates = []
        for x in range(self.width):
            for y in range(self.height):
               coordinates.append((x, y))
        return coordinates

    def generate_board(self):
        """ Build out the initial board. """

        # Generate the initial board with 0s.
        board = [['0' for x in range(self.width)] for y in range(self.height)]
        coordinates = self.get_coordinates()
        # Set up the mines and surrounding counts.
        mines = random.sample(coordinates, self.number_of_mines)
        for x, y in mines:
            board[y][x] = '*'

        # Setup counts for all surrounding cells.
        for coordinate in coordinates:
            for cell in self.get_surrounding_cells(coordinate):
                board[cell[0], cell[1]] = int(board[cell[0], cell[1]]) + 1

        return board

    def __repr__(self):
        """ Print the object representation to the screen. """
        return "<Minesweeper width:%s height:%s number_of_mines:%s>" % \
               (self.width, self.height, self.number_of_mines)

    def __str__(self):
        """ Print the board to the console. """
        result = ""
        for row in self.board:
            result += ''.join(row) + '\n'
        return result

    def count_mines(self):
        """ Count the number of mines currently on the board. """
        count = 0
        for row in self.board:
            for cell in row:
                if cell == '*':
                    count += 1
        return count

    def get_surrounding_cells(self, coord):
        """ Return the surrounding (x, y) coords. """
        surrounding = []
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                # Skip the current cell
                if (x, y) == coord:
                    continue

                # If the surrounding coord is on the board, add it.
                if (0 <= x <= len(self.board)) and \
                    (0 <= y <= len(self.board[x])):
                    surrounding.append((x, y))
        return surrounding