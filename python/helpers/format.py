"""
Helpers for producing output in different formats
"""

import json
import yaml

from tabulate import tabulate

from .error import CliError


def format_output(fmt: str, data):
    """Format data using particular formatter"""
    output = {'output': data}
    if fmt == 'json':
        return json.dumps(output, indent=2)
    if fmt == 'yaml':
        return yaml.dump(output)
    if fmt == 'table':
        if isinstance(data, str):
            data = [[data]]
        elif isinstance(data, list):
            data = {'data': data}
        return tabulate(data, headers=['output'])
    raise CliError(f"Unsupported output format: {fmt}")
