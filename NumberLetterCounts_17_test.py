import unittest
from NumberLetterCounts_17 import translate

class TestTranslate(unittest.TestCase):
    def test_translate_zero(self):
        self.assertEqual(translate(0), "")

    def test_translate_single_digit(self):
        self.assertEqual(translate(1), "one")
        self.assertEqual(translate(2), "two")
        self.assertEqual(translate(3), "three")
        self.assertEqual(translate(4), "four")
        self.assertEqual(translate(5), "five")
        self.assertEqual(translate(6), "six")
        self.assertEqual(translate(7), "seven")
        self.assertEqual(translate(8), "eight")
        self.assertEqual(translate(9), "nine")

    def test_translate_teens(self):
        self.assertEqual(translate(10), "ten")
        self.assertEqual(translate(11), "eleven")
        self.assertEqual(translate(12), "twelve")
        self.assertEqual(translate(13), "thirteen")
        self.assertEqual(translate(14), "fourteen")
        self.assertEqual(translate(15), "fifteen")
        self.assertEqual(translate(16), "sixteen")
        self.assertEqual(translate(17), "seventeen")
        self.assertEqual(translate(18), "eighteen")
        self.assertEqual(translate(19), "nineteen")

    def test_translate_two_digits(self):
        self.assertEqual(translate(20), "twenty")
        self.assertEqual(translate(21), "twenty-one")
        self.assertEqual(translate(30), "thirty")
        self.assertEqual(translate(45), "forty-five")
        self.assertEqual(translate(50), "fifty")
        self.assertEqual(translate(67), "sixty-seven")
        self.assertEqual(translate(70), "seventy")
        self.assertEqual(translate(89), "eighty-nine")
        self.assertEqual(translate(90), "ninety")
        self.assertEqual(translate(99), "ninety-nine")

    def test_translate_hundreds(self):
        self.assertEqual(translate(100), "one hundred")
        self.assertEqual(translate(101), "one hundred and one")
        self.assertEqual(translate(110), "one hundred and ten")
        self.assertEqual(translate(119), "one hundred and nineteen")
        self.assertEqual(translate(120), "one hundred and twenty")
        self.assertEqual(translate(200), "two hundred")
        self.assertEqual(translate(300), "three hundred")
        self.assertEqual(translate(456), "four hundred and fifty-six")
        self.assertEqual(translate(500), "five hundred")
        self.assertEqual(translate(678), "six hundred and seventy-eight")
        self.assertEqual(translate(700), "seven hundred")
        self.assertEqual(translate(890), "eight hundred and ninety")
        self.assertEqual(translate(900), "nine hundred")

    def test_translate_various(self):
        self.assertEqual(translate(1001), "one thousand one")
        self.assertEqual(translate(1111), "one thousand one hundred and eleven")
        self.assertEqual(translate(1200), "one thousand two hundred")
        self.assertEqual(translate(2000), "two thousand")
        self.assertEqual(translate(3456), "three thousand four hundred and fifty-six")
        self.assertEqual(translate(5000), "five thousand")
        self.assertEqual(translate(6789), "six thousand seven hundred and eighty-nine")

if __name__ == '__main__':
    unittest.main()