import functools
from operator import xor

class LFSR:

    def __init__(self, poly, state=None):
        self.poly = poly
        self.length = max(poly)
        self.state = state
        self.output = self.state[:1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

        # If no state is provided, initialize all bits to 1
        if state is None:
            self.state = [1] * self.length
        else:
            # If the state is provided, it must have the same length as the polynomial
            if len(state) < self.length:
                # If the state is shorter than the polynomial, fill the remaining bits with 0
                self.state = [0] * (self.length - len(state)) + state
            else:
                self.state = state

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        """ Update LFSR state and returns output bit """
        # Insert the feedback bit at the beginning of the state
        self.state.insert(0, self.feedback)
        # Remove the last bit of the state
        self.state = self.state[:-1]
        # The output bit is the last bit of the state
        self.output = self.state[-1]

        # Calculate the feedback bit by performing bitwise AND between the polynomial and the current state
        # Then, apply XOR operation on the resulting bits
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

        return self.output

    def run_steps(self, n=1):
        """ Execute N LFSR steps and returns the corresponding output list of bool """
        return [next(self) for _ in range(n)]

    def cycle(self, state=None):
        """ Returns a list of boolean values representing the full LFSR cycle """
        if state is not None:
            self.state = state

        # The number of steps to perform is 2^L - 1, where L is the length of the LFSR
        return [next(self) for _ in range(2**self.length - 1)]

    def __str__(self):
        """ Returns a string representation of the LFSR """
        return f'{self.state} {self.output} {self.feedback}'


def berlekamp_massey(b):
    m = 0
    r = 1
    N = len(b)
    P = [1] # P(x) = 1
    Q = [1] # Q(x) = 1
    R = []

    for t in range(N):
        d = 0
        for j in range(m+1):
            d = xor(d, P[j] and b[t-j]) # Discrepancy computation
        if (d == 1):
            Qtemp = Q.copy()        #
            for i in range(r):      #
                Qtemp = [0] + Qtemp # Qtemp(x) = Q(x)*(x^r)
            if (2*m <= t):
                R = P.copy() # R(x) = P(x)
                for i in range(min(len(Qtemp), len(P))): #
                    P[i] = xor(P[i], Qtemp[i])           #
                if (len(Qtemp) > len(P)):                #
                    P += Qtemp[len(P):]                  # P(x) = P(x) + Qtemp(x)
                Q = R.copy() # Q(x) = R(x)
                m = t + 1 - m
                r = 0
            else:
                for i in range(min(len(Qtemp), len(P))): #
                    P[i] = xor(P[i], Qtemp[i])           #
                if (len(Qtemp) > len(P)):                #
                    P += Qtemp[len(P):]                  # P(x) = P(x) + Qtemp(x)
        r += 1

    # I need a list made of integers which tell me where in the polynomial I have a coefficient 1 or 0:
    # for a polynomial like 1 + 1x + 0x^2 + 1x^3, given by the algorithm as [1,1,0,1],
    # I get a list like [3,1,0], corresponding to x^3 + x + 1
    poly = []
    for i, x in enumerate(P):
        if (x):
            poly = [i] + poly

    return poly


class ShrinkingGenerator:

    def __init__(self):
        pass

class SelfShrinkingGenerator:

    def __init__(self):
        pass

