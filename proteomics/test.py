# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""


import ProtData

with open('insulin.txt', 'r') as f:
    insulin = f.read()

amino = []
for a in insulin:
    amino.append(protein.to_amino(a))

with open('amino.txt', 'w') as f:
    f.write(str(amino))

triple = []
for a in insulin:
    triple.append(protein.to_triple(a))

with open('triple.txt', 'w') as f:
    f.write(str(triple))