#Exercise 5.6 Koch Curve
#Name: Tyler Wallace

from TurtleWorld import *               
world = TurtleWorld()                   
bob = Turtle()

def koch(turtle,x):
        if x < 3:
                pd(turtle)
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

def koch_variant(turtle,x):
        if x < 3:
                pd(turtle)
                fd(turtle,x)
        else:
                pd(turtle)
                koch(turtle,x/3)
                lt(turtle,90)
                koch(turtle,x/3)
                rt(turtle,90)
                koch(turtle,x/3)
                lt(turtle,90)
                koch(turtle,x/3)


def snowflake(turtle,x):
        koch(turtle,x)
        rt(turtle,120)
        koch(turtle,x)
        rt(turtle,120)
        koch(turtle,x)

def snowflake2(turtle,x):
        koch_variant(turtle,x)
        rt(turtle,180)
        koch_variant(turtle,x)
        rt(turtle,180)
        koch_variant(turtle,x)
        rt(turtle,180)
        koch_variant(turtle,x)

bob.delay = 0.001

#snowflake(bob,100)
#pu(bob)
#fd(bob,50)

snowflake2(bob,100)


wait_for_user()                 
