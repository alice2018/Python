# -*- coding: cp936 -*-

arr =[10,15,20,40,10]
print arr 

def maximun(arr):  
    for i in range(0,len(arr)):  
        for j in range(i+1,len(arr)):  
            first=int(arr[i])  
            second=int(arr[j])  
            if first < second:  
               arr[i]=arr[j]  
               arr[j]=first  
    print "Maximun =",arr[0]  
  
maximun(arr)  
