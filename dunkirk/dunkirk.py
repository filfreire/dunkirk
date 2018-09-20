#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dunkirk - export all your Apple Notes to txt files

Usage:
    dunkirk [options]
    dunkirk --help
    dunkirk --version

Options:
    --num=<num>       The number of notes to be exported to Google
                      Keep (default: all notes will be exported)
"""

import logging
from docopt import docopt
from scan_notes import ScanNotes
import textfile
from . import __version__

log = logging.getLogger("main")
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(name)s (%(lineno)s): %(message)s')
logging.root.setLevel(level=logging.INFO)

def start(args):
    # gaia = args['<email>']
    # password = args['<password>']
    num = args['--num']
    # pfx = args['--prefix']
    # no_time = args['--no-time']
    notes = ScanNotes()
    #gkeep.start(gaia, password, notes, num, pfx, no_time, True)
    textfile.start(notes, num)

def main():
    args = docopt(__doc__, version=__version__)
    start(args)


if __name__ == '__main__':
    main()
