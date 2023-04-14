#!/usr/bin/env python3
"""
Author : yaroslavoliinyk <yaroslavoliinyk@localhost>
Date   : 2022-11-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the 5',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text_number',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_number = args.text_number
    
    jump_dict = {str(key): str(value) for key, value in zip(range(1, 10), range(9, 0, -1))}
    jump_dict['5'] = '0'
    jump_dict['0'] = '5'

    ans = (jump_dict.get(c, c) for c in text_number)

    print(''.join(ans))


# --------------------------------------------------
if __name__ == '__main__':
    main()
