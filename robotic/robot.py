from operator import add

from environment.environment import Environment
from environment.square_environment import SquareEnvironment
from orientation.direction import Direction
from orientation.compass import Compass


class Robot:
    """
    Class representing a simple Robot that can be placed in a environment. The
    robot can then move, turn right, turn left and report its current parameters
    when asked. The robot is "clever" as he will not execute any move that could
    make him fall off its given environment. Also the robot needs to be placed
    in the environment before to execute any command so make sure the first
    command you ask him is a "PLACE".

    The environment is composed of tiles identified by coordinates
    ( (0,0), (0,1), ... ).
    """

    def __init__(self, name: str = "Alice", environment: Environment = None):
        """
        Create a Robot
        :param name: the name of the robot (default Alice)
        :type name: str
        :param environment: the environment in which the Robot will navigate
        (default Squared environment 5x5)
        :type environment: Environment
        """
        self.name = name
        self.environment = SquareEnvironment(
            5) if environment is None else environment
        self.position = None
        self.direction = None

    def reset(self):
        """
        Reset the robot. It acts like it is removed from the environment and
        thus has no position and no direction.
        :return:
        """
        self.position = None
        self.direction = None

    def place(self, x: int, y: int, direction: Direction):
        """
        Place the robot on a tile of the environment. If the given coordinates
        are not on the environment the robot will ignore the instruction and
        call _prevent_fall() method.
        :param x: the x coordinate of the targeted tile,
        :type x: int
        :param y: the y coordinate of the targeted tile,
        :type y: int
        :param direction: the direction to which to robot should be facing to
        once placed
        :type direction: Direction
        :return: None
        """
        potential_position = (x, y)
        if self.environment.is_tile(potential_position):
            self.position = potential_position
            self.direction = direction
        else:
            self._prevent_fall()

    def move(self):
        """
        Move the robot forward. If the position he is moving to is outside the
        environment he will ignore the instruction and call _prevent_fall()
        method. Also, if the robot is not yet placed, the instruction will be
        ignored and method _not_placed() will be called instead.
        :return: None
        """
        if self._should_handle_instruction('move'):
            position_to_go = self._compute_next_position()
            if self.environment.is_reachable(self.position, position_to_go):
                self.position = position_to_go
            else:
                self._prevent_fall()

    def right(self):
        """
        Rotate the robot 90° on the right. If the robot is not yet placed, the
        instruction will be ignored and method _not_placed() will be called
        instead.
        :return: None
        """
        if self._should_handle_instruction('right'):
            self.direction = Compass.right(self.direction)

    def left(self):
        """
        Rotate the robot 90° on the left. If the robot is not yet placed, the
        instruction will be ignored and method _not_placed() will be called
        instead.
        :return: None
        """
        if self._should_handle_instruction('left'):
            self.direction = Compass.left(self.direction)

    def report(self):
        """
        Get a report of the current parameters of the robot. If the robot is not
        yet placed, the instruction will be ignored and method _not_placed()
        will be called instead.
        :return: a dict composed like this :
            - 'name' : the name of the robot
            - 'position': the tuple representing the position of the robot in the
            environment
            - 'direction': the direction to which the robot is facing
        :rtype: dict
        """
        if self._should_handle_instruction('report'):
            return {'name': self.name, 'position': self.position,
                    'direction': self.direction}

    def _prevent_fall(self):
        """
        Method called when an instruction that would make the robot fall is
        attempted.
        Nothing is done here, could be overridden if needed.
        :return: None
        """
        print("I'll just pretend you did not ask me this.")

    def _not_placed(self):
        """
        Method called when an instruction is attempted before the robot has been
        placed in its environment.
        Nothing is done here, could be overridden if needed.
        :return: None
        """
        pass

    def _should_handle_instruction(self, instruction: str):
        """
        Check if the given instruction has to be handled by the robot.
        Basically it checks that the robot is placed and if it's not, it calls
        _not_placed() method.
        :param instruction: the attempted instruction
        :type instruction: str
        :return: True is the instruction have to be handled, False otherwise.
        :rtype: bool
        """
        if not self._is_placed():
            self._not_placed()
            return False
        return True

    def _is_placed(self):
        """
        Determine if the robot is placed or not
        :return: True if the robot is placed, False otherwise
        :rtype: bool
        """
        return self.position is not None and self.direction is not None

    def _compute_next_position(self):
        """
        Compute the asked position if the robot has to move with its current
        parameters. It uses the vector of the direction and its current position
        to compute what should be the next position.
        :return: the coordinates of the new position of the robot.
        :rtype: tuple
        """
        return tuple(map(add, self.position, self.direction.value))
