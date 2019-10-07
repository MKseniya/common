import unittest
import math

from homework import Rectangle

rectangle = Rectangle(1, 2)

class TestRectangle(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        self.assertEqual(Rectangle.get_rectangle_perimeter(rectangle), 6)


    def test_get_rectangle_square(self):
        self.assertEqual(Rectangle.get_rectangle_square(rectangle), 2)


    def test_get_sum_of_corners_number_of_corners(self):
        for num in range(1000):
            expected_num = num
        with self.assertRaises(ValueError):
            Rectangle.get_sum_of_corners(rectangle, expected_num)


    def test_get_sum_of_corners(self):
        for num in range(1, 5):
            sum = num * 90
        self.assertEqual(rectangle.get_sum_of_corners(num), sum)


    def test_get_rectangle_diagonal(self):
        self.assertEqual(int(rectangle.get_rectangle_diagonal()), 2)


    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(int(Rectangle.get_radius_of_circumscribed_circle(rectangle)), 1)

    def test_inscribled_circle_value_error(self):
            with self.assertRaises(ValueError):
                rectangle.get_radius_of_inscribed_circle()

    def test_inscribled_circle_radius(self):
        rectangle1 = Rectangle(1, 1)
        self.assertEqual(rectangle1.get_radius_of_inscribed_circle(), 0.5)

if __name__ == '__main__':
    unittest.main()
