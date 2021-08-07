#! /usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""

#Single and Triple letter codes tuples

amino_acids = (
    'Alanine', #0
    'Arginine', #1
    'Asparagine', #2
    'Aspartic_Acid', #3
    'Cysteine', #4
    'Glutamine', #5
    'Glutamic_Acid', #6
    'Glycine', #7
    'Histidine', #8
    'Isoleucine', #9
    'Leucine', #10
    'Lysine', #11
    'Methionine', #12
    'Phenylalaninie', #13
    'Proline', #14
    'Serine', #15
    'Threonine', #16
    'Tryptophan', #17
    'Tyrosine', #18
    'Valine', #19
    'Asparagine/Aspartic_Acid', #20
    'Glutamine/Glutamic_Acid' #21
)

#Triple Code
triple_code = (
    'Ala', #0
    'Arg', #1
    'Asn', #2
    'Asp', #3
    'Cys', #4
    'Gln', #5
    'Glu', #6
    'Gly', #7
    'His', #8
    'Ile', #9
    'Leu', #10
    'Lys', #11
    'Met', #12
    'Phe', #13
    'Pro', #14
    'Ser', #15
    'Thr', #16
    'Trp', #17
    'Tyr', #18
    'Val', #19
    'Asx', #20
    'Glx' #21
)
#Single Code
single_code = (
    'A', #0                 ==========ali nonpolar===================
    'R', #1                 ++++++++++basic(+ve) (2Amine) (3 N atoms)
    'N', #2                 ~~~~~~~~~~polar neutral (C(=O)NH2)~~~~~~~
    'D', #3                 ----------acidic(-ve) (-COOH)------------
    'C', #4                 ~~~~~~~~~~polar neutral (-SH)~~~~~~~~~~~~
    'Q', #5                 ~~~~~~~~~~polar neutral (C(=O)NH2)~~~~~~~
    'E', #6                 ----------acidic(-ve) (-COOH)------------
    'G', #7                 ==========ali nonpolar===================
    'H', #8                 ++++++++++basic(+ve) (2Amine) (3 N atoms)
    'I', #9                 ==========ali nonpolar===================
    'L', #10                ==========ali nonpolar===================
    'K', #11                ++++++++++basic(+ve) (-NH3 Amine) (2 N atoms)
    'M', #12                ==========ali nonpolar (r-S-r)===========
    'F', #13                aro nonpolar  (alanine+phenyl)
    'P', #14                ??? ali polar neutral ????????
    'S', #15                ~~~~~~~~~~polar neutral (-OH)~~~~~~~~~~~~
    'T', #16                ~~~~~~~~~~polar neutral (-OH)~~~~~~~~~~~~
    'W', #17                aro nonpolar  (alanine+phenyl)
    'Y', #18                aro nonpolar  (alanine+phenol)
    'V', #19                ==========ali nonpolar===================
    'B', #20                
    'Z' #21             
)

def to_sinle(AA):
    try:
        try:
            return single_code[amino_acids.index(AA)]
        except:
            return single_code[triple_code.index(AA)]
    except:
         return("Invalid Input")

def to_triple(AA):
    try:
        try:
            return triple_code[amino_acids.index(AA)]
        except:
            return triple_code[single_code.index(AA)]
    except:
        return("Invalid Input")
def to_amino(AA):
    try:
        try:
            return amino_acids[single_code.index(AA)]
        except:
            return amino_acids[triple_code.index(AA)]
    except:return("Invalid Input")


    
Aliphatic = (0, 7, 9, 10, 14, 19) #contain long hydrocarbon sidechin
Aromatic = (13, 17, 18) #contain ring shaped sidechain
Acidic = (3, 6, 20, 21) #(-COOH)
Basic = (1,8, 11)
Hydroxylic = (15, 16) #contain hydroxyl group (-OH)
Sulphur_containing = (4, 12)
Amidic = (2, 5, 20, 21) #containing amide group (C(=O)NH2)

hydrophobic = (0, 7, 9, 10, 14, 19, 12, 13, 17) #nine
polar = (2, 4, 5, 15, 16, 18, 20, 21) #six (Asx and Glx are exceptional)