#Importing the testing frameworks
import unittest
from peg_math import is_valid_jump_distance, rating

#Our test class
class TestPegMath(unittest.TestCase):
    #Function names should start with "test" so unittest can find them
    def test_is_valid_jump_distance(self):
        #Valid jump (5-3=2)
        self.assertTrue(is_valid_jump_distance(3, 5))
        #Invalid Jump because distance is 4-3=1
        self.assertFalse(is_valid_jump_distance(3, 4))

    #Checking if rating function returns correct strings
    def test_rating(self):
        self.assertEqual(rating(1), "Outstanding")
        self.assertEqual(rating(2), "Very Good")
        self.assertEqual(rating(3), "Good")
        self.assertEqual(rating(6), "Average")

#Run the tests
if __name__ == "__main__":
    unittest.main()
