"""
File: refgene_to_bed.py
Author: Brant Faircloth

Created by Brant Faircloth on 06 December 2011 22:12 PST (-0800)
Copyright (c) 2011 Brant C. Faircloth. All rights reserved.

Description: convert UCSC refgene.txt files to BED format 

"""

import os
import sys
import numpy
import argparse

#import pdb


def get_args():
    parser = argparse.ArgumentParser(description="""Convert UCSC refgene.txt to BED
    format""")
    parser.add_argument('input', nargs='?', default=sys.stdin)
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()

def get_int_list(l):
    return [int(i) for i in l.strip(',').split(',')]

def get_string_list(a):
    return ','.join([str(i) for i in a.tolist()])

def main():
    args = get_args()
    for line in open(args.input, 'rU'):
        ls = line.strip().split('\t')
        starts, stops =  get_int_list(ls[9]), get_int_list(ls[10])
        lengths = get_string_list(numpy.array(stops) - numpy.array(starts))
        relstarts = get_string_list(numpy.array(starts) - int(ls[4]))
        outline = "{0}\t{1}\t{2}\t{3}\t999\t{4}\t{8}\t{9}\t0\t{5}\t{6}\t{7}\n".format(
                ls[2],
                ls[4],
                ls[5],
#                ls[1],
                ls[12],
                ls[3],
                ls[8],
                lengths,
                relstarts,
                ls[6],
                ls[7]
            )
        args.output.write(outline)
    args.output.close()

if __name__ == '__main__':
    main()
