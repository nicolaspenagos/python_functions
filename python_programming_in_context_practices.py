import random
import math

#1  ---------------> DRAW SQUARE:
def drawSquare(myTurtle, sideLength):
    for i in range(4):
        if(i%2==0):
            myTurtle.forward(2*sideLength)
        else:
            myTurtle.forward(sideLength)
        myTurtle.right(90)

#2  ---------------> DRAW SPIRAL:
def drawSpiral(myTurtle, maxSize):
    for i in range(1,maxSize,1):
        myTurtle.forward(i)
        myTurtle.right(90)
        
#3  ---------------> DRAW XSQUARE (1.40)
def drawXSquare(myTurtle, limit):
    myTurtle.up()
    myTurtle.goto(0,0)
    myTurtle.down()
    drawXSquareXpos(myTurtle, limit)
    myTurtle.up()
    myTurtle.goto(0,0)
    myTurtle.down()
    drawXSquareXneg(myTurtle, limit)

def drawXSquareXpos(myTurtle, limit):
   for i in range(limit):
       nextPos = i;
       for j in range(10):
           nextPos + (j/10)
           myTurtle.goto(nextPos, (nextPos**2))

def drawXSquareXneg(myTurtle, limit):
   for i in range(limit):
       nextPos = i;
       for j in range(10):
           nextPos + (j/10)
           myTurtle.goto(-1*nextPos, (nextPos**2))
           
#4  ---------------> DRAW HALF_X_PLUS_3 (1.41)
def drawHalfXPlus3(myTurtle, limit):
    myTurtle.up()
    myTurtle.goto(0,3)
    myTurtle.down()
    myTurtle.goto(limit, ((limit/2)+3))
        
#5  ---------------> DRAW POLYGON
def drawCircle(myTurtle, radius):
    circunference = 2*3.1416*radius
    sideLength = circunference/360
    drawPolygon(myTurtle,sideLength, 360)
    
def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360/numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
        
#6  ---------------> LEIBNIZ FORMULA
def leibnizFormula(terms):
    num = 4
    den = 1
    acc = 0
    for i in range(terms):
        acc = acc + num/den * (-1)**i
        den = den + 2
    return acc

#7  ---------------> MONTE CARLO SIMULATION
def monteCarloSimulation(numDarts):
    sumDartsIn = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt((x**2+y**2))
        if(d<=1):
            sumDartsIn = sumDartsIn +1
    return sumDartsIn/numDarts*4

#8  ---------------> TRANSPOSITION CIPHER
def scramble2Encrypt(plainText):
    oddChars = ''
    evenChars = ''
    charCount = 0
    for ch in plainText:
           if(charCount%2==0):
              evenChars = evenChars + ch
           else:
               oddChars = oddChars + ch
           charCount = charCount +1
    return oddChars + evenChars
            

           
        
    
