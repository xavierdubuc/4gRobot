from orientation.direction import Direction


class Compass:
    """
    Compass represents the cardinal points and the relations between them.
    directions variable contains all the supported cardinal points.
    """
    directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH,
                  Direction.WEST]

    @staticmethod
    def right(direction: Direction):
        """
        Give the cardinal point directly to the right of a given initial
        cardinal point.
        :param direction: the initial cardinal point
        :type direction: Direction
        :return: the cardinal point lying on the right of initial cardinal point
        """
        directions = __class__.directions
        return directions[(directions.index(direction) + 1) % len(directions)]

    @staticmethod
    def left(direction: Direction):
        """
        Give the cardinal point directly to the left of a given initial
        cardinal point.
        :param direction: the initial cardinal point
        :type direction: Direction
        :return: the cardinal point lying on the left of initial cardinal point
        """
        directions = __class__.directions
        return directions[(directions.index(direction) - 1) % len(directions)]
