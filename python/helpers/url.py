"""
Helper functions for URL fetching
"""

import requests

from .error import CliError


def process_url(url: str) -> str:
    """Process url"""
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        raise CliError from err
