import unittest
from unittest.mock import patch

from instruction.error.bad_instruction_param_amount import \
    BadInstructionParamAmountError
from instruction.simple_instruction import SimpleInstruction
from robotic.robot import Robot


class SimpleInstructionTestCase(unittest.TestCase):

    @patch.multiple(SimpleInstruction, __abstractmethods__=set())
    def setUp(self):
        self.robot = Robot()
        self.simple_instruction = SimpleInstruction("TEST")

    @patch(
        'instruction.simple_instruction.SimpleInstruction.apply_function')
    def test_more_params(self, mock):
        with self.assertRaises(BadInstructionParamAmountError):
            self.simple_instruction.apply(self.robot, 1)
        with self.assertRaises(BadInstructionParamAmountError):
            self.simple_instruction.apply(self.robot, "NORTH")
        self.assertFalse(mock.called)
