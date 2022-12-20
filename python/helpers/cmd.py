"""
Helper functions for running other command line tools
"""

from typing import List, Generator

from .error import CliError


def process_cmd(args: List[str]) -> Generator:
    """
    Run a program and process its output

    Parameters
    ----------
    args: List[str]
        Command line arguments to run

    Returns
    -------
    lines: Generator
        Sequence of lines constituing the output of runnned program
    """
    yield
