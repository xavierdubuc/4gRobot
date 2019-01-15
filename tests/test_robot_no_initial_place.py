import unittest

from orientation.direction import Direction
from robotic.robot import Robot


class InstructionNoInitialPlaceTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_place(self):
        self.robot.place(0, 0, Direction.NORTH)
        self.assertEqual(self.robot.position, (0, 0))
        self.assertEqual(self.robot.direction, Direction.NORTH)

    def test_right(self):
        self.robot.right()
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.direction)

    def test_left(self):
        self.robot.left()
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.direction)

    def test_move(self):
        self.robot.move()
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.direction)

    def test_report(self):
        self.assertIsNone(self.robot.report())
