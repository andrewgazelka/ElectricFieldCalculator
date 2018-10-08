import unittest

import mathutils


class TestMathUtils(unittest.TestCase):

    def test_sqrt_square(self):
        self.assertAlmostEqual(10, mathutils.sqrt(100))

    def test_sqrt_normal(self):
        self.assertAlmostEqual(87.1235, mathutils.sqrt(87.1235 * 87.1235))

    def test_sqrt_small(self):
        self.assertAlmostEqual(0.00213, mathutils.sqrt(0.00213 * 0.00213))
