from turtle import *



wn = Screen()
wn.setup(width=800, height=800)
wn.bgcolor('black')


TT = Turtle()
TT.color('white')
#TT.setpos(-200,-200 )
TT.clear()


def koch (a, order):
    if order > 0:
        for t in [60,-120,60,0] :
            #forward(a/3)
            koch(a/3, order-1)
            TT.left(t)
    else:
        TT.forward (a)


def koch2 (a, order):
    if order > 0:
        for t in [-60,120,-60,0] :
            #forward(a/3)
            koch2(a/3, order-1)
            TT.left(t)
    else:
        TT.forward (a)

koch2(200,4)
TT.left(120)
koch2(200,4)
TT.left(120)
koch2(200,4)


