import unittest
from board import Board

class TestCellCanFindPotentialValues(unittest.TestCase):
    def setUp(self):
        self.board = Board('puzzles/numbers.txt')

    def test_cell_row_values(self):
        # 2 4 6 9
        cell = self.board.cell_at(4, 0)
        solution = set([2, 4, 6, 9])
        self.assertEqual(cell.row_values(), solution)

        # 3 4 7
        cell = self.board.cell_at(6, 2)
        solution = set([3, 4, 7])
        self.assertEqual(cell.row_values(), solution)

        # 1 5 9
        cell = self.board.cell_at(2, 5)
        solution = set([1, 5, 9])
        self.assertEqual(cell.row_values(), solution)

    def test_cell_column_values(self):
        pass

    def test_cell_block_values(self):
        pass

    def test_cell_potential_values_are_correct(self):
        pass

    def test_cell_with_value_has_no_potential_values(self):
        pass