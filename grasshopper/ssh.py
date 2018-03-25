__author__ = "Christian Kongsgaard"
__license__ = "MIT"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

# Module imports
import os

# Livestock imports
from livestock3d import templates

# Grasshopper imports
import scriptcontext as sc


# -------------------------------------------------------------------------------------------------------------------- #
# Grasshopper SSH functions

ssh_path = r'C:\livestock3d\ssh'
local_path = r'C:\livestock3d\local'

def get_ssh():
    """Extracts the SSH information from a sticky"""

    ip = str(sc.sticky["SSH"]['ip'])
    port = str(sc.sticky["SSH"]['port'])
    user = str(sc.sticky["SSH"]['user'])
    pw = str(sc.sticky["SSH"]['password'])

    ssh_dict = {'ip': ip, 'port': port, 'user': user, 'password': pw}

    return ssh_dict


def clean_ssh_folder():
    """Cleans the livestock/ssh folder on the C drive."""

    if os.path.isdir(ssh_path):
        for file in os.listdir(ssh_path):
            os.remove(ssh_path + '/' + file)
    else:
        os.mkdir(ssh_path)


def clean_local_folder():
    """Cleans the livestock/local folder on the C drive."""

    if os.path.isdir(local_path):
        for file in os.listdir(local_path):
            os.remove(local_path + '/' + file)
    else:
        os.mkdir(local_path)


def write_ssh_commands(ssh_dict):
    """
    Write the files need for Livestock SSH connection to work.

    :param ssh_dict: Dictionary with all SSH information. Needs to be on the following form:
    {'ip': string, 'user': string,
    'port': string, 'password': 'string',
    'file_transfer': list of strings, 'file_run': list of strings,
    'file_return': list of strings, 'template': string}
    """

    # Write SSH commands
    ssh_file = open(ssh_path + '/in_data.txt', 'w')
    ssh_file.write(str(ssh_dict['ip']) + '\n')
    ssh_file.write(str(ssh_dict['port']) + '\n')
    ssh_file.write(str(ssh_dict['user']) + '\n')
    ssh_file.write(str(ssh_dict['password']) + '\n')
    ssh_file.write(str(ssh_dict['file_transfer']) + '\n')
    ssh_file.write(str(ssh_dict['file_run']) + '\n')
    ssh_file.write(str(ssh_dict['file_return']) + '\n')
    ssh_file.close()

    # Write templates
    templates.ssh_template(ssh_path)
    templates.pick_template(ssh_dict['template'], ssh_path)

    return True