import unittest
import electric_field


class TestEEF(unittest.TestCase):

    def test_no_dx(self):
        result = electric_field.get_components(dx=0, dy=2, mag=3)
        self.assertEqual((0, 3), result)

    def test_no_dy(self):
        result = electric_field.get_components(dx=2, dy=0, mag=3)
        self.assertEqual((3, 0), result)

    def test_neg_dx1(self):
        result = electric_field.get_components(dx=-2, dy=0, mag=3)
        self.assertEqual((-3, 0), result)

    def test_neg_dx2(self):
        result = electric_field.get_components(dx=-3, dy=4, mag=5)
        self.assertEqual((-3, 4), result)
