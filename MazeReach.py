# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:27:15 2018

@author: Mohamad
"""
def twoDimListInit(m,n,val):
    L=[val]*m
    for i in range(m):
        L[i]=[val]*n
    return L
def mazeReachabeCells(M):
    m=len(M)
    n=(len(M[0]))
    R=twoDimListInit(m,n,0)
    
    for j in range(m):
        for i in range(n):
            if j==0 and i==0:
                R[0][0]=1
            elif j==0:
                if M[j][i]==1 and R[j][i-1]==1 :
                        R[j][i]==1
            elif i==0:
                    if M[j][i]==1 and R[j-1][i]==1:
                        R[j][i]=1
            else:
                if M[j][i]==1 and (R[j-1][i]==1 or R[j][i-1]==1 ):
                    R[j][i]=1
    return R


M=[[1,0,1], [1,1,1], [1,0,1]]
print(mazeReachabeCells(M))

