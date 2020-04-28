import utils
from cell import Cell

class Board:
    def __init__(self):

        # Initialize the board by reading in numbers from numbers.txt
        values = utils.read_puzzle("numbers.txt")
        self.board = []
        for row_num, row in enumerate(values):
            new_row = []
            for column_num, value in enumerate(row):
                cell = Cell(value, row_num, column_num, self)
                new_row.append(cell)
            self.board.append(new_row)

    def __str__(self):
        board = ""
        for row in self.board:
            for cell in row:
                board = board + str(cell) + ' '
            board = board + "\n"
        return board

    def value_at(self, row, column):
        return self.board[row][column].value
