from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

## PART 1: AES

def display_cipher_image(cipher_data, shape):
    """ Display the image of the cipher data

    Args:
        cipher_data: the cipher data to display
        shape: the shape of the image
    """

    cipher_image = np.frombuffer(cipher_data, dtype=np.uint8).reshape(shape)
    plt.imshow(cipher_image, cmap='gray')
    plt.show()

## PART 2: MONTE CARLO SIMULATION

def monte_carlo_pi(n):
    """ Estimate the value of Pi using the Monte Carlo method with n points

    Args:
        n: number of points to use in the estimation

    Returns:
        pi: the estimated value of Pi as a float
    """

    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    return 4 * np.sum(x**2 + y**2 <= 1) / n


## PART 3: DIFFUSION AND CONFUSION

def plot_histogram(hamming_distances, average, axs, color, title):
    """ Plot a histogram of the Hamming distances between the original ciphertext and the modified ciphertexts

    Args:
        hamming_distances: a list of Hamming distances between the original ciphertext and the modified ciphertexts
        average: the average Hamming distance between the original ciphertext and the modified ciphertexts
        axs: the axis to plot the histogram on
        color: the color of the histogram bars
        title: the title of the histogram

    Returns:
        axs: the axis with the histogram plotted
    """

    axs.hist(hamming_distances, bins=20, color=color, edgecolor='black')
    axs.set_xlabel('Hamming Distance')
    axs.set_ylabel('Frequency')
    axs.set_title(f'Distribution of Hamming Distances ({title})')
    axs.axvline(average, color='red', linestyle='--', label=f'Average: {average}')
    axs.legend()

    return axs

def encrypt_by_mode(plaintext, key, mode):
    """ Encrypt the plaintext using the AES algorithm with the specified key and mode

    Args:
        plaintext: the plaintext to encrypt
        key: the key to use for encryption
        mode: the AES mode to use for encryption

    Returns:
        ciphertext: the encrypted ciphertext
    """

    if mode == "ecb":
        cipher_mode = modes.ECB()
    elif mode == "cbc":
        iv = get_random_bytes(16)
        cipher_mode = modes.CBC(iv)
    elif mode == "cfb":
        iv = get_random_bytes(16)
        cipher_mode = modes.CFB(iv)
    elif mode == "ctr":
        nonce = get_random_bytes(16)
        cipher_mode = modes.CTR(nonce)

    cipher = Cipher(algorithms.AES(key), cipher_mode, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()

def hamming_distance(s1, s2):
    """ Calculate the Hamming distance between two byte sequences

    Args:
        s1: the first byte sequence
        s2: the second byte sequence

    Returns:
        distance: the Hamming distance between the two sequences
    """

    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(s1, s2))

def n_hamming_distance(n, ciphertext, mod_ciphertext):
    """ Calculate the Hamming distance between the original ciphertext and n modified ciphertexts, as well as the average distance

    Args:
        n: number of iterations
        ciphertext: the original ciphertext
        mod_ciphertext: a list of modified ciphertexts

    Returns:
        hamming_distances: a list of Hamming distances between the original ciphertext and the modified ciphertexts
        average: the average Hamming distance between the original ciphertext and the modified ciphertexts
    """

    hamming_distances = []
    averages = []

    for i in range(n):
        distance = hamming_distance(ciphertext, mod_ciphertext[i])
        hamming_distances.append(distance)
        current_average = sum(hamming_distances) / len(hamming_distances)
        averages.append(current_average)

    return hamming_distances, averages[-1]

def create_modified_plaintexts(n, plaintext, key, mode):
    """ Create a list of n modified versions of the plaintext by flipping the i-th bit of the plaintext

    Args:
        n: number of modified plaintexts to create
        plaintext: the original plaintext
        key: the key to use for encryption
        mode: the AES mode to use for encryption

    Returns:
        modified_texts: a list of modified plaintexts
    """

    modified_texts = []
    for i in range(n):
        # Copy the original plaintext and flip the i-th bit of the entire plaintext sequence
        mod_plaintext = bytearray(plaintext)
        byte_index, bit_index = divmod(i, 8)  # Calculate byte index and bit position
        if byte_index < len(mod_plaintext):  # Check to avoid index out of range
            mod_plaintext[byte_index] ^= (1 << bit_index)
            modified_texts.append(encrypt_by_mode(bytes(mod_plaintext), key, mode)) # Encrypt the modified plaintext and add it to the list
    return modified_texts

def create_modified_plaintexts_by_keys(n, plaintext, key, mode):
    """ Create a list of n modified versions of the plaintext by flipping the i-th bit of the key

    Args:
        n: number of modified plaintexts to create
        plaintext: the original plaintext
        key: the key to use for encryption
        mode: the AES mode to use for encryption

    Returns:
        modified_texts: a list of modified plaintexts
    """

    modified_texts = []
    for i in range(n):
        modified_texts.append(encrypt_by_mode(plaintext, key[i], mode))
    return modified_texts

def modify_key(key):
    """ Modify the key by flipping each bit of the key

    Args:
        key: the original key

    Returns:
        mod_keys: a list of modified keys
    """

    modified_keys = []
    for i in range(len(key) * 8): # Create as many modified keys as there are bits in the key
        mod_key = bytearray(key)
        byte_index, bit_index = divmod(i, 8) # Calculate byte index and bit position
        mod_key[byte_index] ^= (1 << bit_index)
        modified_keys.append(bytes(mod_key))
    return modified_keys