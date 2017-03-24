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
        self.flag_cells()

    def get_coordinates(self):
        """ Get coordinates for this board. """
        coordinates = []
        for x in range(self.height):
            for y in range(self.width):
               coordinates.append((x, y))
        return coordinates

    def generate_board(self):
        """ Build out the initial board. """

        # Generate the initial board with 0s.
        board = [[0 for x in range(self.width)] for y in range(self.height)]

        # Set up the mines and surrounding counts.
        mines = random.sample(self.get_coordinates(), self.number_of_mines)
        for x, y in mines:
            board[x][y] = '*'

        return board

    def __repr__(self):
        """ Print the object representation to the screen. """
        return "<Minesweeper width:%s height:%s number_of_mines:%s>" % \
               (self.width, self.height, self.number_of_mines)

    def __str__(self):
        """ Print the board to the console. """
        result = ""
        for row in self.board:
            result += ''.join([str(x) for x in row]) + '\n'
        return result

    def count_mines(self):
        """ Count the number of mines currently on the board. """
        count = 0
        for row in self.board:
            for cell in row:
                if cell == '*':
                    count += 1
        return count

    def _is_on_board(self, coordinate):
        """ Return True if the coordinate is on the board.  Else, False. """
        x, y = coordinate

        if (x >= 0 and x < len(self.board)) and (y >= 0 and y < len(self.board)):
            return True
        return False

    def get_surrounding_cells(self, coord):
        """ Return the surrounding (x, y) coords. """
        surrounding = []
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                # Skip the current cell
                if (x, y) == coord:
                    continue

                try:
                    # If the surrounding coord is on the board, add it.
                    if self._is_on_board((x, y)):
                        surrounding.append((x, y))
                except:
                    print('trying to access: %s, %s' % (x, y))
                    print(self)

        return surrounding

    def flag_cells(self):
        """ Setup counts for all surrounding cells. """
        for coordinate in self.get_coordinates():

            for cell in self.get_surrounding_cells(coordinate):
                if self.board[cell[0]][cell[1]] == '*':
                    continue

                self.board[cell[0]][cell[1]] += 1