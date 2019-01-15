from environment.rectangular_environment import RectangularEnvironment


class SquareEnvironment(RectangularEnvironment):
    """
    SquareEnvironment is a class allowing to define a squared environment in
    which something or someone can move.
    """

    def __init__(self, size, lowest_x=0, lowest_y=0):
        """
        Create a SquareEnvironment
        :param size: the size of the square
        :type size: int
        :param lowest_x: the lowest coordinate of the square on x axis
        (default 0)
        :type lowest_x: int
        :param lowest_y: the lowest coordinate of the square on y axis
        :type lowest_y: int
        (default 0)
        """
        super().__init__(size, size, lowest_x, lowest_y)
