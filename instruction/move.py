from robotic.robot import Robot
from instruction.simple_instruction import SimpleInstruction


class MoveInstruction(SimpleInstruction):
    """
        MoveInstruction class represents the move instruction. This makes the
        link between the keyword "MOVE" used as input for the robot and the
        actual code execution on a given robot.
        """

    def __init__(self):
        """
        Initialize a MoveInstruction
        """
        super().__init__('MOVE')

    def apply_function(self, robot: Robot):
        """
        Apply the "MOVE" instruction to a given robot
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :return: None
        """
        robot.move()
