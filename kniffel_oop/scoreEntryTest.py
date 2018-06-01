import unittest
import die
from calcKniffel import CalcKniffel
from unittest.mock import MagicMock

class TestKniffel(unittest.TestCase):
    def setUp(self):
        self.testKniffelObj = CalcKniffel("testBlub")
        self.newDice = [die.Die(5) for x in range(5)]

    def testCalculate(self):
        self.testKniffelObj.isAllowed = MagicMock(return_value=True)

        self.assertEqual(self.testKniffelObj.points, 0)
        self.testKniffelObj.calculateKat(self.newDice)
        self.assertEqual(self.testKniffelObj.points, 50)

    def testIsAllowed(self):
        testRueckgabe = self.testKniffelObj.isAllowed(self.newDice)
        self.assertTrue(testRueckgabe)

    def testIsNotAllowed(self):
        self.newDice[0].value = 3 
        testRueckgabe = self.testKniffelObj.isAllowed(self.newDice)
        self.assertFalse(testRueckgabe)

    def testNot5Dice(self):
        del self.newDice[0]
        testRueckgabe = self.testKniffelObj.isAllowed(self.newDice)
        self.assertFalse(testRueckgabe)        

if __name__=='__main__':
    unittest.main()
