#!/usr/bin/env python

import argparse, math

def main():
    parser = argparse.ArgumentParser(description="Calculate standard deviation")
    parser.add_argument('filename')

    args = parser.parse_args()

    dataset = open(args.filename).readlines()
    dataset = map(float, dataset)

    # get mean (average)
    avg = float(sum(dataset) / len(dataset))

    print "Mean: " + str(avg)

    # get each value's difference from mean
    diffmeans = []
    for x in dataset:
        diffmeans.append((x-avg)**2)

    # get the mean of those values
    dm_avg = float(sum(diffmeans) / len(diffmeans))

    # take the square root
    stddev = math.sqrt(dm_avg)

    print "1 Standard Deviation: " + str(stddev)
    
    normal = 0
    for x in dataset:
        if x-avg <= stddev:
            normal += 1
    
    print "Within 1 standard deviation: {0}%".format(
        float(float(normal) / len(dataset)) * 100)

    two = 0
    for x in dataset:
        if x-avg <= (2*stddev):
            two += 1

    print "Within 2 standard deviations: {0}%".format(
        float(float(two) / len(dataset)) * 100)

    three = 0
    for x in dataset:
        if x-avg <= (3*stddev):
            three += 1

    print "Within 3 standard deviations: {0}%".format(
        float(float(three) / len(dataset)) * 100)

if __name__=="__main__":
    main()
