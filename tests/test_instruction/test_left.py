import unittest
from unittest.mock import patch

from instruction.left import LeftInstruction
from robotic.robot import Robot


class LeftTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.left_instruction = LeftInstruction()

    @patch('robotic.robot.Robot.left')
    def test_good_params(self, left_patch):
        left_patch.return_value = None
        self.left_instruction.apply(self.robot)
        left_patch.assert_called_once_with()
