from src.map import Map
import unittest



class TestCell(unittest.TestCase):

    def setUp(self):
        """
        .   M   .   .   .
        .   .   M   .   A
        M   .   M   1   .
        .   1   .   .   2
        .   A   .   M   .

        """

        input_file_1 = [
            'C - 5 - 5\n',
            'M - 0 - 2\n',
            'M - 1 - 0\n',
            'M - 2 - 1\n',
            'M - 2 - 2\n',
            'M - 3 - 4\n',
            'T - 1 - 3 - 1\n',
            'T - 3 - 2 - 1\n',
            'T - 4 - 3 - 2\n',
            'A - Lara - 1 - 4 - E - GADAA\n',
            'A - Kara - 4 - 1 - S - AA\n'
        ]

        self.map = Map(input_file_1)
    
    def test_getAccissibility(self):
        self.assertTrue(self.map.getAccessibility(0, 3))
        self.assertTrue(self.map.getAccessibility(1, 3))
        self.assertFalse(self.map.getAccessibility(0, 2))
        self.assertFalse(self.map.getAccessibility(1, 4))
        self.assertFalse(self.map.getAccessibility(0, 5))
        self.assertFalse(self.map.getAccessibility(5, 0))
        self.assertFalse(self.map.getAccessibility(-1, 0))
        self.assertFalse(self.map.getAccessibility(0, -1))

    def test_hasTreasure(self):
        self.assertTrue(self.map.hasTreasures(1, 3))
        self.assertFalse(self.map.hasTreasures(0, 2))
        self.assertFalse(self.map.hasTreasures(1, 4))

    def test_hasTreasures_removeTreasure(self):
        self.assertTrue(self.map.hasTreasures(1, 3))
        self.map.removeTreasure(1, 3)
        self.assertFalse(self.map.hasTreasures(1, 3))
