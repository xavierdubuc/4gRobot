import unittest
from unittest.mock import patch

from instruction.report import ReportInstruction
from orientation.direction import Direction
from robotic.robot import Robot


class ReportTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.robot.place(1, 2, Direction.SOUTH)
        self.report_instruction = ReportInstruction()

    @patch('robotic.robot.Robot.report')
    def test_good_params(self, report_patch):
        report_patch.return_value = {'name': "Test", 'position': (1, 2),
                                     'direction': Direction.SOUTH}
        self.report_instruction.apply(self.robot)
        report_patch.assert_called_once_with()
