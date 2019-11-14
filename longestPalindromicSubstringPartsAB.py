# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:09:12 2018

@author: Mohamad
"""



## a) Using slicing
def longestPalSubsA(s):
   n = len(s)
   start = 0
   end  = -1 # to account for empty string 
   maxLength = 0
   for i in range(n):
       for j in range(i,n):
           t = s[i:j+1]
           tLength = len(t)
           if t==t[::-1] and tLength>=maxLength:
               start = i
               end = j
               maxLength = tLength
   return s[start:end+1]
               
               
print("Part (a)")
print(longestPalSubsA("aceexcivicgrfdds"))
print(longestPalSubsA("civicgrfdds"))
print(longestPalSubsA("aceexcivic"))
print(longestPalSubsA("civic"))
print(longestPalSubsA("123abba1"))
print(longestPalSubsA("abba1"))
print(longestPalSubsA("123abba"))
print(longestPalSubsA("12345"))
print(longestPalSubsA(""))


### b)  Without slicing except for at return, three nested loops 
def isSubsequencePalindrome(s,start,end):
    if start == end: 
        return True 
    else:
        palindrome = True
        i = start
        j = end
        while i<=j: 
            if s[i]!=s[j]:
                palindrome  = False
                break
            i+=1
            j-=1
        return  palindrome
  
     
def longestPalSubsB(s):
   n = len(s)
   start = 0
   end  = -1 # to account for empty string 
   maxLength = 0
   for i in range(n):
       for j in range(i,n):
           tLength = j-i+1
           if isSubsequencePalindrome(s,i,j) and tLength>=maxLength:
               start = i
               end = j
               maxLength = tLength
   return s[start:end+1]

print("Part (b)")
print(longestPalSubsB("aceexcivicgrfdds"))
print(longestPalSubsB("civicgrfdds"))
print(longestPalSubsB("aceexcivic"))
print(longestPalSubsB("civic"))
print(longestPalSubsB("123abba1"))
print(longestPalSubsB("abba1"))
print(longestPalSubsB("123abba"))
print(longestPalSubsB("12345"))
print(longestPalSubsB(""))

