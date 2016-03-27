import sys
import unittest

from mothers_day import *

class TestMothersDay(unittest.TestCase):

    def test_mothers_day(self):
        self.assertEqual(mothers_day(), "Happy Mother's Day, Mom!")

    def test_better_mothers_day(self):
        self.assertEqual(better_mothers_day("Susan"), "Happy Mother's Day, Susan!")

    def test_best_mothers_day(self):
        self.assertEqual(best_mothers_day("Susan"), "Happy Mother's Day, Susan!")
        self.assertEqual(best_mothers_day(), "Happy Mother's Day, Mom!")

    
    def test_holiday_greeting(self):
        self.assertEqual(holiday_greeting("Beyonce", "Jay-Z", "Fourth of July"), "Happy Fourth of July, Beyonce! - From Jay-Z")
        self.assertEqual(holiday_greeting("Beyonce", "Jay-Z"), "Happy Mother's Day, Beyonce! - From Jay-Z")
        self.assertEqual(holiday_greeting("Beyonce"), "Happy Mother's Day, Beyonce! - From Your Favorite Child")
        self.assertEqual(holiday_greeting(), "Happy Mother's Day, Mom! - From Your Favorite Child")



if __name__ == '__main__':
    unittest.main()
