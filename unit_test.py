import unittest

from main import FloodFill


class FloodFillTest(unittest.TestCase):
    def setUp(self) -> None:
        self.image = [[0, 2, 0, 1, 0, 2],
                      [1, 0, 1, 2, 1, 2],
                      [1, 1, 2, 1, 1, 1],
                      [1, 2, 0, 1, 0, 2],
                      [1, 2, 0, 2, 2, 2],
                      [0, 1, 0, 2, 1, 0]]
        self.chosen_color = 1


    def tearDown(self) -> None:
        self.image = [[0, 2, 0, 1, 0, 2],
                      [1, 0, 1, 2, 1, 2],
                      [1, 1, 2, 1, 1, 1],
                      [1, 2, 0, 1, 0, 2],
                      [1, 2, 0, 2, 2, 2],
                      [0, 1, 0, 2, 1, 0]]
    def test_flood_fill(self):
        result = FloodFill.flood_fill(self.image, self.chosen_color)
        self.assertEqual(result,
                         [[1, 2, 0, 1, 0, 2],
                          [1, 0, 1, 2, 1, 2],
                          [1, 1, 2, 1, 1, 1],
                          [1, 2, 0, 1, 0, 2],
                          [1, 2, 0, 2, 2, 2],
                          [0, 1, 0, 2, 1, 0]])
        result = FloodFill.flood_fill(result, 2)
        self.assertEqual(result,
                         [[2, 2, 0, 1, 0, 2],
                          [2, 0, 1, 2, 1, 2],
                          [2, 2, 2, 1, 1, 1],
                          [2, 2, 0, 1, 0, 2],
                          [2, 2, 0, 2, 2, 2],
                          [0, 1, 0, 2, 1, 0]])

    def test_find_best_move(self):
        result = FloodFill.find_best_move(self.image)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
