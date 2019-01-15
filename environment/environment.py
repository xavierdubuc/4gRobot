from abc import ABC


class Environment(ABC):
    """
    Environment is an abstract class allowing to define any environment in which
    something or someone can move.
    """

    def is_reachable(self, initial_position: tuple, final_position: tuple):
        """
        Check if a given position is reachable from another
        :param initial_position: the initial position from which the move would
        be ignited
        :type initial_position: tuple
        :param final_position: the position to reach
        :type final_position: tuple
        :return: True if final_position is reachable from initial_position,
        False otherwise
        :rtype: bool
        """
        return self.is_tile(initial_position) and self.is_tile(final_position)

    def is_tile(self, position: tuple):
        """
        Check if a given position is a existing tile.
        :param position: the position to check
        :type position: tuple
        :return: True if position is a tile of the environment
        :rtype: bool
        """
        return len(position) >= 2
