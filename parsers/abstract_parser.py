from abc import ABC, abstractmethod


class AbstractInstructionParser(ABC):
    """
    AbstractInstructionParser is an abstract class which abstract the component
    responsible to translate a str into a list of callable Instructions.
    """
    @abstractmethod
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
        pass
