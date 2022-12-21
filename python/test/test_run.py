#!/usr/bin/env python3

"""
Test program invocation with different parameters
"""

PROGRAM_NAME = 'cli_sample.py'

from string import printable, whitespace
import subprocess
import sys
import tempfile

from hypothesis import given, settings
from hypothesis.strategies import lists, text


# printable chars besides tabs and linebreaks
more_printable = printable.strip(whitespace) + ' '

def test_run_no_args_print_usage():
    """Run with no arge
    prints usage string"""
    args = [
        sys.executable,
        'cli_sample.py',
    ]
    proc = subprocess.run(args, capture_output=True, text=True)
    assert proc.stderr.startswith('Usage:\n')
    assert proc.returncode == 1


@settings(deadline=None)
@given(text(more_printable))
def test_run_process_string(string):
    """Run with --string option

    Program shall return supplied string
    """
    args = [
        sys.executable,
        'cli_sample.py',
        '--format=raw',
        '--string',
        string,
    ]
    proc = subprocess.run(args, capture_output=True, text=True)
    assert proc.stdout == string
    assert proc.returncode == 0


@given(lists(text(more_printable)))
def test_run_process_file(contents):
    """Run with --file option

    Program shall return file contents
    """
    with tempfile.NamedTemporaryFile(mode='w') as fp:
        fp.writelines(contents)
        args = [
            sys.executable,
            'cli_sample.py',
            '--format=raw',
            '--file',
            fp.name,
        ]
        proc = subprocess.run(args, capture_output=True, text=True)
        assert proc.stdout.splitlines() == contents
        assert proc.returncode == 0
