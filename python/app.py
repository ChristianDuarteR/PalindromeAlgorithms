import matplotlib
from matplotlib import pyplot as plt

import executing_time_gathering

matplotlib.use('TkAgg')
import pandas as pd

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