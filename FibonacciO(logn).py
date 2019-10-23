# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:31:55 2018

@author: Mohamad
"""
#part a
print("A")

def recPowerSlow(x,n):
    if n==0:
        return 1
    elif n<0:
        return 1/(recPowerSlow(x,-n))
    else:
        return x*recPowerSlow(x,n-1)
        
print("recPowerSlow(0,0):",recPowerSlow(0,0))
print("recPowerSlow(0,3):",recPowerSlow(0,3))
print("recPowerSlow(3,0):",recPowerSlow(3,0))
print("recPowerSlow(3,1):",recPowerSlow(3,1))
print("recPowerSlow(-3,1):",recPowerSlow(-3,1))
print("recPowerSlow(2,4):",recPowerSlow(2,4))
print("recPowerSlow(2,-4):",recPowerSlow(2,-4))
x = 1.25
n = 82
print(x,"**",n," :",x**n)
print("recPower(",x,",",n,"):",recPowerSlow(x,n))

#part b
print("B")
def recPowerFast(x,n):
    if n==0:
        return 1
    elif n<0:
        return 1/recPowerFast(x,-n)
    elif n>0:
        if n%2==0:
            y=recPowerFast(x,n/2)
            return y*y
        else:
            z=recPowerFast(x,(n-1)/2)
            return x*z*z
   
        #return x*x**(n-1/)2*x**(n-1)/2
print("recPowerFast(0,0):",recPowerFast(0,0))
print("recPowerFast(0,3):",recPowerFast(0,3))
print("recPowerFast(3,0):",recPowerFast(3,0))
print("recPowerFast(3,1):",recPowerFast(3,1))
print("recPowerFast(-3,1):",recPowerFast(-3,1))
print("recPowerFast(2,4):",recPowerFast(2,4))
#print("recPowerFast(2,-4):",recPowerFast(2,-4))
x = 1.25
n = 82
print(x,"**",n," :",x**n)
print("recPower(",x,",",n,"):",recPowerFast(x,n))

#part c
print("C")
def multMatrices(A,B):
    """ A and B are tuples of tuples representing two 2 by 2 matrices"""
    C00 = A[0][0]*B[0][0]+A[0][1]*B[1][0]
    C01 = A[0][0]*B[0][1]+A[0][1]*B[1][1]
    C10 = A[1][0]*B[0][0]+A[1][1]*B[1][0]
    C11 = A[1][0]*B[0][1]+A[1][1]*B[1][1]
    C = ((C00, C01), (C10, C11))
    #This function multiplies two Matrices and returns the result
    return C
def fibMatrixVersion(n):
    if n==0:
        return 0
    m=recMatrixPowerFast(X,n)
    return m[0][1]
def recMatrixPowerFast(X,n):
        """ X is a tuple of tuple representing a 2 by 2 matrix and n is non-negative integer"""
        if n==1:
            return X
        elif n%2==0:
                y=recMatrixPowerFast(X,n/2)
                #x**4==(x**2)**2
                #We keep on dividing the power by 2 until we reach base case
                C=multMatrices(y,y)
                return C
        else:
                y=recMatrixPowerFast(X,(n-1)/2)
                #When the power is odd: x**5==((x**2)**2)*x
                C=multMatrices(y,y)
                Z=multMatrices(X,C)
                return Z
                
                
X=((1,1),(1,0))
for i in range(11):
    print("F_",i,":", fibMatrixVersion(i))
print("F_ 100 :", fibMatrixVersion(100))
    