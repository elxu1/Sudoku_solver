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
        '''Retreives the value at a row and column number'''
        return self.board[row][column].value

    def is_completed(self):
        '''Determines if the board is completed correctly'''
        return self.check_rows() and self.check_columns() and self.check_blocks()

    def check_rows(self):
        '''Checks if all the rows are correct'''
        values = set(range(1,10))
        for row in self.board:
            if set(row) != values:
                return False
        return True

    def check_columns(self):
        '''Checks if all the columns are correct'''
        values = set(range(1,10))

        # Iterate through cells of the first row
        for cell in self.board[0]:

            # Tell each cell to get all the values in its column
            current_column = set(cell.column_values())
            if current_column != values:
                return False
        return True

    def check_blocks(self):
        '''Checks if all the blocks are correct'''
        values = set(range(1,10))

        # Iterate each block
        for block_num in range(1,10):
            [row_range, column_range] = utils.block_ranges(block_num)
            block_values = []

            # Collect values from each block
            for row in row_range:
                for column in column_range:
                    block_values.append(self.value_at(row, column))

                    # If the values in the block aren't 1 through 9
                    if block_values != values:
                        return False
        return True