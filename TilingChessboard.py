# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:29:08 2018

@author: Mohamad
"""
import numpy
def printMatrix(M,name=""):
    if name!="":print(name)
    print(numpy.matrix(M))
def tileDefectiveChessBoard(n,i,j): # Wrapper function
    m = n
    while m%2 ==0:
        m=m//2
    assert m==1 and 0<=i<=n-1 and 0<=j<=n-1, "Bad Input"
    A = [[1 for v in range(n)] for u in range(n)]
    A[j][i] = 0
    
    return tileDefectiveChessBoardRec(A,1,0,len(A)-1,0,len(A)-1,i,j)
    
def tileDefectiveChessBoardRec(A,tileIndex,startX,endX,startY,endY,i,j):
    global k
    k+=1
    if endX==startX and startY==endY:
        return A
    
    if (endX-startX+1)==2 and (endY-startY+1)==2 :
        if j==startY:
            if i==startX:
                A[j][i+1]=k
                A[j+1][i]=k
                A[j+1][i+1]=k
            else:
                A[j+1][i]=k
                A[j][i-1]=k
                A[j+1][i-1]=k
        else:
            if i==startX:
                A[j][i+1]=k
                A[j-1][i]=k
                A[j-1][i+1]=k
            else:
                A[j-1][i]=k
                A[j-1][i-1]=k
                A[j][i-1]=k
        return A
    
    
    elif (endX-startX+1)>=4 and (endY-startY+1)>=4:
        midi=(endX+startX+1)//2
        midj=(endY+startY+1)//2
        
        if startX<=i<midi and startY<=j<midj:
            
            A[midj][midi]=k
            A[midj-1][midi]=k
            A[midj][midi-1]=k
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,startY,midj-1,i,j)
            i=midi
            j=midj
            if j+1<len(A) and i+1<len(A):            
                tileDefectiveChessBoardRec(A,k,midi,endX,midj,endY,i,j)
            i=midi
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,startY,midj-1,i,j)
            i=midi-1
            j=midj
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,midj,endY,i,j)
        elif startX<=i<midi and j>=midj:
        
            A[midj][midi]=k
            A[midj-1][midi-1]=k
            A[midj-1][midi]=k
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,midj,endY,i,j)
            i=midi
            j=midj
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,midj,endY,i,j)
            i=midi-1
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,startY,midj-1,i,j)
            i=midi
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,startY,midj-1,i,j)
            
        elif i>=midi and startY<=j<midj:         
            A[midj][midi]=k
            A[midj][midi-1]=k
            A[midj-1][midi-1]=k
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,startY,midj-1,i,j)
            i=midi
            j=midj
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,midj,endY,i,j)
            i=midi-1
            j=midj
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,midj,endY,i,j)
            i=midi-1
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,startY,midj-1,i,j)
        elif i>=midi and j>=midj:
            
            A[midj-1][midi]=k
            A[midj][midi-1]=k
            A[midj-1][midi-1]=k
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endY,midj,endY,i,j)
            i=midi
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,midi,endX,startY,midj-1,i,j)
            i=midi-1
            j=midj
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,midj,endY,i,j)
            i=midi-1
            j=midj-1
            if j+1<len(A) and i+1<len(A):
                tileDefectiveChessBoardRec(A,k,startX,midi-1,startY,midj-1,i,j)
    return A   
            
            
            
for (n,i,j) in ((1,0,0),(2,0,0),(2,0,1),(2,1,1),(4,0,0),(8,0,0),(8,2,4)):
    k=0
    print("\ntileDefectiveChessBoard("+str(n)+","+str(i)+","+str(j)+")")
    A = tileDefectiveChessBoard(n,i,j)
    printMatrix(A)
