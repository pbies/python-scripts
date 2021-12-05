#!/usr/bin/env python3

import sys


def main():
    o = open('output.txt', 'w')

    for i in range(1000001):
        o.write(str(i) + "\n")


if __name__ == '__main__':
    main()
