import unittest
from board import Board

class TestCellCanFindPotentialValues(unittest.TestCase):
    def setUp(self):
        self.board = Board('puzzles/numbers.txt')

    def test_cell_row_values(self):
        '''Test to make sure each cell is aware of the values in its row'''
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
        '''Test to make sure each cell is aware of the values in its column'''

        # 2 3 4 7 9
        cell = self.board.cell_at(0, 7)
        solution = set([2, 3, 4, 7, 9])
        self.assertEqual(cell.column_values(), solution)

        # 3 4 8
        cell = self.board.cell_at(4, 5)
        solution = set([3, 4, 8])
        self.assertEqual(cell.column_values(), solution)

        # 2 4 8 9
        cell = self.board.cell_at(5, 1)
        solution = set([2, 4, 8, 9])
        self.assertEqual(cell.column_values(), solution)

    def test_cell_block_values(self):
        '''Test to make sure each cell is aware of the values in its block'''

        # 1 2 3 6
        cell = self.board.cell_at(4, 4)
        solution = set([1, 2, 3, 6])
        self.assertEqual(cell.block_values(), solution)

        # 3 7 9
        cell = self.board.cell_at(7, 1)
        solution = set([3, 7, 9])
        self.assertEqual(cell.block_values(), solution)

        # 2 4 9
        cell = self.board.cell_at(5, 8)
        solution = set([2, 4, 9])
        self.assertEqual(cell.block_values(), solution)

    def test_cell_potential_values_are_correct(self):
        '''Test to make sure each cell can find its potential values'''

        # 3 6
        cell = self.board.cell_at(3, 6)
        solution = set([3, 6])
        self.assertEqual(cell.find_potential_values(), solution)

        # 4 7 9
        cell = self.board.cell_at(5, 3)
        solution = set([4, 7, 9])
        self.assertEqual(cell.find_potential_values(), solution)

        # 2 3 4
        cell = self.board.cell_at(1, 6)
        solution = set([2, 3, 4])
        self.assertEqual(cell.find_potential_values(), solution)

    def test_cell_with_value_has_no_potential_values(self):
        '''Test to make sure cells with values don't have potential values'''

        cell = self.board.cell_at(8, 5)
        self.assertEqual(cell.find_potential_values(), set())

        cell = self.board.cell_at(1, 1)
        self.assertEqual(cell.find_potential_values(), set())

        cell = self.board.cell_at(0, 7)
        self.assertNotEqual(cell.find_potential_values(), set())
