import argparse

from environment.rectangular_environment import RectangularEnvironment
from robotic.robot import Robot
from robotic.cli_robot_simulation import CliRobotSimulation


class Command:
    """
    Simple class used to represent an executed command from terminal.
    """
    def __init__(self):
        """
        Create a new Command
        """
        self.parser = argparse.ArgumentParser()

        # MODES
        self.parser.add_argument('--execute', '-x', nargs="*", required=False,
                                 help="the instructions to execute")
        self.parser.add_argument('--interactive', '-i', nargs="?",
                                 default=False, const=True, type=bool,
                                 help="interactive mode")
        self.parser.add_argument('--file', '-f',
                                 help='a file containing instructions to read')

        # PARAMS
        self.parser.add_argument('--x-size', default=5, type=int,
                                 help='the size (x) of the environment')
        self.parser.add_argument('--y-size', type=int,
                                 help='''the size (y) of the environment
                                 (default to x size)''')
        self.parser.add_argument('--verbose', '-v', type=bool, nargs="?",
                                 help='''verbose mode (including a beautiful 
                                 map !)''', default=False, const=True)
        self.parser.add_argument('--name', help='the name of the robot',
                                 nargs="?", default=None, const=None)

    def run(self):
        """
        Run the command
        :return: None
        """
        args = self.parser.parse_args()
        x_size = args.x_size
        y_size = args.y_size if args.y_size is not None else args.x_size
        robot_params = {
            'environment': RectangularEnvironment(x_size=x_size, y_size=y_size)
        }
        if args.name is not None:
            robot_params['name'] = args.name
        robot = Robot(**robot_params)
        verbose = args.verbose
        simulator = CliRobotSimulation(robot, verbose=verbose)

        # STANDARD INPUT
        if args.execute is not None and len(args.execute) > 0:
            for arg in args.execute:
                simulator.input(arg)
        # FILE READING
        elif args.file is not None:
            simulator.read_from_file(args.file)
        elif args.interactive:
            simulator.interactive()
        else:
            print('Please provide at least -i , -f or -x option')


if __name__ == '__main__':
    Command().run()
