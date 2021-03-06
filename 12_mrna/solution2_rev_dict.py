#!/usr/bin/env python3
""" Infer mRNA from Protein """

import argparse
import os
from functools import reduce
from typing import List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    protein: str
    modulo: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Infer mRNA from Protein',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='protein',
                        type=str,
                        help='Input protein or file')

    parser.add_argument('-m',
                        '--modulo',
                        metavar='int',
                        type=int,
                        default=1000000,
                        help='Modulo value')

    args = parser.parse_args()

    if os.path.isfile(args.protein):
        args.protein = open(args.protein).read().rstrip()

    return Args(args.protein, args.modulo)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    aa_to_codon = {
        'A': ['GCA', 'GCC', 'GCG', 'GCU'],
        'C': ['UGC', 'UGU'],
        'D': ['GAC', 'GAU'],
        'E': ['GAA', 'GAG'],
        'F': ['UUC', 'UUU'],
        'G': ['GGA', 'GGC', 'GGG', 'GGU'],
        'H': ['CAC', 'CAU'],
        'I': ['AUA', 'AUC', 'AUU'],
        'K': ['AAA', 'AAG'],
        'L': ['CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
        'M': ['AUG'],
        'N': ['AAC', 'AAU'],
        'P': ['CCA', 'CCC', 'CCG', 'CCU'],
        'Q': ['CAA', 'CAG'],
        'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
        'S': ['AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
        'T': ['ACA', 'ACC', 'ACG', 'ACU'],
        'V': ['GUA', 'GUC', 'GUG', 'GUU'],
        'W': ['UGG'],
        'Y': ['UAC', 'UAU'],
        '*': ['UAA', 'UAG', 'UGA'],
    }

    possible = [len(aa_to_codon[aa]) for aa in args.protein + '*']
    print(product(possible) % args.modulo)


# --------------------------------------------------
def product(xs: List[int]) -> int:
    """ Return the product """

    return reduce(lambda x, y: x * y, xs, 1)


# --------------------------------------------------
def test_product() -> None:
    """ Test product """

    assert product([]) == 1
    assert product([4]) == 4
    assert product([1, 2, 3, 4]) == 24


# --------------------------------------------------
if __name__ == '__main__':
    main()
