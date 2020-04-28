import utils

class Cell:
    '''Represents a cell on the 9x9 board'''

    def __init__(self, value, row, column, board):
        self.value = value
        self.row = row
        self.column = column
        self.board = board

    def __str__(self):
        return str(self.value) if type(self.value) is int else '*'

    def rowValues(self):
        '''Get all the values in the same row'''
        return self.board[self.row]

    def columnValues(self):
        '''Get all the values in the same column'''
        values = []
        for row in self.board:
            values.append(row[self.column])
        return values

    def blockValues(self):
        '''Get all the values in the same 3x3 block'''