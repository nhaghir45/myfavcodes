from graphics import *
import copy 
wrd=input("what is the word (*op):")
life=int(input("how much lifes"))
#depcopyyyyyyyyyyyyyy
life_old = copy.deepcopy(life)
#score=0
#########################################################################
#displaing title screen
#displayArea=GraphWin('hangman', 1000, 750)

for i in range (999):
    print("\n")
    print("  ")



ans=""
for i in wrd:
    if i == " ":
        ans = ans + " "
    else:
        ans=ans+"-"
    ########################
        #gussing input
while (life>=1 and ans!=wrd):
    gss=input("what are you guessing?: ")
    c=0
    flag=0
    for i in wrd:
        if gss==i:
            temp_ans=list(ans)
            temp_ans[c]=gss
            ans="".join(temp_ans)
            flag=1
        c=c+1

        

    if flag==0:
        life=life-1
            
            
       
    print(ans)
if life <=0:
    print ("the word was... : ",wrd)
    print ("you had...")
    print(life)
    print ("amount of life(s) reming")
    print ("and you had:")
    print(life_old)
    print ("life(s) at the beginng")
    print("GAME OVER")
    if life_old<=0:
       
        print ("value is",life_old)
        raise Exception ("value is invalid A.K.A nobody can play properly please check your specific value or check the value above:")
        
    
    



