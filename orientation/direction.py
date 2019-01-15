from enum import Enum


class Direction(Enum):
    """
    A Direction enum element represents a cardinal point.
    A vector is assigned to each of them to represent the move it implies.
    """
    NORTH = (0, 1)
    WEST = (-1, 0)
    SOUTH = (0, -1)
    EAST = (1, 0)
