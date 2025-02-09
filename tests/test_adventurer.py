from src.adventurer import Adventurer
import unittest

class TestCell(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer('Carbon', 1, 1, 'N', 'A')
        self.adventurer_done = Adventurer('Carbon', 1, 1, 'N', '')

    def test_setOrientation(self):
        self.adventurer.setOrientation('G')
        self.assertEqual(self.adventurer.getOrientation(), 'O')
        self.adventurer.setOrientation('G')
        self.assertEqual(self.adventurer.getOrientation(), 'S')
        self.adventurer.setOrientation('G')
        self.assertEqual(self.adventurer.getOrientation(), 'E')
        self.adventurer.setOrientation('G')
        self.assertEqual(self.adventurer.getOrientation(), 'N')
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getOrientation(), 'E')
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getOrientation(), 'S')
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getOrientation(), 'O')
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getOrientation(), 'N')

    def test_addTreasure(self):
        self.adventurer.addTreasure()
        self.assertEqual(self.adventurer.getTreasure(), 1)

    def test_isDone(self):
        self.assertFalse(self.adventurer.isDone())
        self.assertTrue(self.adventurer_done.isDone())

    def test_getNextMove(self):
        self.assertEqual(self.adventurer.getNextMove(), 'A')
        # On vérifie que le mouvement a bien été enlevé de la séquence
        self.assertEqual(self.adventurer.getNextMove(), '')
    
    def test_getNextCell(self):
        self.assertEqual(self.adventurer.getNextCell(), (1, 0))
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getNextCell(), (2, 1))
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getNextCell(), (1, 2))
        self.adventurer.setOrientation('D')
        self.assertEqual(self.adventurer.getNextCell(), (0, 1))
        self.adventurer.setOrientation('D')