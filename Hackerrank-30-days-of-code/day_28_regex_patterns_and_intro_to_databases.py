#!/bin/python3

import re


if __name__ == '__main__':
    N = int(input())
    regex = r".*@gmail\.com"
    re.compile(regex)
    names = []
    for i in range(N):
        name, email = [str(i) for i in input().split()]
        if re.match(regex, email):
            names.append(name)
    names.sort()
    for _name in names:
        print(_name)
