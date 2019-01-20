from io import StringIO

from parsers.persistent_parser import PersistentParser
from robotic.abstract_robot_simulation import AbstractRobotSimulation
from robotic.talkative_robot import TalkativeRobot


class ServerRobotSimulation(AbstractRobotSimulation):
    """
    ServerRobotSimulation is a class allowing to launch a simulation of a Robot
    with interaction through an API. It keeps track of more data than the
    CliRobotSimulation.
    """

    def __init__(self, robot: TalkativeRobot):
        """
        Create a new ServerRobotSimulation.
        :param robot: the robot to use in this simulation
        :type robot: TalkativeRobot
        """
        output = StringIO()
        super().__init__(robot, parser=PersistentParser(output=output),
                         output=output)
        self.robot.set_output(output)
        self.errors = []

    def reset(self):
        """
        Reset the simulation. This means resetting the output and the error
        array.
        :return: None
        """
        self.errors = []
        self.output.flush()
        self.output.close()
        self.output = StringIO()
        self.parser.set_output(self.output)
        self.robot.set_output(self.output)

    def _handle_bad_param_amount(self, instruction: dict):
        """
       Method called when an instruction is called with a bad amount of
       parameters. This implementaton add the error in the errors list.
       :param instruction: the called instruction
       :type instruction: dict
       :return: None
       """
        self.errors.append({
            'instruction': instruction['command'].text,
            'error': 'bad_param_amount'
        })

    def _handle_bad_param_type(self, instruction: dict):
        """
        Method called when an instruction is called with a parameter of a wrong
        type. This implementaton add the error in the errors list.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        self.errors.append({
            'instruction': instruction['command'].text,
            'error': 'bad_param_type'
        })

    def _extra_instruction_handling(self, instruction: dict):
        """
        Method called after an instruction has been handled.
        :param instruction: the called instruction
        :type instruction: dict
        :return: None
        """
        pass

    def exec(self, instructions: list):
        self.reset()
        super().exec(instructions)
        for ign_inst in self.parser.ignored_instructions:
            self.errors.append({
                'instruction': ign_inst,
                'error': 'ignored'
            })
