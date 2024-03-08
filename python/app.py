import matplotlib
from matplotlib import pyplot as plt

import executing_time_gathering
from python.data_generator import get_random_palindrome

matplotlib.use('TkAgg')
import pandas as pd


def is_palindrome(word):
    return word == word[::-1]


def test_generar_palindromes():
    random_palindromes = []
    non_palindromes = []

    for _ in range(100):
        word = get_random_palindrome(5)
        if is_palindrome(word):
            random_palindromes.append(word)
        else:
            non_palindromes.append(word)

    print("Palabras palíndromas generadas aleatoriamente:")
    print(random_palindromes[:5])

    # Imprimir algunas palabras que no son palíndromas generadas aleatoriamente
    print("\nPalabras que no son palíndromas generadas aleatoriamente:")
    print(non_palindromes[:5])

#if __name == "__main__":
#    test_generar_palindromes()


if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 20000
    step = 2000
    samples_by_size = 3

    table = executing_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    df = pd.DataFrame(table,
                   columns=["Size", "Direct Comparation",
                            "Reversive Comparation", "Recursive Comparation"])
    print(df)

    df.plot(x="Size",
         y=["Direct Comparation", "Reversive Comparation", "Recursive Comparation"], kind="line", marker="x")

    plt.show()
