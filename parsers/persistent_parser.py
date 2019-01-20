import sys
from io import TextIOBase

from parsers.simple_parser import SimpleInstructionParser


class PersistentParser(SimpleInstructionParser):
    """
    PersistentParser do exactly the same job as SimpleInstructionParser but it
    keeps a trace of ignored instructions.
    """

    def __init__(self, instructions_separator: str = '\n',
                 arguments_separator: str = ',',
                 command_arg_separator: str = ' ',
                 output: TextIOBase = sys.stdout):
        """
        Create a PersistentParser with given separators.
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
        super().__init__(instructions_separator, arguments_separator,
                         command_arg_separator, output)
        self.ignored_instructions = []

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
        self.ignored_instructions = []
        return super().parse_str(text)

    def instruction_not_supported(self, str_instruction: str):
        """
        This method is called when an instruction is not supported.
        :param str_instruction: the not supported instruction that triggers
        this method call
        :type str_instruction: str
        :return: None
        """
        self.ignored_instructions.append(str_instruction)
