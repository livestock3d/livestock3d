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
    my_lines = file.readlines()
    file.close()
    print(my_lines)

    result_file = open(folder + '/my_result.txt', 'w')
    result_file.write(my_lines)
    result_file.close()

    return None
