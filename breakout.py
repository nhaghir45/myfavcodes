from graphics import *
import time
###########################################################################################

# making the title/screen
size_height=750
size_width=1000
brick_h=40
brick_w=100

bricks_height = 0.5 * size_height
y = 575
x = 500
step_x = 5
step_y = 5
r=10
displayArea=GraphWin('atiri breckout', size_width, size_height)

# paddle size

x_pad=size_width/2
y_pad=size_height * 0.9


pad_height=20
pad_width=150

# score
score=0


#################################################################################################
bricks_xn=int(size_width/brick_w)
bricks_yn=int(size_height*0.4/brick_h)
brick_t = 0.15* size_height

#makineing arry
#array=[[0]*bricks_xn]*bricks_yn  **** wrong
array = [[0 for col in range(bricks_xn)] for row in range(bricks_yn)]

rec=[[]*bricks_yn]*bricks_xn 

print(array)


oo=0

# infinte loop
while (True):
   
    if(oo==0):
        tx=Text(Point(size_width/2,size_height/2),"Press space to start")
        tx.draw(displayArea)
        tx.setFace("courier")
        oo=1
    b=displayArea.checkKey()

    if b=="space":
        tx.undraw()
        for i in range (bricks_xn):
            for j in range (bricks_yn):
                rec2=Rectangle(Point(i*brick_w,brick_t + j * brick_h), Point(i*brick_w + brick_w,brick_t + j * brick_h + brick_h))
                rec2.draw(displayArea)
                rec2.setFill("blue")
                rec2.setOutline("red")
                    
        while(True):
            # creating ball
            
            cir= Circle(Point(x,y), r)
            cir.setOutline("red")
            cir.setWidth(5)
            cir.draw(displayArea)
            cir.setFill("red")


            #making paddle
            
            rec=Rectangle(Point(x_pad,y_pad),Point(x_pad+pad_width,y_pad+pad_height))
        
            rec.draw(displayArea)
            rec.setFill("black")
            
            k=displayArea.checkKey()

            if k=="Left":
                if x_pad - 6*abs(step_x) >=0:
                    x_pad = x_pad - 6*abs(step_x);
                
            if k=="Right":
                if x_pad + 6*abs(step_x) + pad_width <=size_width:
                    x_pad = x_pad + 6*abs(step_x);

             # chek for bounse of the wall
                  
            if ( x + step_x + r > size_width or x-r+step_x <0):
               step_x = step_x * (-1)
               
            if (y+ step_y + r> size_height):
                Game_Over=False
                
            if (y+ step_y + r> size_height or y-r+step_y<0):
                step_y=step_y* (-1)

                
                
        # chek if it bounse from paddle
                
            if (y+step_y+r>=y_pad and y+r<=y_pad and x>= x_pad - r and x<= x_pad+pad_width+r):
                step_y=step_y*-1

        #####################################################################################

        # chaeck if hit from bricks

            for i in range (bricks_yn):
                for j in  range (bricks_xn):
                    hit = 0
                    if array[i][j]==0:
                        #bottom hit
                        # i= row brick t= 
                        if (y+step_y-r<=brick_t + i* brick_h + brick_h  and y-r>= brick_t + i* brick_h + brick_h and x>= j*brick_w- r and x<= j*brick_w+brick_w+r):
                            step_y=step_y*-1
                            array[i][j]=1
                            rec2=Rectangle(Point(j*brick_w,brick_t + i * brick_h), Point(j*brick_w + brick_w,brick_t + i * brick_h + brick_h))
                            rec2.draw(displayArea)
                            rec2.setFill("yellow")
                            rec2.setOutline("red")

                            hit = 1
                            break

                        #top hit
                        if (y+step_y+r>=brick_t + i* brick_h   and y+r<= brick_t + i* brick_h  and x>= j*brick_w- r and x<= j*brick_w+brick_w+r):
                            step_y=step_y*-1
                            array[i][j]=1
                            rec2=Rectangle(Point(j*brick_w,brick_t + i * brick_h), Point(j*brick_w + brick_w,brick_t + i * brick_h + brick_h))
                            rec2.draw(displayArea)
                            rec2.setFill("yellow")
                            rec2.setOutline("red")

                            hit = 1
                            break

                        #left hit
                        if (x+step_x+r>=  j* brick_w   and x+r<= j* brick_w  and y>= brick_t+i*brick_h- r and y<= brick_t+i*brick_h+brick_h+r):
                            step_x=step_x*-1
                            array[i][j]=1
                            rec2=Rectangle(Point(j*brick_w,brick_t + i * brick_h), Point(j*brick_w + brick_w,brick_t + i * brick_h + brick_h))
                            rec2.draw(displayArea)
                            rec2.setFill("yellow")
                            rec2.setOutline("red")

                            hit = 1
                            break                        
                         #right hit
                        if (x+step_x-r<=  j* brick_w+brick_w   and x-r>= j* brick_w+brick_w  and y>= brick_t+i*brick_h- r and y<= brick_t+i*brick_h+brick_h+r):
                            step_x=step_x*-1
                            array[i][j]=1
                            rec2=Rectangle(Point(j*brick_w,brick_t + i * brick_h), Point(j*brick_w + brick_w,brick_t + i * brick_h + brick_h))
                            rec2.draw(displayArea)
                            rec2.setFill("yellow")
                            rec2.setOutline("red")

                            hit = 1
                            break                        

                        
                if (hit == 1):
                    break

                    
            print(array)

            #for item in displayArea.items[:]:  #[circle, line]
                #if(item==rec):
                    #item.undraw()
            
            x = x + step_x
            #r=r+step_r
            y=y+step_y

            
            time.sleep(0.01)
            rec.undraw()
            cir.undraw()
            displayArea.update()
            

            



                                                                                 
