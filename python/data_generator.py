import random
import string

from python import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(''.join(get_random_palindrome(limit)))
    return answer


# Generador de palabras (Pueden o no ser palindromes)
def get_random_palindrome(size):
    half_size = size // 2
    first_half = ''.join(random.choices(string.ascii_lowercase, k=half_size))

    # Introducimos un cambio aleatorio en la segunda mitad
    second_half = first_half[::-1]
    ##if random.random() < 0.5:  # 50% de las veces
    ##    second_half = second_half[:-1] + random.choice(string.ascii_lowercase)

    return first_half + second_half


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)
