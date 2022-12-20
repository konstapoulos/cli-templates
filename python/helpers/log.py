"""
Helper functions for logging
"""

import logging

from typing import Optional

from .error import CliError


def setup_logging(level: str = 'info', filename: Optional[str] = None) -> None:
    """Logging parameters"""
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise CliError('Invalid log level: f{level}')
    fmt = '%(levelname)s\t%(asctime)s %(message)s'
    if filename == 'stdout':
        filename = None
    logging.basicConfig(level=numeric_level, format=fmt, filename=filename)
