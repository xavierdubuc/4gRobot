import unittest

from environment.square_environment import SquareEnvironment


class SquareEnvironmentTestCase(unittest.TestCase):
    def setUp(self):
        self.size = 10
        self.environment = SquareEnvironment(self.size)

    def test_is_tile(self):
        for i in range(self.size):
            for j in range(self.size):
                self.assertTrue(self.environment.is_tile((i, j)), str((i, j)))
        fails = ((-1, 0), (0, -1), (0, self.size), (self.size, 0))
        for fail in fails:
            self.assertFalse(self.environment.is_tile(fail), str(fail))

    def test_is_reachable(self):
        for i in range(self.size):
            for j in range(self.size):
                if i < self.size - 1:
                    self.assertTrue(
                        self.environment.is_reachable((i, j), (i + 1, j)))
                if i > 0:
                    self.assertTrue(
                        self.environment.is_reachable((i, j), (i - 1, j)))
                if j < self.size - 1:
                    self.assertTrue(
                        self.environment.is_reachable((i, j), (i, j + 1)))
                if j > 0:
                    self.assertTrue(
                        self.environment.is_reachable((i, j), (i, j - 1)))
                fails = ((-1, 0), (0, -1))
                for fail in fails:
                    self.assertFalse(
                        self.environment.is_reachable((i, j), fail))
