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