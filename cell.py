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
        cells = self.board[self.row]
        values = map(lambda cell: cell.value, cells)

        # Remove the none values and the value of this cell
        values = set(filter(None, values))
        return values - set([self.value])

    def column_values(self):
        '''Get all the values in the same column'''
        values = set()
        for row in self.board:

            # Get the value from each cell in a column
            value = row[self.column].value
            values.add(value)
        return values

    def block_values(self):
        '''Get all the values in the same 3x3 block'''

        # Get the row and column ranges
        block = block_number(self.row, self.column)
        [row_range, column_range] = block_ranges(block)

        # Iterate the ranges and collect the values from the board
        values = set()
        for row in row_range:
            for column in column_range:
                value = self.board.value_at(row, column)
                values.add(value)
        return values

    def find_potential_values(self):
        if type(self.value) == 'int':
            return []
        else:
            potential_values = set(range(1, 10))

            # The used values is the set union of the row, column, and block values
            used_values = self.row_values().union(self.column_values()).union(self.block_values())

            # The potential values is just the set difference of all values and the used values
            return potential_values.difference(used_values)