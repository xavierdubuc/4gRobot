import unittest

from orientation.compass import Compass
from orientation.direction import Direction


class CompassTestCase(unittest.TestCase):
    def test_right(self):
        direction = Direction.NORTH
        direction = Compass.right(direction)
        self.assertEqual(direction, Direction.EAST)
        direction = Compass.right(direction)
        self.assertEqual(direction, Direction.SOUTH)
        direction = Compass.right(direction)
        self.assertEqual(direction, Direction.WEST)
        direction = Compass.right(direction)
        self.assertEqual(direction, Direction.NORTH)

    def test_left(self):
        direction = Direction.NORTH
        direction = Compass.left(direction)
        self.assertEqual(direction, Direction.WEST)
        direction = Compass.left(direction)
        self.assertEqual(direction, Direction.SOUTH)
        direction = Compass.left(direction)
        self.assertEqual(direction, Direction.EAST)
        direction = Compass.left(direction)
        self.assertEqual(direction, Direction.NORTH)
