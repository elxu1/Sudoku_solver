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
    file.close()
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

def transpose(grid):
    '''Takes the transpose of a grid'''

    # Set up an empty grid to put the transposed grid
    column_range = range(len(grid[0]))
    row_range = range(len(grid))
    transpose_grid = [[] for _ in column_range]

    # Iterate by row through the grid
    # Assign the value to each column of the transpose grid
    for row_num in row_range:
        for column_num in column_range:
            cell_value = grid[row_num][column_num]
            transpose_grid[column_num].append(cell_value)
    return transpose_grid
