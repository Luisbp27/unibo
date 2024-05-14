import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

## TASK 1

class RSA:
    """ RSA class to encrypt and decrypt messages using the RSA algorithm
    """

    def __init__(self, length=None, p=None, q=None):
        """ Initialize the RSA object

        Args:
            p: first prime number
            q: second prime number
        """

        # If length is not provided, set it to 1024 bits
        if length is None:
            length = 1024

        self.length = length

        # If p or q are not provided, generate them
        if p is None or q is None:
            p = self.generate_prime()
            q = self.generate_prime()

        self.p = p
        self.q = q

        # Calculate the other parameters
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
            gcd, _, _ = extended_euclidean_algorithm(i, self.phi)
            if gcd == 1:
                return i

    def find_d(self):
        """ Find d = e^-1 mod phi

        Returns:
            d: the private key
        """

        _, x, _ = extended_euclidean_algorithm(self.key_pub, self.phi)
        return x % self.phi

    def generate_prime(self):
        """ Generate a prime number using CSPRNG for more security and Miller-Rabin primality test

        Returns:
            p: the prime number
        """

        while True:
            # Generate a random number of length bits
            p = int.from_bytes(get_random_bytes(self.length // 8), byteorder='big')
            if miller_rabin(p, 50):
                return p

    def encrypt(self, plaintext):
        """ Encrypt the message using the public key

        Args:
            plaintext: the message to encrypt

        Returns:
            ciphertext: the encrypted message
        """

        return square_multiply(int.from_bytes(plaintext, byteorder='big'), self.key_pub, self.n)

    def decrypt(self, ciphertext):
        """ Decrypt the message using the private key

        Args:
            ciphertext: the encrypted message

        Returns:
            plaintext: the decrypted message
        """

        plaintext = square_multiply(ciphertext, self.key_priv, self.n)

        # Calculate the number of bytes needed to represent the plaintext
        # We add 7 to round up to the nearest byte
        plaintext_bytes = (plaintext.bit_length() + 7) // 8

        return plaintext.to_bytes(plaintext_bytes, byteorder='big')

def extended_euclidean_algorithm(a, m):
    """ Extended Euclidean Algorithm to find the inverse of a mod m

    Args:
        a: first number
        m: second number

    Returns:
        r0: gcd(a, m)
        s0: quotient of the division of a by m
        t0: quotient of the division of m by a
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

## TASK 2

def aes_encrypt(key, plaintext):
    """ Encrypt the message using the AES algorithm in ECB mode with manual padding

    Args:
        key: the key to encrypt the message
        plaintext: the message to encrypt

    Returns:
        ciphertext: the encrypted message
    """

    cipher = AES.new(key, AES.MODE_ECB)
    block_size = AES.block_size
    ciphertext = b''

    # Encrypt each block individually
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        if len(block) == block_size:
            ciphertext += cipher.encrypt(block)
        else:
            block += b'\x00' * (block_size - len(block)) # Add padding
            ciphertext += cipher.encrypt(block)

    return ciphertext

def aes_decrypt(key, ciphertext):
    """ Decrypt the message using the AES algorithm in ECB mode with manual padding

    Args:
        key: the key to decrypt the message
        ciphertext: the message to decrypt

    Returns:
        plaintext: the decrypted message
    """

    cipher = AES.new(key, AES.MODE_ECB)
    block_size = AES.block_size
    plaintext = b''

    # Decrypt each block individually
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = cipher.decrypt(block)
        plaintext += decrypted_block.rstrip(b'\x00') # Remove padding

    return plaintext