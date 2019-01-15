from abc import ABC, abstractmethod

from robotic.robot import Robot
from instruction.error.bad_instruction_param_amount import BadInstructionParamAmountError
from instruction.instruction import Instruction


class SimpleInstruction(Instruction, ABC):
    """
    SimpleInstruction is an abstract class representing an Instruction which
    does not allow any parameter.
    """

    def apply(self, robot: Robot, *args):
        """
        Check that no parameters is given and apply the instruction to the given
        robot.
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :param args: the arguments to the instruction (should be empty)
        :raise BadInstructionParamAmountError: when args is not empty
        :return: None
        """
        if args is not None and len(args) > 0:
            raise BadInstructionParamAmountError(
                'Instruction is malformed (no arguments allowed) !')
        self.apply_function(robot)

    @abstractmethod
    def apply_function(self, robot: Robot):
        """
        Apply the instruction to a given robot
        :param robot: the robot on which the instruction should be executed
        :type robot: Robot
        :return: None
        """
        pass
