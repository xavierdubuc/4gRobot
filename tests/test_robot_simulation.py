import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from instruction.error.bad_instruction_param_amount import \
    BadInstructionParamAmountError
from instruction.error.bad_instruction_param_type import \
    BadInstructionParamTypeError
from instruction.left import LeftInstruction
from instruction.place import PlaceInstruction
from orientation.direction import Direction
from robotic.robot import Robot
from robotic.robot_simulation import RobotSimulation


class RobotSimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.robot_simulation = RobotSimulation(self.robot)

    @patch('builtins.input', side_effect=['PLACE 0,0,NORTH', 'SHUTDOWN'])
    def test_interactive(self, mock):
        self.robot_simulation.interactive()
        self.assertEqual(self.robot.position, (0, 0))
        self.assertEqual(self.robot.direction, Direction.NORTH)

    @patch('parsers.simple_parser.SimpleInstructionParser.parse_str')
    @patch('robotic.robot_simulation.RobotSimulation.exec', return_value=None)
    def test_input(self, mock_exec, mock_parse_str):
        mock_parse_str.return_value = [
            {
                'command': PlaceInstruction(),
                'args': ['0', '0', 'NORTH']
            },
            {
                'command': LeftInstruction(),
                'args': []
            }
        ]
        self.robot_simulation.input('whatever')
        mock_exec.assert_called_once_with(mock_parse_str.return_value)

    @patch('instruction.place.PlaceInstruction.apply',
           side_effect=BadInstructionParamAmountError)
    @patch('sys.stdout', new_callable=StringIO)
    def test_exec_bad_param_amount(self, sys_mock, apply_mock):
        in_data = [{'command': PlaceInstruction(), 'args': []}]
        self.robot_simulation.output = sys_mock
        self.robot_simulation.exec(in_data)
        self.assertEqual(sys_mock.getvalue(),
                         self.robot_simulation.error_messages[
                             'bad_params_amount'] + '\n')

    @patch('instruction.place.PlaceInstruction.apply',
           side_effect=BadInstructionParamTypeError)
    @patch('sys.stdout', new_callable=StringIO)
    def test_exec_bad_param_type(self, sys_mock, apply_mock):
        in_data = [{'command': PlaceInstruction(), 'args': []}]
        self.robot_simulation.output = sys_mock
        self.robot_simulation.exec(in_data)
        self.assertEqual(sys_mock.getvalue(),
                         self.robot_simulation.error_messages[
                             'bad_param_type'] + '\n')

    def test_read_file(self):
        filename = 'bluh'
        test_data = 'PLACE 0,0,NORTH\nRIGHT'
        m = unittest.mock.mock_open(read_data=''.join(test_data))
        m.return_value.__iter__ = lambda x: x
        m.return_value.__next__ = lambda x: next(iter(x.readline, ''))
        with patch('builtins.open', m):
            self.robot_simulation.read_from_file(filename)
            self.assertEqual(self.robot.position, (0, 0))
            self.assertEqual(self.robot.direction, Direction.EAST)
            m.assert_called_once_with(filename)

    def test_print_border(self):
        spec_robot_simulation = RobotSimulation(self.robot, verbose=True,
                                                output=MagicMock())
        self.assertTrue(hasattr(spec_robot_simulation, 'border'))
        self.assertIsNone(spec_robot_simulation.border)
        spec_robot_simulation._print_border()
        self.assertIsNotNone(spec_robot_simulation.border)
        firstly_generated = spec_robot_simulation.border
        self.assertEqual(spec_robot_simulation.border[0], '+')
        self.assertEqual(spec_robot_simulation.border[-2:], '+\n')
        self.assertEqual(spec_robot_simulation.border.strip('+\n'),
                         '-' * spec_robot_simulation.robot.environment.x_size)
        spec_robot_simulation._print_border()
        self.assertIs(firstly_generated, spec_robot_simulation.border)

    def test_robot_repr(self):
        tests = {
            Direction.NORTH: '^',
            Direction.WEST: '<',
            Direction.EAST: '>',
            Direction.SOUTH: 'v'
        }
        for direction, char in tests.items():
            self.robot.direction = direction
            self.assertEqual(self.robot_simulation._robot_repr(), char)

    def test_print_map(self):
        mock = StringIO()
        robot_simulation = RobotSimulation(self.robot, verbose=True,
                                           output=mock)
        position = (0, 0)
        direction = Direction.NORTH
        self.robot.place(*position, direction)
        robot_simulation._print_map()
        map_elements = mock.getvalue().strip().split('\n')
        map_borders = map_elements[0:1] + map_elements[-1:]

        # BORDERS
        for map_border in map_borders:
            print(map_border)
            self.assertEqual(map_border[0], '+')
            self.assertEqual(map_border[-1], '+')
            for char in map_border[1:-1]:
                self.assertEqual(char, '-')

        # LINES & ROBOT
        map_lines = map_elements[1:-1]
        for i, map_line in enumerate(reversed(map_lines)):
            self.assertEqual(map_line[0], '|')
            self.assertEqual(map_line[-1], '|')
            for j, char in enumerate(map_line[1:-1]):
                if self.robot.position == (i, j):
                    self.assertNotEqual(char, '-')
                else:
                    self.assertEqual(char, '-')
