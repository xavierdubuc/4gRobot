import unittest
from unittest.mock import patch, Mock

from instruction.instruction import Instruction
from instruction.left import LeftInstruction
from instruction.move import MoveInstruction
from instruction.place import PlaceInstruction
from instruction.report import ReportInstruction
from instruction.right import RightInstruction
from parsers.simple_parser import SimpleInstructionParser


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = SimpleInstructionParser()

    @patch('parsers.simple_parser.SimpleInstructionParser._parse_instructions',
           Mock(return_value=[
               'PLACE 0, 0, NORTH',
               'REPORT',
               'MOVE',
               'REPORT',
               'LEFT',
               'REPORT',
               'RIGHT',
               'REPORT'
           ]))
    @patch('parsers.simple_parser.SimpleInstructionParser._parse_command_args',
           Mock(return_value=(PlaceInstruction(), ['0', '0', 'NORTH'])))
    def test_parse_str(self):
        instructions = self.parser.parse_str('')
        self.assertIsNotNone(instructions)
        self.assertEqual(len(instructions), 8)
        for instruction in instructions:
            self.assertIsInstance(instruction, dict)
            command = instruction.get('command')
            args = instruction.get('args')
            self.assertIsNotNone(command)
            self.assertIsNotNone(args)
            self.assertIsInstance(command, Instruction)
            self.assertIsInstance(args, list)

    @patch('parsers.simple_parser.SimpleInstructionParser._parse_instructions',
           Mock(return_value=['JUMP']))
    @patch('parsers.simple_parser.SimpleInstructionParser._parse_command_args',
           Mock(return_value=(None, [])))
    @patch(
        'parsers.simple_parser.SimpleInstructionParser.instruction_not_supported')
    def test_parse_str_unknown(self, inst_not_supported_mock):
        inst_not_supported_mock.return_value = None
        str = 'JUMP'
        instructions = self.parser.parse_str(str)
        self.assertEqual(len(instructions), 0)
        inst_not_supported_mock.assert_called_once_with(str)

    def test_parse_instructions(self):
        str = '''
            PLACE 0,0,NORTH
            REPORT
            MOVE
            REPORT
            LEFT
            REPORT
            RIGHT
            REPORT
        '''
        instructions = self.parser._parse_instructions(str)
        self.assertIsNotNone(instructions)
        self.assertEqual(len(instructions), 8)

    def test_parse_instructions_unique(self):
        str = 'PLACE 0,0,NORTH'
        instructions = self.parser._parse_instructions(str)
        self.assertIsNotNone(instructions)
        self.assertEqual(len(instructions), 1)

    @patch('parsers.simple_parser.SimpleInstructionParser._parse_arguments',
           Mock(return_value=['0', '0', 'NORTH']))
    @patch('parsers.simple_parser.SimpleInstructionParser._get_instruction',
           Mock(return_value=PlaceInstruction()))
    def test_parse_command_args_with_args(self):
        inst = 'PLACE 0,0,NORTH'
        instruction, args = self.parser._parse_command_args(inst)
        self.assertIsInstance(instruction, PlaceInstruction)
        self.assertIsInstance(args, list)
        self.assertEqual(len(args), 3)
        self.assertEqual(args, ['0', '0', 'NORTH'])

    @patch('parsers.simple_parser.SimpleInstructionParser._parse_arguments',
           Mock(return_value=["blah"]))
    @patch('parsers.simple_parser.SimpleInstructionParser._get_instruction',
           Mock(return_value=ReportInstruction()))
    def test_parse_command_args_without_args(self):
        insts = ['REPORT', ' REPORT', ' report', ' REPORT']
        for inst in insts:
            out = self.parser._parse_command_args(inst)
            self.assertEqual(len(out), 2)
            self.assertIsInstance(out[0], ReportInstruction)
            self.assertIsInstance(out[1], list)

    def test_parse_arguments(self):
        args_strs = ['0,0,NORTH', '0,0, NORTH', '0, 0,NORTH', '0,0,NORTH ',
                     '0 ,0,NORTH']
        for args_str in args_strs:
            args = self.parser._parse_arguments(args_str)
            self.assertIsInstance(args, list)
            self.assertEqual(len(args), 3)
            self.assertEqual(args, ['0', '0', 'NORTH'])

    def test_get_instruction(self):
        commands = {
            'PLACE': PlaceInstruction,
            'MOVE': MoveInstruction,
            'LEFT': LeftInstruction,
            'RIGHT': RightInstruction,
            'REPORT': ReportInstruction
        }
        for command, instruction in commands.items():
            x = self.parser._get_instruction(command)
            self.assertIsNotNone(x)
            self.assertIsInstance(x, instruction)
        self.assertIsNone(self.parser._get_instruction('JUMP'))
