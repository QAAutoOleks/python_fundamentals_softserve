import unittest
import practical_task_1


class TestCollections(unittest.TestCase):

    def test_map_and_compreh(self):
        self.assertEqual([1, 3, 5], practical_task_1.compreh_list('1,  2, 3'))
        self.assertEqual([1, 3, 5], practical_task_1.map_list('1,  2, 3'))
        self.assertEqual([1, -1, 2], practical_task_1.map_list('1,  -2, 0'))


if __name__ == '__main__':
    unittest.main()