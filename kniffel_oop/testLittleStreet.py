import unittest
import die
from calcLittleStreet import CalcLittelStreet
from unittest.mock import MagicMock

class TestKniffel(unittest.TestCase):
    def setUp(self):
        self.testLStreetObj = CalcLittelStreet("testBlub")
        self.newDice = [die.Die(3), die.Die(2), die.Die(4), die.Die(1), die.Die(3)]


    def testCalculate(self):
        self.testLStreetObj.isAllowed = MagicMock(return_value=True)

        self.assertEqual(self.testLStreetObj.points, 0)
        self.testLStreetObj.calculateKat(self.newDice)
        self.assertEqual(self.testLStreetObj.points, 30)

    def testIsAllowed(self):
        testRueckgabe = self.testLStreetObj.isAllowed(self.newDice)
        self.assertTrue(testRueckgabe)

if __name__=='__main__':
    unittest.main()