#TurtleGraphics.py
#Name: Jacob Cargile
#Date:9/19/2024
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def moveJim(jim):# Made a new function to move the turtle without lines
    jim.up()
    jim.right(270)
    jim.forward(10)
    jim.left(90)
    jim.forward(10)
    jim.right(180)
    jim.down()

def squaresInSquares(jim, number): 

    if number == 1:
        moveJim(jim)
        drawSquare(jim, 20)
    if number == 2:
        moveJim(jim)
        drawSquare(jim, 20) 
        moveJim(jim)
        drawSquare(jim, 40)
    if number == 3:
        moveJim(jim)
        drawSquare(jim, 20) 
        moveJim(jim)
        drawSquare(jim, 40)
        moveJim(jim)
        drawSquare(jim, 60)
    if number == 4:
        moveJim(jim)
        drawSquare(jim, 20) 
        moveJim(jim)
        drawSquare(jim, 40)
        moveJim(jim)
        drawSquare(jim, 60)
        moveJim(jim)
        drawSquare(jim, 80)
    if number == 5:
        moveJim(jim)
        drawSquare(jim, 20) 
        moveJim(jim)
        drawSquare(jim, 40)
        moveJim(jim)
        drawSquare(jim, 60)
        moveJim(jim)
        drawSquare(jim, 80)
        moveJim(jim)
        drawSquare(jim, 100)


def fillCorner(dave, corner):
    # draw big square
    drawSquare(dave, 100)
    
    
    if corner == 1: 
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 2:
        dave.forward(50)
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 3:
        dave.right(90)
        dave.forward(50)
        dave.left(90)
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
    elif corner == 4:
        dave.up()
        dave.forward(50)
        dave.right(90)
        dave.forward(50)
        dave.left(90)
        dave.down()
        dave.begin_fill()
        drawSquare(dave, 50)
        dave.end_fill()
        
        
        
        
def main():
    myTurtle = turtle.Turtle()
    
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle,5) #draws a pentagon
    
    # drawPolygon(myTurtle, 8) #draws an octogon
    
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares

    # I left all of the commands with the hashtag in front of them so when you grade it you dont have all of them running.

main()
