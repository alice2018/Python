# -*- coding: cp936 -*-


n = int(input("please input n( > 0) :"))
def factorial(n):
    j = 1
    for i in range(1,n+1):
        j = j*i
    print "n! =",j

factorial(n)
