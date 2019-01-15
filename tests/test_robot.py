import unittest
from unittest.mock import patch

from orientation.compass import Compass
from orientation.direction import Direction
from robotic.robot import Robot


class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot('Test')
        self.initial_x = 0
        self.initial_y = 0
        self.initial_dir = Direction.NORTH
        self.robot.place(self.initial_x, self.initial_y, self.initial_dir)

    def test_place(self):
        self.robot.place(1, 2, Direction.SOUTH)
        self.assertEqual(self.robot.position, (1, 2))
        self.assertEqual(self.robot.direction, Direction.SOUTH)

    def test_right(self):
        self.robot.right()
        self.assertEqual(self.robot.position, (self.initial_x, self.initial_y))
        self.assertEqual(self.robot.direction, Compass.right(self.initial_dir))

    def test_left(self):
        self.robot.left()
        self.assertEqual(self.robot.position, (self.initial_x, self.initial_y))
        self.assertEqual(self.robot.direction, Compass.left(self.initial_dir))

    def test_move_y(self):
        self.robot.move()
        self.assertEqual(self.robot.position,
                         (self.initial_x, self.initial_y + 1))
        self.assertEqual(self.robot.direction, self.initial_dir)

    def test_move_x(self):
        self.robot.right()
        self.robot.move()
        self.assertEqual(self.robot.position,
                         (self.initial_x + 1, self.initial_y))
        self.assertEqual(self.robot.direction, Compass.right(self.initial_dir))

    def test_report(self):
        expected = {
            'name': 'Test',
            'position': (0, 0),
            'direction': Direction.NORTH
        }
        self.assertDictEqual(self.robot.report(), expected)

    @patch('robotic.robot.Robot._prevent_fall')
    def test_move_outside_environment(self, prevent_fall_mock):
        self.robot.left()
        self.robot.move()
        self.assertEqual(self.robot.position, (self.initial_x, self.initial_y))
        prevent_fall_mock.assert_called_once_with()

    @patch('robotic.robot.Robot._prevent_fall')
    def test_place_outside_environment(self, prevent_fall_mock):
        self.robot.place(1000, 1000, Direction.SOUTH)
        self.assertEqual(self.robot.position, (self.initial_x, self.initial_y))
        self.assertEqual(self.robot.direction, self.initial_dir)
        prevent_fall_mock.assert_called_once_with()
