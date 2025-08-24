import unittest
import decorator_dividing
import range_generator


class TestFunctions(unittest.TestCase):

    def test_dividing(self):
        self.assertEqual(decorator_dividing.dividing(6, 3), 2)
        self.assertEqual(decorator_dividing.dividing(6, 0), None)

    def test_range_generator(self):
        value = range_generator.range_generator(1)
        next(value)
        self.assertRaises(StopIteration, lambda: next(value))


if __name__ == '__main__':
    unittest.main()