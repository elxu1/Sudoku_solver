import unittest
from board import Board

# To test, run python -m unitttest test_board
class TestBoardHasCorrectValues(unittest.TestCase):
    def setUp(self):
        self.testing_board = Board("puzzles/numbers.txt")

    def test_values(self):
        '''Tests if a board can properly read a text file'''
        self.assertEqual(self.testing_board.value_at(3, 1), 2)
        self.assertEqual(self.testing_board.value_at(5, 5), 3)
        self.assertEqual(self.testing_board.value_at(6, 2), 9)
        self.assertNotIsInstance(self.testing_board.value_at(8,8), int)
        with self.assertRaises(IndexError):
            index = self.testing_board.board_size + 1
            self.testing_board.value_at(index, index)

class TestBoardChecksProperly(unittest.TestCase):
    def setUp(self):
        self.row_puzzle = Board("puzzles/row.txt")
        self.column_puzzle = Board("puzzles/column.txt")
        self.block_puzzle = Board("puzzles/block.txt")
        self.complete_puzzle = Board("puzzles/complete.txt")

    def test_check_row(self):
        '''Tests if a board can make sure each row is correct'''
        self.assertTrue(self.row_puzzle.check_rows())
        self.assertFalse(self.column_puzzle.check_rows())
        self.assertFalse(self.block_puzzle.check_rows())
        self.assertTrue(self.complete_puzzle.check_rows())

    def test_check_column(self):
        '''Tests if a board can make sure each column is correct'''
        self.assertFalse(self.row_puzzle.check_columns())
        self.assertTrue(self.column_puzzle.check_columns())
        self.assertFalse(self.block_puzzle.check_columns())
        self.assertTrue(self.complete_puzzle.check_columns())

    def test_check_block(self):
        '''Tests if a board can make sure each block is correct'''
        self.assertFalse(self.row_puzzle.check_blocks())
        self.assertFalse(self.column_puzzle.check_blocks())
        self.assertTrue(self.block_puzzle.check_blocks())
        self.assertTrue(self.complete_puzzle.check_blocks())

    def test_is_completed(self):
        '''Tests if a board can detect if it is complete'''
        self.assertFalse(self.row_puzzle.is_completed())
        self.assertFalse(self.column_puzzle.is_completed())
        self.assertFalse(self.block_puzzle.is_completed())
        self.assertTrue(self.complete_puzzle.is_completed())