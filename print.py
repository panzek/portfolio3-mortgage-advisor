"""
function to print text color 
using ASNI escape sequences 
"""

def print_red(text):
    """
    print terminal text in red color 
    """
    print(f'\033[0;31m{text}\033[00m')


def print_green(text):
    """
    print terminal text in green color 
    """
    print(f'\033[32m{text}\033[00m')


def print_cyan(text):
    """
    print terminal text in green color 
    """
    print(f'\033[36m{text}\033[00m')


def print_purple(text):
    """
    print terminal text in green color 
    """
    print(f'\033[35m{text}\033[00m')


def print_yellow(text):
    """
    print terminal text in green color 
    """
    print(f'\033[1;33m{text}\033[00m')