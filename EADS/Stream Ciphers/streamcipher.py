import functools
from operator import xor

class LFSR:

    def __init__(self, poly, state=None):
        self._poly = poly
        self._state = state
        self.length = max(poly)
        self.poly = [1 if i in poly else 0 for i in range(self.length + 1)]

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        self.state.insert(0, self.feedback)
        self.state = self.state[:self.length]
        self.output = self.state[self.length - 1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

        return self.output

    def run_steps(self, n=0):
        return [next(self) for _ in range(n)]

    def cycle(self, state=None):
        if state is not None:
            self.state = state

        return self.run_steps(self.length)

    def __str__(self):
        return f'{self.state} {self.output} {self.feedback}'


class BerlekampMassey:

    def __init__():
        pass


class ShrinkingGenerator:

    def __init__(self):
        pass

class SelfShrinkingGenerator:

    def __init__(self):
        pass

