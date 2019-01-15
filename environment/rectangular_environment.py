from environment.environment import Environment


class RectangularEnvironment(Environment):
    """
    RectangularEnvironment is a class allowing to define a rectangular
    environment in which something or someone can move.
    """

    def __init__(self, x_size: int, y_size: int, lowest_x: int = 0,
                 lowest_y: int = 0):
        """
        Create a RectangularEnvironment
        :param x_size: the size of the rectangle on x axis
        :type x_size: int
        :param y_size: the size of the rectangle on y axis
        :type y_size: int
        :param lowest_x: the lowest coordinate of the rectangle on x axis
        (default 0)
        :type lowest_x: int
        :param lowest_y: the lowest coordinate of the rectangle on y axis
        (default 0)
        :type lowest_y: int
        """
        super().__init__()
        self.x_size = x_size
        self.y_size = y_size
        self.lowest_x = lowest_x
        self.lowest_y = lowest_y

    def is_tile(self, position: tuple):
        """
        Extend default is_tile behaviour by checking that given position is
        contained in the defined rectangle by the environment.
        :type position: tuple
        :return: True if position is a tile of the environment
        :rtype: bool
        """
        return super().is_tile(position) and self._x_position_is_valid(
            position[0]) and self._y_position_is_valid(position[1])

    def _x_position_is_valid(self, x: int):
        """
        Check if a x axis coordinate is valid, that means that it is bigger than
        the lowest value and smaller than the x axis size of the rectangle.
        :param x: the x axis coordinate to test
        :type x: int
        :return: True if x axis coordinate is valid
        :rtype: bool
        """
        return self.lowest_x <= x < (self.lowest_x + self.x_size)

    def _y_position_is_valid(self, y: int):
        """
        Check if a y axis coordinate is valid, that means that it is bigger than
        the lowest value and smaller than the y axis size of the rectangle.
        :param y: the y axis coordinate to test
        :type y: int
        :return: True if y axis coordinate is valid
        :rtype: bool
        """
        return self.lowest_y <= y < (self.lowest_y + self.y_size)
