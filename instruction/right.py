from robotic.robot import Robot
from instruction.simple_instruction import SimpleInstruction


class RightInstruction(SimpleInstruction):
    """
    RightInstruction class represents the right instruction. This makes the link
    between the keyword "RIGHT" used as input for the robot and the actual code
    execution on a given robot.
    """

    def __init__(self):
        """
        Initialize a RightInstruction
        """
        super().__init__('RIGHT')

    def apply_function(self, robot: Robot):
        """
        Apply the "RIGHT" instruction to a given robot
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :return: None
        """
        robot.right()
