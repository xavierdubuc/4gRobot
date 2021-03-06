import sys
from io import TextIOBase

from environment.rectangular_environment import RectangularEnvironment
from instruction.instruction import Instruction
from instruction.report import ReportInstruction
from orientation.direction import Direction
from parsers.abstract_parser import AbstractInstructionParser
from robotic.abstract_robot_simulation import AbstractRobotSimulation
from robotic.robot import Robot


class CliRobotSimulation(AbstractRobotSimulation):
    """
    CliRobotSimulation is a class allowing to launch a simulation of a Robot with
    interaction from a user :
    - interactively by using interactive method,
    - programmatically by using exec (or input if passing str)
    - by passing instructions through a file (using method read_from_file)
    """

    def __init__(self, robot: Robot, output: TextIOBase = sys.stdout,
                 verbose=False, stop_interactive_keyword: str = "SHUTDOWN",
                 parser: AbstractInstructionParser = None):
        """
        Create a new RobotSimulation
        :param robot: the robot to use in this simulation
        :type robot: Robot
        :param output: the interface on which the robot and the simulation can
        write (default sys.stdout)
        :type output: TextIOBase
        :param verbose: if the simulation should be verbose or not
        (default False)
        :type verbose: bool
        :param stop_interactive_keyword: the word used to stop the interactive
        mode (default "SHUTDOWN")
        :type stop_interactive_keyword: str
        :param parser: the parser to use in order to understand the input from
        user (default SimpleInstructionParser)
        :type parser: AbstractInstructionParser
        """
        super().__init__(robot, parser, output)
        self.verbose = verbose
        if self.verbose:
            self.border = None
        self.stop_interactive_keyword = stop_interactive_keyword
        self.interactive_prompt = 'Give me an instruction ! ({} to leave)\n'.format(
            self.stop_interactive_keyword)

    def interactive(self):
        """
        Start an interactive session in which the user can input commands in
        real time
        :return: None
        """
        self.output.write('Hello my name is {}, you can control me !\n'.format(
            self.robot.name))
        str_instruction = input(self.interactive_prompt).upper()
        while str_instruction != self.stop_interactive_keyword:
            self.input(str_instruction)
            if not self.verbose:
                self.input('REPORT')
            str_instruction = input(self.interactive_prompt).upper()

    def read_from_file(self, filepath: str):
        """
        Read a file of instruction and executes every instruction found.
        :param filepath: the path to the file to read
        :type filepath: str
        :return: None
        """
        with open(filepath) as file:
            for line in file:
                self.input(line)

    def _handle_bad_param_amount(self, instruction: dict):
        """
        Method called when an instruction is called with a bad amount of
        parameters.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        self.output.write(self.error_messages['bad_params_amount'] + '\n')

    def _handle_bad_param_type(self, instruction: dict):
        """
        Method called when an instruction is called with a parameter of a wrong
        type.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        self.output.write(self.error_messages['bad_param_type'] + '\n')

    def _extra_instruction_handling(self, instruction: dict):
        """
        Method called after an instruction has been handled.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        if self.verbose and not isinstance(instruction['command'],
                                           ReportInstruction):
            self._print_map()

    def _print_map(self):
        """
        Print a map of the environment and the position of the robot.
        :return: None
        """
        if isinstance(self.robot.environment, RectangularEnvironment):
            # first line
            self._print_border()
            # inner lines
            for j in range(self.robot.environment.y_size - 1, -1, -1):
                self.output.write('|')
                for i in range(self.robot.environment.x_size):
                    if self.robot.position == (i, j):
                        self.output.write(self._robot_repr())
                    else:
                        self.output.write('-')
                self.output.write('|')
                self.output.write('\n')
            # last line
            self._print_border()

    def _print_border(self):
        """
        Print a horizontal border (for the map).
        :return: None
        """
        if self.border is None:
            edge = '+'
            elements = [
                edge,
                ''.join(['-'] * self.robot.environment.x_size),
                edge,
                '\n'
            ]
            self.border = ''.join(elements)
        self.output.write(self.border)

    def _robot_repr(self):
        """
        Get a representation of the robot (for the map) in order to indicate to
        which direction he is pointing.
        :return: a char representing the robot and the direction he's looking to
        :rtype: str
        """
        if self.robot.direction == Direction.NORTH:
            return '^'
        if self.robot.direction == Direction.SOUTH:
            return 'v'
        if self.robot.direction == Direction.WEST:
            return '<'
        if self.robot.direction == Direction.EAST:
            return '>'
