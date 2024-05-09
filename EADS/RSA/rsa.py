import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class RSA:
    """ RSA class to encrypt and decrypt messages using the RSA algorithm
    """

    def __init__(self, length = None, p = None, q = None):
        """ Initialize the RSA object

        Args:
            p: first prime number
            q: second prime number
        """

        self.length = length
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.key_pub = self.find_e()
        self.key_priv = self.find_d()

    def find_e(self):
        """ Find e = 2, 3, 4, ... phi-1 such that e is coprime with phi

        Returns:
            e: the public key
        """

        for i in range(2, self.phi):
            if self.is_coprime(i, self.phi):
                return i

    def find_d(self):
        """ Find d = e^-1 mod phi

        Returns:
            d: the private key
        """

        for i in range(2, self.phi):
            if (self.key_pub * i) % self.phi == 1:
                return i

    def is_coprime(self, a, b):
        """ Check if two numbers are coprime

        Args:
            a: first number
            b: second number

        Returns:
            coprime: True if a and b are coprime, False otherwise
        """

        while b:
            a, b = b, a % b
        return a == 1

    def encrypt(self, plaintext):
        """ Encrypt the message using the public key

        Args:
            plaintext: the message to encrypt

        Returns:
            ciphertext: the encrypted message
        """

        # pow(x, y, z) calculates x^y % z
        return square_multiply(plaintext, self.key_pub, self.n)

    def decrypt(self, ciphertext):
        """ Decrypt the message using the private key

        Args:
            ciphertext: the encrypted message

        Returns:
            plaintext: the decrypted message
        """

        # pow(x, y, z) calculates x^y % z
        return square_multiply(ciphertext, self.key_priv, self.n)

def extended_euclidean_algorithm(a, m):
    """ Extended Euclidean Algorithm to find the inverse of a mod m

    Args:
        a: first number
        m: second number

    Raises:
        ValueError: Numbers are not coprime, they have not an inverse

    Returns:
        r0: gcd(a, m)
        s0:
        t0:
    """

    r0, r1 = m, a
    s0, s1, t0, t1 = 0, 1, 1, 0

    i = 0
    while r1 != 0:
        i += 1
        r = r0 % r1 # Calculate the remainder
        q = (r0 - r) // r1 # Calculate the quotient
        s = s0 - q * s1 # Calculate the new value of s
        t = t0 - q * t1 # Calculate the new value of t

        # Update values
        r0, r1 = r1, r
        s0, s1 = s1, s
        t0, t1 = t1, t

    return r0, s0, t0

def square_multiply(x, e, n):
    """ Square and Multiply algorithm to calculate x^e % n

    Args:
        x: base
        e: exponent
        n: modulus

    Returns:
        result: x^e % n
    """

    result = 1
    for bit in bin(e)[2:]:
        result = (result ** 2) % n
        if bit == '1':
            result = (result * x) % n
    return result

def miller_rabin(p, N):
    """ Miller-Rabin primality test to check if a number is prime

    Args:
        p: number to test
        N: number of iterations

    Returns:
        prime: True if p is prime, False otherwise
    """

    if p == 2:
        return True

    if p % 2 == 0:
        return False

    # Write p as 2^r * d + 1
    r = 0
    d = p - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(N):
        a = random.randint(2, p - 1)
        x = square_multiply(a, d, p)
        if x == 1 or x == p - 1:
            continue

        for _ in range(r - 1):
            x = square_multiply(x, 2, p)
            if x == 1:
                return False
            if x == p - 1:
                break
        else:
            return False

    return True