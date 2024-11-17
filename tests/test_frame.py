import unittest
from src.frame import crop
from parameterized import parameterized

class FrameTest(unittest.TestCase):
    def test_single_row_and_column(self):
        result = crop(100, 100, 1, 1, 0)
        self.assertEqual(result, [0, 100, 0, 100])

    def test_default_index_when_larger_than_cells(self):
        result = crop(100, 100, 1, 1, 2)
        self.assertEqual(result, [0, 100, 0, 100])
    
    @parameterized.expand([
        (0, 0, 50, 0, 50),
        (1, 50, 100, 0, 50),
        (2, 0, 50, 50, 100),
        (3, 50, 100, 50, 100)
    ])
    def test_multiple_row_and_column(self, index, xOffset, width, yOffset, height):
        result = crop(100, 100, 2, 2, index)
        self.assertEqual(result[0], xOffset)
        self.assertEqual(result[1], width)
        self.assertEqual(result[2], yOffset)
        self.assertEqual(result[3], height)
    
if __name__ == '__main__':
    unittest.main()