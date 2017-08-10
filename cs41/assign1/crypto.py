#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Big Game

A suite of cryptographic functions
"""
import random
import utils
import operator
import functools

"""
Caesar Cipher
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caesar_cipher = {tup[0]:tup[1] for tup in
              zip(alphabet,alphabet[3:] + alphabet[:3])}

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    caesar_cipher is a dictionary representing the
    function f(alphabet[index_of(letter)])
                = alphabet((index_of(letter) + 3) % 26)

    This function simply maps each alphabetical letter
    of the plaintext to its caesar output using f.
    """
    return ''.join(map(
        lambda char: caesar_cipher[char]
                     if char in alphabet
                     else char,
                     plaintext.upper()))

def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    reverse_caesar_cipher is a dictionary representing the
    function f(alphabet[index_of(letter)])
                = alphabet((index_of(letter) - 3) % 26)

    This function simply maps each alphabetical letter
    of the plaintext to its reverse_caesar output using f.
    """
    reverse_caesar_cipher = {val:key for key, val in caesar_cipher.items()}
    return ''.join(map(
        lambda char: reverse_caesar_cipher[char]
                      if char in alphabet else char,
                      ciphertext.upper()))

"""
Vigenere Cipher
"""

def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher with a keyword.
    
    First the repeated keyword is expanded to match the length
    of the plaintext. Then the sum of the indices of the plaintext
    plus the keyword is mapped to the appropriate letter of the
    alphabet.
    """
    n_repeats = len(plaintext) // len(keyword) + 1
    keyword_repeated = (keyword * n_repeats)[:len(plaintext)]
    num_plaintext = [ord(char) - ord('A') for char in plaintext]
    increments = [ord(char) - ord('A') for char in keyword_repeated]
    return ''.join(map(lambda char, inc: alphabet[(char + inc) % 26], zip(num_plaintext, increments)))


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using a Vigenere cipher with a keyword.

    First the repeated keyword is expanded to match the length
    of the plaintext. Then the sum of the indices of the plaintext
    minus the keyword is mapped to the appropriate letter of the
    alphabet.
    """
    n_repeats = len(plaintext) // len(keyword) + 1
    keyword_repeated = (keyword * n_repeats)[:len(plaintext)]
    num_ciphertext = [ord(char) - ord('A') for char in ciphertext]
    increments = [ord(char) - ord('A') for char in keyword_repeated]
    return ''.join(map(lambda char, inc: alphabet[(char - inc) % 26], zip(num_ciphertext, increments)))


"""
Merkle-Hellman Knapsack Cryptosystem
"""
def super_increasing_generator():
    first = True
    total = 0
    while True:
        if first:
            next_int = random.randint(2, 10)
            first = False
        else:
            next_int = random.randint(total+1, 2*total)
        total = total + next_int
        yield next_int

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    return a if b % a == 0 else gcd(b % a, a)

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    w = []
    gen = super_increasing_generator()
    for i in range(n):
        w.append(next(gen))
    q = next(gen)
    r = random.randint(2, q-1)
    while gcd(q, r) > 1:
        r = random.randint(2,q-1)
    return (tuple(w), q, r)

def create_public_key(private_key):
    """Creates a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    w, q, r = private_key
    return tuple([(r * w_i) % q for w_i in w])

def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes OR a message string
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    if type(message) == str:
        chunks = map(ord, list(message))
    else: # type(message) == message bytes
        chunks = list(message)
    chunks = map(utils.byte_to_bits, chunks)
    chunks = [zip(chunk, public_key) for chunk in chunks]
    return [sum(
        [(letter_bit * pubkey_bit) for (letter_bit, pubkey_bit) in chunk])
            for chunk in chunks]

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r
    
    @return bytearray or str of decrypted characters
    """
    
    w, q, r = private_key
    s = utils.modinv(r, q)
    c_primes = map(lambda c: (c*s) % q, message)
    
    """
    The following line is the heart of the decryption 
    algorithm. It is rather dense, so I will provide 
    equivalent pseudocode and a worked example of how 
    the reduction transforms a single c_prime value 
    into the bits of a decrypted letter.
    
    Equivalent pseudocode:
    bits = []
    for w_i in reversed(w):
        if w_i > c_prime:
            bits.prepend(0)
        else:
            bits.prepend(1)
            c_prime -= w_i
    return bits
    
    [[c_prime]] + list(reversed(w)) 
           =  [[1293], 2771, 1133, 389, 154, 55, 18, 6, 4]
    reduce => [[1293, 0], 1133, 389, 154, 55, 18, 6, 4]
    reduce => [[160, 1, 0], 389, 154, 55, 18, 6, 4]
    reduce => [[160, 0, 1, 0], 154, 55, 18, 6, 4]
    reduce => [[6, 1, 0, 1, 0], 55, 18, 6, 4]
    reduce => [[6, 0, 1, 0, 1, 0], 18, 6, 4]
    reduce => [[6, 0, 0, 1, 0, 1, 0], 6, 4]
    reduce => [[0, 1, 0, 0, 1, 0, 1, 0], 4]
    reduce => [[0, 0, 1, 0, 0, 1, 0, 1, 0]]
    
    After the reduction, the subsequent steps transform
    the decrypted letter-bits into a decrypted letter
    which is joined with the other letters to obtain the
    plaintext.
    
    # remove the c_prime value placeholder
    remove_first => [[0, 1, 0, 0, 1, 0, 1, 0],...]
    to_byte      =>  [74,...]
    to_char      =>  ['J',...]
    ''.join(chars) => 'James'
    
    """
    decrypted_bits = map(
        lambda c_prime:
            functools.reduce(
                lambda x, y:
                    [x[0]] + [0] + x[1:] if y > x[0] else
                    [x[0] - y] + [1] + x[1:],
                [[c_prime]] + list(reversed(w))),
        c_primes)
    decrypted_bits = map(lambda lst: lst[1:], decrypted_bits)
    decrypted_bytes = map(utils.bits_to_byte, decrypted_bits)
    return ''.join(map(chr, decrypted_bytes))


