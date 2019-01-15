from orientation.direction import Direction
from robotic.robot import Robot
from instruction.error.bad_instruction_param_amount import BadInstructionParamAmountError
from instruction.error.bad_instruction_param_type import BadInstructionParamTypeError
from instruction.instruction import Instruction


class PlaceInstruction(Instruction):
    """
    PlaceInstruction class represents the left instruction. This makes the
    link between the keyword "PLACE" used as input for the robot and the
    actual code execution on a given robot.
    """

    def __init__(self):
        """
        Initialize a PlaceInstruction
        """
        super().__init__('PLACE')

    def apply(self, robot: Robot, *args):
        """
        Apply the "PLACE" instruction to a given robot
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :param args: the arguments needed by the place instruction in the right
        order :
        - the x coordinate of the position (int or str)
        - the y coordinate of the position (int or str),
        - the direction to which the robot should look at (a string which must
        one these : "WEST", "NORTH", "EAST" or "SOUTH")
        :raise BadInstructionParamAmountError: when args does not contain
        exactly 3 arguments
        :raise BadInstructionParamTypeError: when one of the 3 given arguments
        in args is not in the right type
        :return: None
        """
        if len(args) == 3:
            if isinstance(args[0], str) and not args[0].isdigit():
                raise BadInstructionParamTypeError(
                    'X-axis coordinate should be an integer')
            if isinstance(args[0], str) and not args[1].isdigit():
                raise BadInstructionParamTypeError(
                    'Y-axis coordinate should be an integer')
            if not args[2] in Direction.__members__:
                content = '''Direction should be a cardinal point 
                            (received "{}")'''.format(args[2])
                raise BadInstructionParamTypeError(content)
            sub_args = (int(args[0]), int(args[1]),
                        args[2] if isinstance(args[2], Direction) else
                        Direction[args[2]])
            robot.place(*sub_args)
        else:
            raise BadInstructionParamAmountError(
                'Instruction is malformed (exactly 3 arguments are allowed) !')
