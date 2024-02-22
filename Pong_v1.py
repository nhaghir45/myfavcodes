#pong*p/
##########################################################################################################################
from graphics import *
import time
score_left=0
score_right=0
fc=int(input(" do you want a filled circle 1 for yes 0 no"))
#if fc>=1:
    #warning
    #print (" eplilepsy warning")
r=int(input("radius? "))
it=int(input("1  log or 0 no log"))
print("w,s for player 1 and up key, down key for player 2")
if it==1:
    qwerty=int(input("how much dely do you want before next ping"))

# making the title/screen
displayArea=GraphWin('Pong', 1000, 750)

y = 375
x = 500
#setting how much the ball move by
step_x = 5
step_y = 5
step_r = 5

x_pad_Left=50
y_pad_Left=500

x_pad_Right=950
y_pad_Right=500
# paddle size

pad_height=100
pad_width=5

oo=0

# infinte loop
while (True):
   
    if(oo==0):
        tx=Text(Point(500,375),"Press space to start")
        tx.draw(displayArea)
        tx.setFace("courier")
        oo=1
    b=displayArea.checkKey()
    print (b)
    if b=="space":
        line=Line(Point(500,0), Point(500,750))
        line.draw(displayArea)
        while(True):
              
            
            
            for item in displayArea.items[:]:  #[circle, line]
                if(item != line):
                    item.undraw()
                    
            displayArea.update()
            if it==1:
                while (True):
                    time.sleep (qwerty)
                    print (item)
                
            print(item)
            # selcets everyting and Undrawing the preives frame

            text1=Text(Point(400,50),str(score_left))
            text2=Text(Point(600,50),str(score_right))
            text1.draw(displayArea)
            text2.draw(displayArea)

            #line=Line(Point(500,0), Point(500,750))
            #line.draw(displayArea)
            

            cir= Circle(Point(x,y), r)
            cir.setOutline("red")
            cir.setWidth(5)
            cir.draw(displayArea)

            #fill the circle if picked 1
            if fc>=1:
                cir.setFill("red")
                #i=0
                #while r>=i:
                      #cir= Circle(Point(x,y), i)
                      #cir.setOutline("black")
                      #cir.draw(displayArea)       
                      #i=i+1
        #making paddles 
            
            rec=Rectangle(Point(x_pad_Left,y_pad_Left),Point(x_pad_Left+pad_width,y_pad_Left+pad_height))
            rec.draw(displayArea)
            rec.setFill("black")
            rec2=Rectangle(Point(x_pad_Right,y_pad_Right),Point(x_pad_Right+pad_width,y_pad_Right+pad_height))
            rec2.draw(displayArea)
            rec2.setFill("black")

            # if keys w,s,down,up was press limated paddle from flying away from screen

            k=displayArea.checkKey()

            if k=="w":
                if y_pad_Left - 6*abs(step_y) >=0:
                    y_pad_Left = y_pad_Left - 6*abs(step_y);
                
            if k=="s":
                if y_pad_Left + 6*abs(step_y) + pad_height<=750:
                    y_pad_Left = y_pad_Left + 6*abs(step_y);
                    
            if k=="W":
                if y_pad_Left - 6*abs(step_y) >=0:
                    y_pad_Left = y_pad_Left - 6*abs(step_y);
            if k=="S":
                if y_pad_Left + 6*abs(step_y)  + pad_height<=750:
                    y_pad_Left = y_pad_Left + 6*abs(step_y);
                
            if k=="Up":
                if y_pad_Right - 6*abs(step_y) >=0:
                    y_pad_Right = y_pad_Right - 6*abs(step_y);
                
            if k=="Down":
                if y_pad_Right + 6*abs(step_y) + pad_height <=750:
                    y_pad_Right = y_pad_Right + 6*abs(step_y);
                    


            # chek for bounse of the wall

            if (x-r+step_x <0):
                score_left=score_left-1

            if ( x + step_x + r > 1000):
                score_right=score_right-1
            
                  
            if ( x + step_x + r > 1000 or x-r+step_x <0):
               step_x = step_x * (-1)
            if (y+ step_y + r> 750 or y-r+step_y<0):
                step_y=step_y* (-1)
                
        # chek if it bounse from paddle
                
            if (x+step_x+r>=x_pad_Right and x+r<=x_pad_Right and y>= y_pad_Right - r and y<= y_pad_Right+pad_height+r):
                score_right=score_right+1
                step_x=step_x*-1
                
            if (x+step_x-r<=x_pad_Left+pad_width and x-r>=x_pad_Left+pad_width and y>= y_pad_Left - r and y<= y_pad_Left+pad_height+r):
                step_x=step_x*-1
                score_left=score_left+1

                
               # changing r_step if pressed 1
            if ( r>=200 or r<=0): 
                step_r = step_r * (-1)




            x = x + step_x
            #r=r+step_r
            y=y+step_y
            
            time.sleep(0.00001)
        break
        
