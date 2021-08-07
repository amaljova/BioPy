# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""



def BMI(kg, cm):
	m=cm/100
	return(kg/m**2)

def checkmass(bmi):
	return("obase" if (bmi > 25) else "normal" if (25>bmi>18) else "feeble", bmi)


