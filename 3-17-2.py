# -*- coding: cp936 -*-


def isPrime(num):
    i=2
    while(i<num):
        if (0== num%i):
            return False
            break
        else:
            i=i+1
    return True


N= int(raw_input("please input a number N: "))
print "质数为 :"

total = 0
for j in range(1, N+1):
    if j == 1:
        continue
    elif isPrime(j):
        print j
    else:
        total += 1
print "合计为 ：",N-total-1   
    
        
    

