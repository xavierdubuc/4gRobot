import sys

from environment.environment import Environment
from robotic.robot import Robot


class TalkativeRobot(Robot):
    """
    TalkativeRobot extends the Robot class by allowing the use of an output in
    order to get feedback even when commands are ignored.
    """

    def __init__(self, name: str = "Alice", environment: Environment = None,
                 output=sys.stdout):
        """
        Create a Robot
        :param name: the name of the robot (default Alice)
        :type name: str
        :param environment: the environment in which the Robot will navigate
        (default Squared environment 5x5)
        :type environment: Environment
        """
        super().__init__(name, environment)
        self.output = output


    def set_output(self, output):
        """
        Set the output used by this talkative robot.
        :param output: the output to use from now on
        :type output: TextIOBase
        :return: None
        """
        self.output = output

    def _prevent_fall(self):
        """
        Method called when an instruction that would make the robot fall is
        attempted.
        Nothing is done here, could be overridden if needed.
        :return: None
        """
        self.output.write(
            "I'll just pretend you did not ask me this, I don't want to fall !")

    def _not_placed(self):
        """
        Method called when an instruction is attempted before the robot has been
        placed in its environment.
        Nothing is done here, could be overridden if needed.
        :return: None
        """
        self.output.write("Pssst! Place me before asking me anything else !")
