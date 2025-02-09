from src.group import Group
import unittest

class TestCell(unittest.TestCase):

    def setUp(self):
        input_file = [
            'A - Lara - 1 - 1 - N - AAAAAA\n',
            'A - Cara - 2 - 1 - S - ADGD\n',
            'A - Dara - 1 - 2 - E - A'
        ]
        self.group = Group(input_file)

    
    def test_numberOfAdventurers(self):
        self.assertEqual(self.group.getNumberOfAdventurers(), 3)

    def test_allDone(self):
        self.assertFalse(self.group.allDone())

    def test_addAdventurerDone(self):
        self.assertFalse(self.group.allDone())
        self.group.addAdventurerDone()
        self.assertEqual(self.group.getNumberOfAdventurersDone(), 1)
        self.group.addAdventurerDone()
        self.group.addAdventurerDone()
        self.assertTrue(self.group.allDone())