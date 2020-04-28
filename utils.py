def try_eval(char):
    try:
        return eval(char)
    except:
        return None

def read_puzzle(puzzle_file):
    '''Reads a text file containing the sudoku puzzle and returns a 9x9 array'''
    file = open(puzzle_file, "r")
    puzzle_arr = []

    # Read each line
    for _ in range(9):
        line = file.readline()

        # Turn each line into an array of integers
        numbers = line.split(' ')
        numbers = list(map(try_eval, numbers))
        puzzle_arr.append(numbers)

    return puzzle_arr

def block_number(row, col):
    '''Defines the block a cell is located in'''
    return (row//3) * 3 + (col//3)

def block_ranges(block):
    '''Helper function to get block ranges'''
    row_start = (block // 3) * 3
    row_end = row_start + 3
    col_start = (block % 3) * 3
    col_end = col_start + 3
    return [range(row_start, row_end), range(col_start, col_end)]