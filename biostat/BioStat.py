# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@ email: amaljova@gmail.com

"""

#The best way to learn statistics is to code!!!!


#measure of central tendancy (Mean, Median, Mode)
def mean(arr):
    return sum(arr)/len(arr)


#Varience and Standard Deviation
#SD = squareroot(Varience)
def varience(arr):
    mean = sum(arr)/len(arr)
    diff=[]
    for i in arr:
        diff.append((i-mean)**2)
    return sum(diff)/len(diff)



#Normalization
#1 Min-Max Normaliztion

def min_max_norm(X_list):
    X_min = min(X_list)
    X_max = max(X_list)
    X_norm_list =[]
    for X in X_list:
        X_norm =(X - X_min)/(X_max - X_min)
        X_norm_list.append(X_norm)
    return X_norm_list


#Standardization


def Z(x):
    #Z score normalization
    #Here all features will have the property of mean = 0 and sd = 1
    return (x-mean(x))/varience(x)**(1/2)

#

a = [1,2,3,4,5,6,7,8,9]
print(varience(a), mean(a))

