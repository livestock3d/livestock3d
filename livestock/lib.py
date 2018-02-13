__author__ = "Christian Kongsgaard"
__license__ = "MIT"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

# Module imports

# Livestock imports

# Grasshopper imports

# -------------------------------------------------------------------------------------------------------------------- #
# Livestock Functions


def my_function(folder):

    file = open(folder + '/my_file.txt', 'r')
    my_lines = [line.strip()
                for line in file.readlines()]

    file.close()
    print(my_lines)

    result_file = open(folder + '/my_result.txt', 'w')
    [result_file.write(line) for line in my_lines]
    result_file.close()

    return None
