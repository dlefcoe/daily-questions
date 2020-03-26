# example of how to use turtle graphics

import turtle
import random

pen = turtle.Turtle()
txt = turtle.Turtle()

# screen setup
scr = turtle.Screen()
scr.title('example turtle program')
scr.bgcolor('black')
scr.setup(width=600, height=500)
scr.tracer(0)


x = scr.screensize()


print(x)

pen.color("red")
turtle.colormode(255)

def writeAtTop(v):
    txt.undo()
    txt.penup()
    txt.goto(200,200)
    txt.pendown()
    txt.color('white')
    txt.write("iteration value: " + str(v+1))



# turtle.write('helloWorld')
def drawShape():

    rSize = 50
    for i in range(rSize):
        randomColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pen.color(randomColour)
        #pen.color('yellow')
        pen.forward(100)
        pen.left(155)
        writeAtTop(i)
        for j in range(5):
            pen.color('blue')
            pen.forward(20)
            pen.left(72)
        
    pen.penup()
    pen.left(45)
    pen.forward(0.5*(100**2 + 100**2)**0.5)
    pen.pendown()


for i in range(3):
    drawShape()




# the end
turtle.done()