__author__ = "Christian Kongsgaard"
__license__ = "MIT"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

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

    elif template_name == 'plot_graph':
        plot_graph(path)

    elif template_name == 'ssh':
        ssh_template(path)
        
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

    file_name = r'/my_first_template.py'
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


def plot_graph(path):
    """
    Writes a template.

    :param path: Path to write it to.
    :type path: str
    :return: The file name
    """

    file_name = r'/plot_graph_template.py'
    file = open(path + file_name, 'w')

    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("import platform\n")
    file.write("from pathlib import Path\n")

    file.write("system = platform.system()\n")
    file.write("if system == 'Windows':\n")
    file.write("    sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("elif system == 'Linux':\n")
    file.write("    sys.path.insert(0, str(Path.home()) + '/livestock3d' )\n")

    file.write("import livestock3d as ls\n")

    file.write("# Run function\n")
    file.write("ls.plot_graph()\n")

    file.write("# Announce that template finished and create out file\n")
    file.write("print('Finished with template')\n")
    file.write("file = open('out.txt', 'w')\n")
    file.write("file.close()\n")
    file.close()

    return file_name


def ssh_template(path):
    """
    Writes the ssh template.

    :param path: Path to write it to.
    """

    file_name = r'/ssh_template.py'
    file = open(path + file_name, 'w')

    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("import ssh\n")

    file.write("# Run function\n")
    file.write("ssh.ssh_connection()\n")

    file.close()

    return True