import unittest
from unittest.mock import patch

from instruction.right import RightInstruction
from robotic.robot import Robot


class RightTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.right_instruction = RightInstruction()

    @patch('robotic.robot.Robot.right')
    def test_good_params(self, right_patch):
        right_patch.return_value = None
        self.right_instruction.apply(self.robot)
        right_patch.assert_called_once_with()
