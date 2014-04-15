#Exercise 5.6 Koch Curve
#Name: Tyler Wallace

from TurtleWorld import *               
world = TurtleWorld()                   
bob = Turtle()

def koch(turtle,x):
        if x < 3:
                fd(turtle,x)
        else:
                pd(turtle)
                koch(turtle,x/3)
                lt(turtle,60)
                koch(turtle,x/3)
                rt(turtle,120)
                koch(turtle,x/3)
                lt(turtle,60)
                koch(turtle,x/3)
