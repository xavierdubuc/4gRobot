import sys
from io import TextIOBase

from instruction.simple_instruction import SimpleInstruction
from robotic.robot import Robot


class ReportInstruction(SimpleInstruction):
    """
    ReportInstruction class represents the report instruction. This makes the
    link between the keyword "REPORT" used as input for the robot and the actual
    code execution on a given robot. The instance variable "report_template" is
    used to determine the way the string to print should be formed.
    """
    report_template = '[{name}, in {position}, facing {direction}]\n'

    def __init__(self, output: TextIOBase = sys.stdout):
        """
        Creates a ReportInstruction.
        :param output: The output interface on which the instruction will write
        the report made by the robot.
        :type output: TextIOBase
        """
        super().__init__('REPORT')
        self.output = output

    def apply_function(self, robot: Robot):
        """
        Apply the "REPORT" instruction to a given robot and print the result on
        self.output.
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :return: None
        """
        report = robot.report()
        if report is not None:
            self.output.write(self.report_template.format(**report))
