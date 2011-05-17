#!/usr/bin/env python

import random, argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a data file of N random numbers")
    parser.add_argument('N', type=int)
    
    args = parser.parse_args()

    random.seed(None)

    s = ''
    for i in range(args.N):
        s += str(random.randint(0,1000)) + '\n'

    open("randomdata.txt", "w").write(s)

if __name__=="__main__":
    main()
