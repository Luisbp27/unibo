import functools
from operator import xor

class LFSR:
    """ Linear Feedback Shift Register (LFSR) class
    LFSR is a shift register whose input bit is a linear function of its previous state.
    The output bit is the last bit of the state.

    Attributes:
    - poly: Polynomial of the LFSR
    - length: Length of the LFSR
    - state: Initial state of the LFSR
    - output: Output bit of the LFSR
    - feedback: Feedback bit of the LFSR

    Methods:
    - __init__: Constructor
    - __len__: Returns the length of the LFSR
    - __iter__: Iterator
    - __next__: Returns the next output bit of the LFSR
    - run_steps: Execute N LFSR steps and returns the corresponding output list of bool
    - cycle: Returns a list of boolean values representing the full LFSR cycle
    - __str__: Returns a string representation of the LFSR
    """

    def __init__(self, poly, state=None):
        """ Constructor

        Args:
            poly: Polynomial of the LFSR
            state: Initial state of the LFSR. Default is None.
        """

        self.length = max(poly)
        # Convert the polynomial to a list of bits
        self.poly = [1 if i in poly else 0 for i in range(self.length + 1)][::-1]
        self.state = state

        # If no state is provided, initialize all bits to 1
        if state is None:
            self.state = [1] * self.length
        else:
            # Convert the state to a list of bits
            self.state = [int(i) for i in list(bin(state)[2:])]
            self.state = [0]*(self.length - len(self.state)) + self.state if (self.length > len(self.state)) else self.state

        print(f"Initial state: {self.state}")

        self.output = self.state[:1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

    def __len__(self):
        """ Returns the length of the LFSR

        Returns:
            length: Length of the LFSR
        """

        return self.length

    def __iter__(self):
        """ Iterator

        Returns:
            self: LFSR
        """

        return self

    def __next__(self):
        """ Returns the next output bit of the LFSR

        Returns:
            output: Output bit of the LFSR
        """

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
        """ Execute N LFSR steps and returns the corresponding output list of bool

        Args:
            n: Number of steps to perform. Default is 1.

        Returns:
            list_of_bool: List of boolean values representing the output of the LFSR
        """

        return [next(self) for _ in range(n)]

    def cycle(self, state=None):
        """ Returns a list of boolean values representing the full LFSR cycle

        Args:
            state: Initial state of the LFSR. Default is None.

        Returns:
            list_of_bool: List of boolean values representing the full LFSR cycle
        """

        if state is not None:
            self.state = state

        # The number of steps to perform is 2^L - 1, where L is the length of the LFSR
        return [next(self) for _ in range(2**self.length - 1)]

    def __str__(self):
        """ Returns a string representation of the LFSR

        Returns:
            str: String representation of the LFSR
        """

        return f'{self.state} {self.output} {self.feedback}'


def berlekamp_massey(b):
    """ Berlekamp-Massey algorithm
    Berlekamp-Massey algorithm is a method to find the shortest LFSR that can generate a given binary sequence.

    Args:
        b : List of binary values

    Returns:
        poly: Polynomial of the LFSR
    """

    m = 0 # LFSR length
    r = 1 # LFSR feedback polynomial degree
    N = len(b) # Length of the input sequence
    P = [1] # P(x) = 1
    Q = [1] # Q(x) = 1
    R = [] # R(x) = 0

    for t in range(N):
        d = 0
        for j in range(m+1):
            d = xor(d, P[j] and b[t-j]) # Calculate the discrepancy
        if (d == 1):
            # If the discrepancy is 1, update the new polynomial R(x)
            Qtemp = Q.copy()
            for i in range(r):
                Qtemp = [0] + Qtemp
            if (2*m <= t):
                R = P.copy() # R(x) <- P(x)
                for i in range(min(len(Qtemp), len(P))):
                    P[i] = xor(P[i], Qtemp[i])
                if (len(Qtemp) > len(P)):
                    P += [0] * (len(Qtemp) - len(P) + r)
                    for i in range(len(Qtemp)):
                        P[i + r] = xor(P[i + r], Qtemp[i])  # P(x) = P(x) + Qtemp(x)*x^r
                Q = R.copy() # Q(x) <- R(x)
                m = t + 1 - m
                r = 0
            else:
                for i in range(min(len(Qtemp), len(P))):
                    P[i] = xor(P[i], Qtemp[i])
                if len(Qtemp) > len(P):
                    P += [0] * (len(Qtemp) - len(P) + r)
                    for i in range(len(Qtemp)):
                        P[i + r] = xor(P[i + r], Qtemp[i])  # P(x) = P(x) + Qtemp(x)*x^r
        r += 1 # r <- r + 1

    poly = [i for i, x in enumerate(P) if x] # P(x)

    return poly


class ShrinkingGenerator:
    """ Shrinking Generator based on two LFSRs
    Shrinking Generator is a stream cipher that generates a key stream by combining two LFSRs.
    The output bit is the result of the bitwise AND operation between the output bits of the two LFSRs.

    Attributes:
    - polyA: Polynomial of the first LFSR
    - polyS: Polynomial of the second LFSR
    - stateA: Initial state of the first LFSR
    - stateS: Initial state of the second LFSR
    - lfsrA: First LFSR
    - lfsrS: Second LFSR
    - output: Output bit of the Shrinking Generator

    Methods:
    - __init__: Constructor
    - __iter__: Iterator
    - __next__: Returns the next output bit of the Shrinking Generator
    """

    def __init__(self, polyA=None, polyS=None, stateA=None, stateS=None):
        """ Constructor

        Args:
            polyA: Polynomial of the first LFSR. Default is None.
            polyS: Polynomial of the second LFSR. Default is None.
            stateA: Initial state of the first LFSR. Default is None.
            stateS: Initial state of the second LFSR. Default is None.
        """

        self.lfsrA = LFSR(polyA, stateA)
        self.lfsrS = LFSR(polyS, stateS)
        self.output = None

    def __iter__(self):
        """ Iterator

        Returns:
            self: Shrinking Generator
        """

        return self

    def __next__(self):
        """ Returns the next output bit of the Shrinking Generator

        Returns:
            output: Output bit of the Shrinking Generator
        """

        a = next(self.lfsrA)
        s = next(self.lfsrS)
        self.output = a & s

        return self.output

class SelfShrinkingGenerator:
    """ Self-Shrinking Generator based on a LFSR
    Self-Shrinking Generator is a stream cipher that generates a key stream by using a single LFSR.
    The output bit is the result of the bitwise AND operation between the output bit of the LFSR and a selection bit.

    Attributes:
    - poly: Polynomial of the LFSR
    - selection_bit: Selection bit
    - state: Initial state of the LFSR
    - lfsr: LFSR
    - output: Output bit of the Self-Shrinking Generator

    Methods:
    - __init__: Constructor
    - __iter__: Iterator
    - __next__: Returns the next output bit of the Self-Shrinking Generator
    """

    def __init__(self, poly=None, selection_bit=3, state=None):
        """ Constructor

        Args:
            poly: Polynomial of the LFSR. Default is None.
            selection_bit: Selection bit. Default is None.
            state: Initial state of the LFSR. Default is None.
        """

        self.lfsr = LFSR(poly, state)
        self.sbit = selection_bit
        self.output = None

    def __iter__(self):
        """ Iterator

        Returns:
            self: Self-Shrinking Generator
        """

        return self

    def __next__(self):
        """ Returns the next output bit of the Self-Shrinking Generator

        Returns:
            output: Output bit of the Self-Shrinking Generator
        """

        s = next(self.lfsr)
        self.output = s & self.sbit
        return self.output

