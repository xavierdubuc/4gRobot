from robotic.robot import Robot
from instruction.simple_instruction import SimpleInstruction


class LeftInstruction(SimpleInstruction):
    """
    LeftInstruction class represents the left instruction. This makes the link
    between the keyword "LEFT" used as input for the robot and the actual code
    execution on a given robot.
    """

    def __init__(self):
        """
        Initialize a LeftInstruction
        """
        super().__init__('LEFT')

    def apply_function(self, robot: Robot):
        """
        Apply the "LEFT" instruction to a given robot
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :return: None
        """
        robot.left()
