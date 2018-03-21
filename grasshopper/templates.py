__author__ = "Christian Kongsgaard"
__license__ = "MIT"

# -------------------------------------------------------------------------------------------------------------------- #
# Livestock Templates Functions



def pick_template(template_name, path):
    """
    Writes a template given a template name and path to write it to.
    :param template_name: Template name.
    :param path: Path to save it to.
    """

    template_name = str(template_name)

    if template_name == 'my_first_template':
        my_first_template(path)

    else:
        raise NameError('Could not find template: ' + str(template_name))

    return True


def my_first_template(path):
    """
    Writes a template.

    :param path: Path to write it to.
    :type path: str
    :return: The file name
    """

    file_name = r'/my_firsts_template.py'
    file = open(path + file_name, 'w')

    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("import livestock3d as ls\n")

    file.write("# Run function\n")
    file.write("ls.my_function(r'" + path + "')\n")

    file.write("# Announce that template finished and create out file\n")
    file.write("print('Finished with template')\n")

    file.close()

    return file_name