import utils
from cell import Cell

class Board:
    def __init__(self):

        # Initialize the board by reading in numbers from numbers.txt
        values = utils.read_puzzle("numbers.txt")
        self.board = []
        for rowNum, row in enumerate(values):
            newRow = []
            for columnNum, value in enumerate(row):
                cell = Cell(value, rowNum, columnNum, self)
                newRow.append(cell)
            self.board.append(newRow)

    def __str__(self):
        board = ""
        for row in self.board:
            for cell in row:
                board = board + str(cell) + ' '
            board = board + "\n"
        return board

b = Board()
print(b)