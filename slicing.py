import unittest

def invert_string(text: str) -> str:
    return text[::-1]


#unittest invert_slicing
class SlicingTest(unittest.TestCase):
    def test_invert_string(self):
        self.assertEqual(invert_string("a word"),"drow a")

if __name__ == "__main__":
    unittest.main()