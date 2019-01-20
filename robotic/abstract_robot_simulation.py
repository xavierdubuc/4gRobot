import sys
from abc import ABC, abstractmethod
from io import TextIOBase

from instruction.error.bad_instruction_param_amount import \
    BadInstructionParamAmountError
from instruction.error.bad_instruction_param_type import \
    BadInstructionParamTypeError
from parsers.abstract_parser import AbstractInstructionParser
from parsers.simple_parser import SimpleInstructionParser
from robotic.robot import Robot


class AbstractRobotSimulation(ABC):
    """
    RobotSimulation is a class allowing to launch a simulation of a Robot with
    interaction from a user :
    - interactively by using interactive method,
    - programmatically by using exec (or input if passing str)
    - by passing instructions through a file (using method read_from_file)
    """

    error_messages = {
        'bad_params_amount': 'ERROR: Too much or too few parameters',
        'bad_param_type': 'ERROR: Bad parameter type'
    }

    def __init__(self, robot: Robot, parser: AbstractInstructionParser = None,
                 output: TextIOBase = sys.stdout):
        """
        Create a new RobotSimulation
        :param robot: the robot to use in this simulation
        :type robot: Robot
        :param parser: the parser to use in order to understand the input from
        user (default SimpleInstructionParser)
        :type parser: AbstractInstructionParser
        :param output: the interface on which the robot and the simulation can
        write (default sys.stdout)
        :type output: TextIOBase
        """
        self.robot = robot
        self.output = output
        self.parser = parser if parser is not None else SimpleInstructionParser(
            output=self.output)

    def input(self, iinput: str):
        """
        Input a string in the parser. The string can contain one or multiple
        instructions for the robot. The parser parses it and executes what
        should be
        :param iinput: The input to parse.
        :type iinput: str
        :return: None
        """
        instructions = self.parser.parse_str(iinput)
        self.exec(instructions)

    def exec(self, instructions: list):
        """
        Execute a list of instruction.
        :param instructions: A list of dict objects build like that:
        - 'command': the instruction object to be executed
        - 'args': the arguments the instruction object need to fulfill its
        execution
        :type instructions: list
        :return: None
        """
        for instruction in instructions:
            try:
                instruction['command'].apply(self.robot, *instruction['args'])
            except BadInstructionParamAmountError:
                self._handle_bad_param_amount(instruction)
            except BadInstructionParamTypeError:
                self._handle_bad_param_type(instruction)
            self._extra_instruction_handling(instruction)

    @abstractmethod
    def _handle_bad_param_amount(self, instruction: dict):
        """
        Method called when an instruction is called with a bad amount of
        parameters.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        pass

    @abstractmethod
    def _handle_bad_param_type(self, instruction: dict):
        """
        Method called when an instruction is called with a parameter of a wrong
        type.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        pass

    @abstractmethod
    def _extra_instruction_handling(self, instruction: dict):
        """
        Method called after an instruction has been handled.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        pass
