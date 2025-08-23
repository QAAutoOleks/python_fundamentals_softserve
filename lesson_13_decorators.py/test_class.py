import unittest
import decorator_dividing


class TestFunctions(unittest.TestCase):

    def test_dividing(self):
        self.assertEqual(decorator_dividing.dividing(6, 3), 2)


if __name__ == '__main__':
    unittest.main()