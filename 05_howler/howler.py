#!/usr/bin/env python3
"""
Author : yaroslavoliinyk <yaroslavoliinyk@localhost>
Date   : 2022-11-28
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    output = args.outfile

    content = open(text).read() if os.path.isfile(text) else text
    content = content.upper()

    if output:
        # Solution 1
        # out_wh = open(output, 'wt')
        # out_wh.write(content)
        # out_wh.close()
        # Solution 2
        out_wh = open(output, "wt")
        print(content, file=out_wh)
    else:
        print(content)


# --------------------------------------------------
if __name__ == '__main__':
    main()
