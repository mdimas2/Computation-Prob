# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:10:22 2018

@author: Mohamad
"""
def LongestPalSubA(L):
    lengh=0
    lengh_max=0
    for i in range(len(L)):
        for j in range(i,len(L)-1):
            if L[i:j]==L[j:i:-1]:
                lengh=j-i
                if lengh>lengh_max:
                    lengh_max=lengh
                    start=i
                    end=j
                
    return L[start:end+1]
def LongestPalSubB(L):
    lengh=0
    maxlengh=0
    start=0
    end=0
    for k in range(len(L)):
        for j in range(k,len(L)-1):
            a=0
            for i in range(k,j):
                if L[i]!=L[j-a]:  
                    lengh=0
                    maxlengh=0
                    break
                else:
                    lengh=j-k
                    a+=1
                if lengh>maxlengh:
                    maxlengh=lengh
            if maxlengh>(end-start) :
                start=k
                end=j
                
    return L[start:end+1]
def LongestPalSubC(L):
    a=0
    end=0
    start=0
    lengh=0
    maxlengh=0
    n=len(L)
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[i]!=L[n-1-j]:
                lengh=0
                maxlengh=0
            else:
                lengh=n-1-j
                a+=1
            if lengh>maxlengh:
                maxlengh=lengh
        if maxlengh>(end-start):
            start=i
            end=j
    return(L[start:end+1])
        
                
            
            
s=input("Please enter list separated by spaces: ")
L=s.split()
y=LongestPalSubA(L)
print(y)
z=LongestPalSubB(L)
print(z)
x=LongestPalSubC(L)
print(x)

