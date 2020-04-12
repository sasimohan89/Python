import main
import unittest

class TestMain(unittest.TestCase):
    def test_add_five(self):
        test_param = 10
        result = main.add_five(test_param)
        self.assertEqual(result, 15)

    def test1_add_five(self):
        test_param = 'adfg'
        result = main.add_five(test_param)
        self.assertIsInstance(result, ValueError)

    def test2_add_five(self):
        test_param = None
        result = main.add_five(test_param)
        self.assertEqual(result, 'please enter number')

    def test3_add_five(self):
        test_param = ''
        result = main.add_five(test_param)
        self.assertEqual(result, 'please enter number')

unittest.main()