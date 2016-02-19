#!/bin/python

import argparse
import random as r

chars = "ABCDEFQWRTYUIOPSGHJKLZXVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*():{};'\".,/\\+_=-?№`~[]"

types = [chars.find('Q'), chars.find('q'), chars.find('1'), chars.find('!')]
sz = len(types)

parser = argparse.ArgumentParser(description='Simple Password Generator')
parser.add_argument('-t', '--type', type=int, dest='type', default=sz, help="Type is one of listed types of password:\n\t0 - Hex string\n\t1 - Only capital latin letters\n\t2 - Latin letters\n\t3 - Lattin letters and nums\n\t{} - All available chars".format(sz))
parser.add_argument('len', type=int, help="Password length")
parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', default=False, help="Quiet mode")

def gen(t, s):
    if t < 0 or t >= sz:
        if not isQuiet:
            print('Unknown pas type. Generating with all available...')
        t = sz - 1
    if s < 8:
        if not isQuiet:
            print('Can\'t generate passwords with length <8. Generating with min len...')
        s = 8
     
    string = []
    for i in range(0, s):
        string += chars[r.randrange(0, types[t])]
    return ''.join(string)

args = parser.parse_args()
isQuiet = args.quiet
print(gen(args.type, args.len))
