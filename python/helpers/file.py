"""
Helper functions for file processing
"""

from .error import CliError


def process_file(path: str):
    """
    Process input data from file

    Parameters
    ----------
    path: str
        Description of your command-line interface.

    Returns
    -------
    lines: Generator
        Sequence of lines constituing the input file
    """
    try:
        with open(path) as file:
            return [l.strip() for l in file.readlines()]
    except OSError as err:
        raise CliError from err
