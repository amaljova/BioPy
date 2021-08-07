# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""



#Fundamental Data of Genomics
#By Amal Joseph Varghese

#Deoxyribo nucleotides
Dnuc=("A", "T", "G", "C")
#Ribo nucleotides
Rnuc=("A", "U", "G", "C")
#Deoxyribo nucleotide Compliments
Dcomp = {'A' : 'T', 'T':'A', 'G': 'C', 'C': 'G'}
#Ribo nucleotide Compliments
Rcomp = {'A' : 'U', 'U':'A', 'G': 'C', 'C': 'G'}
#Purines and Pyrimidines
nucType={
    'A':'Purine',
    'G':'Purine',
    'C':'Pyrimidine',
    'T':'Pyrimidine',
    'U':'Pyrimidine'
}

Rtranslate = {
    #'AUG' = 'M'= Start Codon, 'UAA' = 'UAG'= 'UGA' = '|' = Stop codon

    "AAA": "K", "AAG": "K", "AAU": "N", "AAC": "N",    # AAN->K (if N= Purine) else N
    "AGA": "R", "AGG": "R", "AGU": "S", "AGC": "S",    # AGN->R (if N= Purine) else S
    "AUA": "I", "AUG": "M", "AUU": "I", "AUC": "I",    # AUN->I or M (if N==G) (if 3H ->M)
    "ACA": "T", "ACG": "T", "ACU": "T", "ACC": "T",    # ACN->T
    #=============================================#    
    "UAA": "|", "UAG": "|", "UAU": "Y", "UAC": "Y",    # UAN->| (if N= Purine) else Y
    "UGA": "|", "UGG": "W", "UGU": "C", "UGC": "C",    # UGN->C (if N= Pyrimidine) else (if 2H ->|) else (if 3H ->W)
    "UUA": "L", "UUG": "L", "UUU": "F", "UUC": "F",    # UUN->L (if N= Purine) else F
    "UCA": "S", "UCG": "S", "UCU": "S", "UCC": "S",    # UCN->S
    #=============================================#    
    "GAA": "E", "GAG": "E", "GAU": "D", "GAC": "D",    # GAN->E (if N= Purine) else D
    "GGA": "G", "GGG": "G", "GGU": "G", "GGC": "G",    # GGN->G
    "GUA": "V", "GUG": "V", "GUU": "V", "GUC": "V",    # GUN->V
    "GCA": "A", "GCG": "A", "GCU": "A", "GCC": "A",    # GCN->A
    #=============================================#    
    "CAA": "Q", "CAG": "Q", "CAU": "H", "CAC": "H",    # CAN->Q (if N= Purine) else H
    "CGA": "R", "CGG": "R", "CGU": "R", "CGC": "R",    # CGN->R
    "CUA": "L", "CUG": "L", "CUU": "L", "CUC": "L",    # CUN->L
    "CCA": "P", "CCG": "P", "CCU": "P", "CCC": "P"     # CCN->P
}

Dtranslate = {
    #'ATG' = 'M'= Start Codon, 'TAA' = 'TAG'= 'TGA' = '|' = Stop codon

    "AAA": "K", "AAG": "K", "AAT": "N", "AAC": "N",
    "AGA": "R", "AGG": "R", "AGT": "S", "AGC": "S",
    "ATA": "I", "ATG": "M", "ATT": "I", "ATC": "I",
    "ACA": "T", "ACG": "T", "ACT": "T", "ACC": "T",
    #=============================================#
    "TAA": "|", "TAG": "|", "TAT": "Y", "TAC": "Y",
    "TGA": "|", "TGG": "W", "TGT": "C", "TGC": "C",
    "TTA": "L", "TTG": "L", "TTT": "F", "TTC": "F",
    "TCA": "S", "TCG": "S", "TCT": "S", "TCC": "S",
    #=============================================#
    "GAA": "E", "GAG": "E", "GAT": "D", "GAC": "D",
    "GGA": "G", "GGG": "G", "GGT": "G", "GGC": "G",
    "GTA": "V", "GTG": "V", "GTT": "V", "GTC": "V",
    "GCA": "A", "GCG": "A", "GCT": "A", "GCC": "A",
    #=============================================#
    "CAA": "Q", "CAG": "Q", "CAT": "H", "CAC": "H",
    "CGA": "R", "CGG": "R", "CGT": "R", "CGC": "R",
    "CTA": "L", "CTG": "L", "CTT": "L", "CTC": "L",
    "CCA": "P", "CCG": "P", "CCT": "P", "CCC": "P"
}

reverseTranslate ={
    'M': ('AUG'),
    'W': ('UGG'),
    'Y': ('UAU', 'UAC'),
    'K': ('AAA', 'AAG'),
    'N': ('AAU', 'AAC'),
    'C': ('UGU', 'UGC'),
    'F': ('UUU', 'UUC'),
    'E': ('GAA', 'GAG'),
    'D': ('GAU', 'GAC'),
    'Q': ('CAA', 'CAG'),
    'H': ('CAU', 'CAC'),
    'I': ('AUA', 'AUU', 'AUC'),
    '|': ('UAA', 'UAG', 'UGA'),
    'T': ('ACA', 'ACG', 'ACU', 'ACC'),
    'G': ('GGA', 'GGG', 'GGU', 'GGC'),
    'V': ('GUA', 'GUG', 'GUU', 'GUC'),
    'A': ('GCA', 'GCG', 'GCU', 'GCC'),
    'P': ('CCA', 'CCG', 'CCU', 'CCC'),
    'L': ('UUA', 'UUG', 'CUA', 'CUG', 'CUU', 'CUC'),
    'R': ('AGA', 'AGG', 'CGA', 'CGG', 'CGU', 'CGC'),
    'S': ('AGU', 'AGC', 'UCA', 'UCG', 'UCU', 'UCC')
    
}


