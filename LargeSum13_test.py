import unittest
import time

class TestCode(unittest.TestCase):

    def test_sum(self):
        start_time = time.time()

        lst = [
            46376937677490009712648124896970078050417018260538
        ]
        x = sum(lst)
        self.assertEqual(str(x)[:10], '4637693767')

        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    unittest.main()
