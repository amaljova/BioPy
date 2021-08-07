# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""

#A comprihensive python module for genomic amnalysis

import GenData
import random
from collections import Counter

def randDNA(length):
    '''Generates a Random DNA sequence of given length'''
    return ''.join(random.choice(GenData.Dnuc) for n in range(length))


def randRNA(length):
    '''Generates a Random RNA sequence of given length'''
    return ''.join(random.choice(GenData.Rnuc) for n in range(length))


def countNuc(seq):
    '''Count nucleotides in a given sequence. Return a dictionary'''
    return dict(Counter(seq))


def transcribe(seq):
    '''DNA -> RNA Transcription. Replacing Thymine with Uracil'''
    return seq.replace("T", "U")

def reverseComp(seq):
    ''' Swapping adenine with thymine and guanine with cytosine.
    Reversing newly generated string'''
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

def countGC(seq):
    '''GC Content in a DNA/RNA sequence'''
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def translate(seq, start=0):
    '''Translates  RNA sequence into an aminoacid sequence'''
    return [GenData.Rtranslate[seq[pos:pos + 3]] for pos in range(start, len(seq) - 2, 3)]

