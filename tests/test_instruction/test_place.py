import unittest
from unittest.mock import patch

from instruction.error.bad_instruction_param_amount import \
    BadInstructionParamAmountError
from instruction.error.bad_instruction_param_type import \
    BadInstructionParamTypeError
from instruction.place import PlaceInstruction
from orientation.direction import Direction
from robotic.robot import Robot


class PlaceTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.place_instruction = PlaceInstruction()
        self.patcher = patch('robotic.robot.Robot.place')
        self.place_patch = self.patcher.start()
        self.place_patch.return_value = None

    def tearDown(self):
        self.patcher.stop()

    def test_good_params(self):
        self.place_instruction.apply(self.robot, 1, 2, 'SOUTH')
        self.place_patch.assert_called_once_with(1, 2, Direction.SOUTH)
        self.place_instruction.apply(self.robot, '2', '4', 'NORTH')
        self.place_patch.assert_called_with(2, 4, Direction.NORTH)

    def test_less_params(self):
        with self.assertRaises(BadInstructionParamAmountError):
            self.place_instruction.apply(self.robot, 1, 2)
        with self.assertRaises(BadInstructionParamAmountError):
            self.place_instruction.apply(self.robot, 1)
        self.assertFalse(self.place_patch.called)

    def test_more_params(self):
        with self.assertRaises(BadInstructionParamAmountError):
            self.place_instruction.apply(self.robot, 1, 2, 'SOUTH', 42)
        self.assertFalse(self.place_patch.called)

    def test_bad_params(self):
        with self.assertRaises(BadInstructionParamTypeError):
            self.place_instruction.apply(self.robot, 'SOUTH', '1', '2')
        with self.assertRaises(BadInstructionParamTypeError):
            self.place_instruction.apply(self.robot, '1', 'SOUTH', '2')
        with self.assertRaises(BadInstructionParamTypeError):
            self.place_instruction.apply(self.robot, '1', '2', 'PLACE')
        self.assertFalse(self.place_patch.called)
