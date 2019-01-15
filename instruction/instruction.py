from abc import ABC, abstractmethod

from robotic.robot import Robot


class Instruction(ABC):
    """
    An Instruction represent a command that can be asked to the robot. It is
    composed by a function to act on the robot and a text representing the
    command in string. This text is used to parse incoming text commands.
    """

    def __init__(self, text):
        """
        Create an Instruction
        :param text: the text representation of the command
        """
        self.text = text

    @abstractmethod
    def apply(self, robot: Robot, *args):
        """
        Apply the function corresponding to the command to a given robot.
        :param robot: the robot on which to the command should be executed
        :type robot: Robot
        :param args: the needed arguments of the function (default empty)
        :return: None
        """
        pass
