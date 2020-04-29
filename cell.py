from utils import block_number, block_ranges

class Cell:
    '''Represents a cell on the 9x9 board'''

    def __init__(self, value, row, column, board):
        self.value = value
        self.row = row
        self.column = column
        self.board = board

    def __str__(self):
        return str(self.value) if type(self.value) is int else '*'

    def row_values(self):
        '''Get all the values in the same row'''
        return self.board[self.row]

    def column_values(self):
        '''Get all the values in the same column'''
        values = []
        for row in self.board:
            values.append(row[self.column])
        return values

    def block_values(self):
        '''Get all the values in the same 3x3 block'''

        # Get the row and column ranges
        block = block_number(self.row, self.column)
        [row_range, column_range] = block_ranges(block)

        # Iterate the ranges and collect the values from the board
        values = []
        for row in row_range:
            for column in column_range:
                values.append(self.board.value_at(row, column))
        return values