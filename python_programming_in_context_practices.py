import random
import time
import math

#1  ---------------> Draw Square:
def drawSquare(myTurtle, sideLength):
    for i in range(4):
        if(i%2==0):
            myTurtle.forward(2*sideLength)
        else:
            myTurtle.forward(sideLength)
        myTurtle.right(90)

#2  ---------------> Draw Spiral:
def drawSpiral(myTurtle, maxSize):
    for i in range(1,maxSize,1):
        myTurtle.forward(i)
        myTurtle.right(90)
        
#3  ---------------> Draw X^2
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
           
#4  ---------------> Draw x/2 + 3
def drawHalfXPlus3(myTurtle, limit):
    myTurtle.up()
    myTurtle.goto(0,3)
    myTurtle.down()
    myTurtle.goto(limit, ((limit/2)+3))
        
#5  ---------------> Draw Polygon
def drawCircle(myTurtle, radius):
    circunference = 2*3.1416*radius
    sideLength = circunference/360
    drawPolygon(myTurtle,sideLength, 360)
    
def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360/numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
        
#6  ---------------> Leibniz Formula
def leibnizFormula(terms):
    num = 4
    den = 1
    acc = 0
    for i in range(terms):
        acc = acc + num/den * (-1)**i
        den = den + 2
    return acc

#7  ---------------> Monte Carlo Simulation
def monteCarloSimulation(numDarts):
    sumDartsIn = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt((x**2+y**2))
        if(d<=1):
            sumDartsIn = sumDartsIn +1
    return sumDartsIn/numDarts*4

#8  ---------------> Tranposition Cipher
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

def scramble2Decrypt(cipherText):
    
    halfLength = len(cipherText)//2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    
    plainText = ''
    
    for i in range(halfLength):
            plainText = plainText + evenChars[i]
            plainText = plainText + oddChars[i]

    if len(evenChars)>len(oddChars):
        plainText = plainText + evenChars[-1]
    else:
        plainText = plainText + oddChars[-1]
    
    return plainText;
    
#9  ---------------> Input Encrypt Message
def encryptMessage():
    msg = input('Enter a message to encrypt: ')
    cipherText = scramble2Encrypt(msg)
    print('The encrypted meesage is: ', cipherText)

#10  ---------------> Susbtitution Cipher
def substitutionEncrypt(plainText, key):

    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    plainText = plainText.lower()
    cipherText = ''
    
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
        
    return cipherText

def substitutionDecrypt(cipherText, key):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cipherText = cipherText.lower()
    plainText = ''

    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]

    return plainText

def getMyKey():
    
    key = ''
    keepGoing = True;

    while keepGoing:
        ch = chr(random.randint(97,122))
        if(ch not in key):
            key = key + ch
            
        if len(key)>= 26:
            keepGoing = False

    key = key + ' '
    return key 
        
#11  ---------------> Shuffle
#O(n^2) (because of the pop())
def shuffle(myList): 
    
    shuffleList = []
    c = 0;
    
    for i in range(len(myList)):
        idx = random.randint(0, len(myList)-1)
        shuffleList.append(myList.pop(idx))
        c=c+ len(myLIst)

    print('Iterarions: ',c)
    return shuffleList
#O(n^2) (because of the pop())
def shuffleVoid(myList):
    
    shuffleList = []
    c = 0;
    
    for i in range(len(myList)):
        idx = random.randint(0, len(myList)-1)
        shuffleList.append(myList.pop(idx))
        c=c+len(myList)

    for i in range(len(shuffleList)):
        myList.append(shuffleList.pop())
        c=c+1

    print('Iterarions: ',c)

     
def bigList(limit):
    bigList = []
    for i in range(limit):
        bigList.append(i)
    return bigList

#O(n-1)
def fisherYatesShuffle(_list):
    c = 0;
    n = len(_list)
    for i in range(n-1, 0, -1):
        c = c+1
        idx = random.randint(0, i)
        if(idx!=i):
            temp = _list[i]
            _list[i] = _list[idx]
            _list[idx] = temp
    
    print('Iterarions: ', c)
        


def measureTime(fun, _list):
    
    start = time.time()
    fun(_list)
    end = time.time()
    print('Time:', end - start)



    
        
