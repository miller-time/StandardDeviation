#!/usr/bin/env python

import argparse, math

def main():
    parser = argparse.ArgumentParser(description="Calculate standard deviation")
    parser.add_argument('filename')

    args = parser.parse_args()

    dataset = open(args.filename).readlines()
    dataset = map(float, dataset)

    avg = float(sum(dataset) / len(dataset))

    print "Average: " + str(avg)
    
if __name__=="__main__":
    main()
