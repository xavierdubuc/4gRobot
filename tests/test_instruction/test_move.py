import unittest
from unittest.mock import patch

from instruction.move import MoveInstruction
from robotic.robot import Robot


class MoveTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.move_instruction = MoveInstruction()

    @patch('robotic.robot.Robot.move')
    def test_good_params(self, move_patch):
        move_patch.return_value = None
        self.move_instruction.apply(self.robot)
        move_patch.assert_called_once_with()
