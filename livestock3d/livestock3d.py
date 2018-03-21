__author__ = "Christian Kongsgaard"
__license__ = "MIT"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

# Module imports
import numpy as np
import matplotlib.pyplot as plt

# Livestock imports

# Grasshopper imports

# -------------------------------------------------------------------------------------------------------------------- #
# Livestock Functions


def my_function(folder):

    file = open(folder + '/data_file.txt', 'r')
    my_lines = [line.strip()
                for line in file.readlines()]
    file.close()

    repeat = int(my_lines[1].strip())
    line_to_write = my_lines[0].strip()

    result_file = open(folder + '/result.txt', 'w')

    for i in range(repeat):
        result_file.write(line_to_write + '\n')

    result_file.close()

    return None


def plot_graph(folder):
    y_values = np.loadtxt(folder + '/data_file.txt')
    x_values = np.linspace(0, len(y_values), len(y_values))

    plt.figure()
    plt.plot(x_values, y_values)
    plt.savefig(folder + '/plot.png')

    return None