#########################################################
#            IMPLEMENTATION OF CONSOLE MENU             #
# You shouldn't need to change anything below this box. #
#########################################################

def clean_caesar(text):
    """Convert text to a form compatible with the preconditions imposed by Caesar cipher"""
    return text.upper()

def clean_vigenere(text):
    return ''.join(ch for ch in text.upper() if ch.isupper())

def run_caesar():
    action = utils.get_action()
    encrypting = action == 'E'
    data = clean_caesar(utils.get_input(binary=False))

    print("* Transform *")
    print("{}crypting {} using Caesar cipher...".format('En' if encrypting else 'De', data))

    output = (encrypt_caesar if encrypting else decrypt_caesar)(data)

    utils.set_output(output)


def run_vigenere():
    action = utils.get_action()
    encrypting = action == 'E'
    data = clean_vigenere(utils.get_input(binary=False))

    print("* Transform *")
    keyword = clean_vigenere(input("Keyword? "))

    print("{}crypting {} using Vigenere cipher and keyword {}...".format('En' if encrypting else 'De', data, keyword))

    output = (encrypt_vigenere if encrypting else decrypt_vigenere)(data, keyword)

    utils.set_output(output)


def run_merkle_hellman():
    action = utils.get_action()

    print("* Seed *")
    seed = input("Set Seed [enter for random]: ")
    import random
    random.seed(seed)
    print("* Building private key...")

    private_key = generate_private_key()
    public_key = create_public_key(private_key)

    if action == 'E':  # Encrypt
        data = utils.get_input(binary=True)
        print("* Transform *")
        chunks = encrypt_mh(data, public_key)
        output = ' '.join(map(str, chunks))
    else:  # Decrypt
        data = utils.get_input(binary=False)
        chunks = [int(line.strip()) for line in data.split() if line.strip()]
        print("* Transform *")
        output = decrypt_mh(chunks, private_key)

    utils.set_output(output)


def run_suite():
    """
    Runs a single iteration of the cryptography suite.

    Asks the user for input text from a string or file, whether to encrypt
    or decrypt, what tool to use, and where to show the output.
    """
    print('-' * 34)
    tool = utils.get_tool()
    # This isn't the cleanest way to implement functional control flow,
    # but I thought it was too cool to not sneak in here!
    commands = {
        'C': run_caesar,         # Caesar Cipher
        'V': run_vigenere,       # Vigenere Cipher
        'M': run_merkle_hellman  # Merkle-Hellman Knapsack Cryptosystem
    }
    commands[tool]()


def main():
    
    """Test example for debugging/testing
    priv_key = ((4, 6, 18, 55, 154, 389, 1133, 2771), 4931, 1176)
    pub_key = (4704, 2125, 1444, 577, 3588, 3812, 1038, 4236)

    message = 'James' # ['J', 'a', 'm', 'e', 's'] => [74, 97, 109, 101, 115]
    message = encrypt_mh(message, pub_key) # [6751, 7805, 15205, 11617, 9420]
    message = decrypt_mh(message, priv_key) # 'James'
    """
    
    """Harness for CS41 Assignment 1"""
    print("Welcome to the Cryptography Suite!")
    run_suite()
    while utils.get_yes_or_no("Again?"):
        run_suite()
    print("Goodbye!")


if __name__ == '__main__':
    main()
