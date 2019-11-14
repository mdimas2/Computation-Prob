# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:49:20 2018

@author: Mohamad
"""


def movedisks(n,start=1,destination=3,intermediate=2):
    if n>=2:
        movedisks(n-1,start,intermediate,destination)
    print("Move disks from",start,"to",destination)
    if n>=2:
        movedisks(n-1,intermediate,destination,start)
        
        
def towerHanoi(n,source1=1,source2=2,destination=4,intermediate=3):
    if n>=2:
         movedisks(n-1,source2,intermediate,destination)
    print("Move disks from",source2,"to",destination)  

    if n>=2:
       movedisks(n-1,source1,source2,destination)
    print("Move disks from",source1,"to",destination)
    if n>=2:
       towerHanoi(n-1,source2,intermediate,destination,source1)


print("a")
towerHanoi(3)
print("b")
towerHanoi(2)
print("c")
towerHanoi(1)

        
    
