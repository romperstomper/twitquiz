import countstr
import unittest

class TestCountstr(unittest.TestCase):
    def test_countit(self):
        self.assertEqual(
            countstr.countit('aaaabbbcca'),
                [("a", 4), ("b", 3), ("c", 2), ("a", 1)])

if __name__ == '__main__':
    unittest.main()