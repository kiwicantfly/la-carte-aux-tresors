from src.cell import Cell
import unittest

class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()

    def test_accessibility(self):
        self.assertTrue(self.cell.getAccessibility())