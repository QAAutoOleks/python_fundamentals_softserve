import unittest
import json_cars

class TestCarMethods(unittest.TestCase):

    def test_type(self):
        result_file = open("result.json", "r")
        result_dict = json_cars.json.load(result_file)
        self.assertTrue(type(result_dict) == list)


if __name__ == '__main__':
    unittest.main()