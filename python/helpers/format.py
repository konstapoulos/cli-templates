"""
Helpers for producing output in different formats
"""

import json
import yaml

from tabulate import tabulate

from .error import CliError


def format_output(fmt: str, data):
    """Format data using particular formatter"""
    if fmt == 'yaml':
        return yaml.dump({'output': data}, indent=2)
    if fmt == 'raw':
        return str(data)
    if fmt == 'json':
        output = json.dumps({'output': data}, indent=2)
        return f"{output}\n" # FIXME figure out how to make platform-agnostic
    if fmt == 'table':
        if isinstance(data, str):
            data = [[data]]
        elif isinstance(data, list):
            data = {'output': data}
        output = tabulate(data, headers=['output'])
        return f"{output}\n" # FIXME figure out how to make platform-agnostic
    raise CliError(f"Unsupported output format: {fmt}")
