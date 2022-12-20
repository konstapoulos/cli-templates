#!/usr/bin/env python3

"""Sample CLI tool written in python3


Usage:
  ./cli_sample.py [options] (-s <string> | -f <file> | -u <url>)
  ./cli_sample.py (-h | --help)

Options:
  -s, --string <string>        input data as a command line literal
  -f, --file <file>            input data from a file
  -u, --url <url>              input data to fetch from URL
  -o, --output <file>          output file [default: stdout]
  --format <format>            output format: table, json, yaml [default: table]
  --loglevel <level>           logging level to use (debug, info, warning,
                                  error, critical) [default: info]
  --logfile <file>             direct logging messages to file [default: stdout]
  -h, --help                   show this screen

Examples:

  # process string
  ./cli_sample.py --string 'hello world'

  # process list of names from file 'names.txt'
  ./cli_sample.py -f names.txt 

  # fetch data from url and process it; verbose logging
  ./cli_sample.py --loglevel debug -u https://httpbin.org/json
"""

# more docopt examples:
# https://github.com/docopt/docopt/tree/master/examples

import logging

from docopt import docopt

from helpers.error import CliError
from helpers.file import process_file
from helpers.format import format_output
from helpers.log import setup_logging
from helpers.string import process_string
from helpers.url import process_url


def main(arguments):
    """Main entry point"""

    logging.debug(arguments)

    data = None

    string = arguments['--string']
    if string:
        data = process_string(string)

    file = arguments['--file']
    if file:
        data = process_file(file)

    url = arguments['--url']
    if url:
        data = process_url(url)

    print(format_output(arguments['--format'], data))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Sample CLI tool')
    setup_logging(arguments['--loglevel'], arguments['--logfile'])
    try:
        main(arguments)
    except CliError as err:
        logging.error(err)
