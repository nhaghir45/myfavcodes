a=int(input (" what is the current year "))
b=int(input(" what year have you been born "))
c=input ("In what format do you want your age: (s/min/hr/d/w/mo/y)?")
age= (a-b)
if (c=="y"):
    print (" your age in years is :   ",age)
elif (c=="mo"):    # elif : is else if
    print (" your age in months is :   ",age*12)
elif (c=="w"):    # elif : is else if
    print (" your age in weeks is :   ",age*12*4)
elif (c=="d"):    # elif : is else if
    print (" your age in days is :   ",age*12*4*7)
elif (c=="hr"):    # elif : is else if
    print (" your age in hours is :   ",age*12*4*7*24)
elif (c=="min"):    # elif : is else if
    print (" your age in minutes is :   ",age*12*4*7*24*60)
elif (c=="s"):    # elif : is else if
    print (" your age in seconds is :   ",age*12*4*7*24*60*60)
