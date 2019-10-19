# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:38:02 2018

@author: Mohamad
"""
print("A")
def minCoinChangeRec(L,t):
    if t<=0:
        return 0
    Rtmax=t
    for x in L:
        if x<=t:
            Rt=1+minCoinChangeRec(L,t-x)
            if Rt<Rtmax:
                Rtmax=Rt
    return Rtmax
L = [1,1,5]
for t in (10,1):
    Z=[]
    print("minCoinChangeRec(L,"+str(t)+"):",minCoinChangeRec(L,t))        
            
print("B")
def minCoinChange(L,t):
    def minCoinChangeRecMemoized(L,t,Sol):
        if t==0:
            return 0
        if Sol[t]!=-1:
            return Sol[t]        
        else:
            Rtmax=t
            for x in L:
                if x<=t:
                    Rt=1+minCoinChangeRecMemoized(L,t-x,Sol)
                    if Rt<Rtmax:
                        Rtmax=Rt
        Sol[t]=Rtmax
        return Rtmax
    Sol = [-1]*(t+1)
    return minCoinChangeRecMemoized(L,t,Sol)
    
L = [1,5,10,17,25]
for t in (0,1,15,24,25,26,27,28,29,34,100):
    print("minCoinChange(L,"+str(t)+"):",minCoinChange(L,t))

print("C")
def ExtendedMinCoinChangeRecMemoized(L,t,Sol,Aux):
        if t==0:
            return 0
        if Sol[t]!=-1:
            return Sol[t]        
        else:
            Rtmax=t
            for x in L:
                if x<=t:
                    Rt=1+ExtendedMinCoinChangeRecMemoized(L,t-x,Sol,Aux)
                    if Rt<=Rtmax:
                        Rtmax=Rt
                        Aux[t]=x
        Sol[t]=Rtmax
        return Rtmax
    
def findMinCoinChange(L,t):
    Sol=[-1]*(t+1)
    Aux=[0]*(t+1)
    minCoin=ExtendedMinCoinChangeRecMemoized(L,t,Sol,Aux)
    bestCut=[]
    m=t
    while m>0:
        i=Aux[m]
        bestCut.append(i)
        m=m-i
    return (minCoin,bestCut)

L = [1,5,10,17,25]
for t in (0,1,15,24,25,26,27,28,29,34,100):
    print("findMinCoinChange(L,"+str(t)+"):",findMinCoinChange(L,t))

        
        
    
    
    
