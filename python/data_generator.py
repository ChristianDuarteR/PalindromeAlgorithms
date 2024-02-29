import random

from python import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(''.join(get_random_character(1, limit)))
    return answer


def get_random_character(start, limit):
    return random.choices(constants.ALLOWED_CHARS, k=random.randint(start, limit))


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)
