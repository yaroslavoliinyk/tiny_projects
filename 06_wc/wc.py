#!/usr/bin/env python3
"""
Author : yaroslavoliinyk <yaroslavoliinyk@localhost>
Date   : 2022-11-28
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    parser.add_argument('-w',
                        '--word',
                        help='Number of words',
                        action='store_true')

    parser.add_argument('-l',
                        '--line',
                        help='Number of lines',
                        action='store_true')

    parser.add_argument('-c',
                        '--character',
                        help='Number of bytes',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.file
    word = args.word
    line_ = args.line
    character = args.character
    arg_set = word or line_ or character

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for file_handle in files:
        lines = 0
        words = 0
        length = 0
        output = ''
        for line in file_handle:
            lines += 1
            words += len(line.split())
            length += len(line)
        output += f'{lines:8}' if line_ or not arg_set else ''
        output += f'{words:8}' if word or not arg_set else ''
        output += f'{length:8}' if character or not arg_set else ''
        print(f'{output} {file_handle.name}')
        total_lines += lines
        total_words += words
        total_bytes += length

    if (len(files) > 1):
        output = ''
        output += f'{total_lines:8}' if line_ or not arg_set else ''
        output += f'{total_words:8}' if word or not arg_set else ''
        output += f'{total_bytes:8}' if character or not arg_set else ''
        output += ' total'
        print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
