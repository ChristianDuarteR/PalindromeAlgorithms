import random
import time

from python import algorithms
from python import constants
from python import data_generator
from python.algorithms import directiveComparative, reversiComparative, recursiveApproach
from python.data_generator import get_random_list


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(''.join(get_random_list(size)))
    return [
        take_time_for_algorithm(samples, directiveComparative),
        take_time_for_algorithm(samples, reversiComparative),
        take_time_for_algorithm(samples, recursiveApproach),
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
