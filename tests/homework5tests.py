import unittest
from homework5 import Hometask


class MyTestCase(unittest.TestCase):
    def test_common_numbers(self):
        self.assertEqual(Hometask.common_numbers(), [1, 2, 3, 5, 8, 13])


if __name__ == '__main__':
    unittest.main()
