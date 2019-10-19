# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:56:53 2018

@author: Mohamad
"""
print("A")
def LenOfLISEndingWithGivenIndexRec(L,i):
    if i==0:
        return 1
    maxlen = 1
    for j in range(i,-1,-1):
        if L[j]<L[i]:
            length=1+LenOfLISEndingWithGivenIndexRec(L,j)            
            if length>maxlen:
                maxlen=length
    return maxlen
                                                    
L = [1, 4, 1, 5, 7, 10, 20, 3, 50, 1]
for i in range(len(L)):
    print(LenOfLISEndingWithGivenIndexRec([1, 4, 1, 5, 7, 10, 20, 3, 50, 1],i), end = " ")
    
print()
print("B")
def LISLen(P):
    def LenOfLISEndingWithGivenIndexRecMemoized(L,i):
        if i==0:
            return 1
        maxlen = 1
        for j in range(i,-1,-1):
            if L[j]<L[i]:
                length=1+LenOfLISEndingWithGivenIndexRec(L,j)            
                if length>maxlen:
                    maxlen=length
        C[i]=maxlen
        return maxlen
    n=len(P)
    C=[-1]*n
    for i in range (n):
        LenOfLISEndingWithGivenIndexRecMemoized(P,i)
    return max(C)

print(LISLen([1, 2, 10, 5, 2, 7]))
print(LISLen([1, 4, 1, 5, 7, 10, 20, 3, 50, 1]))
print(LISLen([10, 9, 5, 7, 10, 20]))
print(LISLen([10, 3, 2, 1]))
        













