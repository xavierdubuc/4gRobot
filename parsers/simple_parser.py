import sys
from io import TextIOBase

from instruction.left import LeftInstruction
from instruction.move import MoveInstruction
from instruction.place import PlaceInstruction
from instruction.report import ReportInstruction
from instruction.right import RightInstruction
from parsers.abstract_parser import AbstractInstructionParser


class SimpleInstructionParser(AbstractInstructionParser):
    """
    SimpleInstructionParser is a basic parser that naively parse a string
    containing one or more instructions for a robot. It supports all
    instructions defined in instructions dict variable where the key should be
    the text of the instruction. It uses this key to determine which instruction
    he found.

    The parsing is based on simple (and configurable) separators used to split
    the input.
    """

    def __init__(self, instructions_separator: str = '\n',
                 arguments_separator: str = ',',
                 command_arg_separator: str = ' ',
                 output: TextIOBase = sys.stdout):
        """
        Create a SimpleInstructionParser with given separators.
        :param instructions_separator: the separator used between instructions
        (default '\n')
        :type instructions_separator: str
        :param arguments_separator: the separator used between instruction
        arguments (default ',')
        :type arguments_separator: str
        :param command_arg_separator: the separator used between instruction and
        its arguments (default ' ')
        :type command_arg_separator: str
        :param output: the output on which the instructions can write their
        information
        :type output: TextIOBase
        """
        self.separators = {
            'instructions': instructions_separator,
            'arguments': arguments_separator,
            'command_args': command_arg_separator
        }
        self.instructions = {
            'PLACE': PlaceInstruction(),
            'MOVE': MoveInstruction(),
            'LEFT': LeftInstruction(),
            'RIGHT': RightInstruction(),
            'REPORT': ReportInstruction(output=output)
        }

    def parse_str(self, text: str):
        """
        Parse a given "program" containing a bunch of instructions for the robot
        and retrieve the right Instruction objects ready to be executed and the
        corresponding arguments.
        :param text: the "program" to parse
        :type text: str
        :return: the list of recognized instruction, it ignores unsupported
        instructions and call instruction_not_supported method instead of adding
        it in the list.
        :rtype: list of dict {Instruction, list of str}
        """
        instructions = []
        str_instructions = self._parse_instructions(text.upper())
        for str_instruction in str_instructions:
            command, args = self._parse_command_args(str_instruction)
            if command is None:
                self.instruction_not_supported(str_instruction)
            else:
                instructions.append({'command': command, 'args': args})
        return instructions

    def _parse_instructions(self, instructions: str):
        """
        Parse a given "program" containing a bunch of instructions for the robot
        and make a list of instructions still encoded as str.
        :param instructions: the "program" to parse
        :type instructions: str
        :return: a list of string encoded instructions
        :rtype: list of str
        """
        return instructions.strip().split(self.separators['instructions'])

    def _parse_command_args(self, instruction: str):
        """
        Parse a given string encoded instruction to get the Instruction object
        to call and its parameters.
        :param instruction: the string encoded instruction
        :type instruction: str
        :return: the instruction object to call (or None) and a list containing
        the parsed arguments
        :rtype: tuple
        """
        parts = instruction.strip().split(self.separators['command_args'],
                                          maxsplit=1)
        args = self._parse_arguments(parts[1]) if len(parts) > 1 else []
        return self._get_instruction(parts[0]), args

    def _parse_arguments(self, arguments: str):
        """
        Parse string encoded arguments to get them as list.
        :param arguments: the string encode arguments
        :type arguments: str
        :return: the arguments parsed in a list
        :rtype: list of str
        """
        return list(
            map(str.strip, arguments.split(self.separators['arguments'])))

    def _get_instruction(self, instruction: str):
        """
        Get a given instruction based on its text representation.
        :param instruction: the string encode instruction
        :type instruction: str
        :return: the found instruction or None if no instruction found
        :rtype: Instruction or None
        """
        return self.instructions.get(instruction)

    def instruction_not_supported(self, str_instruction: str):
        """
        This method is called when an instruction is not supported.
        :param str_instruction: the not supported instruction that triggers
        this method call
        :type str_instruction: str
        :return: None
        """
        print('"{}" instruction is not supported'.format(str_instruction))
