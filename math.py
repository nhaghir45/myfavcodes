import math
import time
from timeit import default_timer as timer
start = timer()

a=float(input("enter your firt number"))
A=float(input("sec num"))
symb = input("The operation you want to do (+,-,x,/,%,sqrt, ^2, random, counter,temp): ")
if symb=="+":
    print (a+A)
if symb=="-":
    print (a-A)
if symb=="x":
    print (a*A)
if symb=="/":
    print (a/A)
if symb=="%":
    print (a*100/A,"%")
if symb=="sqrt":
    print (math.sqrt(a))
if symb=="^2":
    print (a ** 2) # = a * a
if symb=="random":
    print ("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ")

    if symb=="counter":
        a=int(input("how much do you want to count to"))

        for i in range (a):
                i=1
                i=i+1
                print (i)





if symb=="temp":
    a=int(input("enter tep number in the firt unit"))
    a1=input("enter the unit (C/F/K):   ")
    a2=input("enter the  conversion unit (C/F/K):   ")

    if a1=="C":
        if a2=="F":
            print (a*9/5+32)
        elif a2=="K":
                    print (a+273.15)
        

        
    if a1=="F":
        if a2=="C":
            print ((a-32)*5/9) 
    elif a2=="F":
        print ((a-32)*5/9+273.15)
        

        
    if a1=="K":
        if a2=="C":
            print (a-273.15)
        elif a2=="F":
            print ((a-273.15)*9/5+32)

        











finish = timer()
print((finish - start))#*1000000000"))

    
    
#x*y
#xy
#2x

#x + y =10

#x + y -y = 10 - y
#---------------------------
#x = 10 - y
#-------------------------
#y=5 --->   x = 5
#y = 2 ---? x = 8
