# dunkirk 🛥️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Export all your [Apple iCloud Notes](https://www.icloud.com/notes) on macOS to text files.

> Disclaimer: this is a sloppy adaptation of https://github.com/adamyi/notes_to_keep

## Installation
Recommended python version: `Python 2.7.15`

```
python setup.py build && python setup.py install && pip install dunkirk
```

## Usage
```
Usage:
    dunkirk [options]
    dunkirk --help
    dunkirk --version

Options:
    --num=<num>       The number of notes to be exported to text files
                      (default: all notes will be exported)
```

Notes export will then be in a `temporary_export/` folder.


## Acknowledgements

This repo is my sloppy and python n00b adaptation of https://github.com/adamyi/notes_to_keep, and was only possible thanks to the hard work of [Adam Yi (@adamyi)](https://github.com/adamyi).

## Contribute

I have few knowledge in python, so I welcome any pull requests or issues.

## Disclaimer

This is not an official Apple product. It is not endorsed nor supported by Apple Inc.

## License

Copyright 2018 Filipe Freire

[MIT License](LICENSE)
