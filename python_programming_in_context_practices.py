import random
import time
import math
import urllib.request
from image import *

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
    print('Time:', end - start, ' seconds')

#11  ---------------> Bubble Sort
#O(n^2)
def bubbleSort(uList):
    comparations = 0
    i = 0
    for i in range(len(uList)-i):
        for j in range(len(uList)-i-1):
            temp = uList[j+1]
            comparations += 1
            if(uList[j]>uList[j+1]):
                uList[j+1]= uList[j]
                uList[j] = temp
    #print('Comparations performed: ', comparations)

def generateRandomList(limit):
    uList = []
    for i in range(limit):
        uList.append(random.randint(1,limit))
    return uList
                
def isSorted(sList):
    sorted = True
    for i in range(len(sList)-1):
        if(sList[i]>sList[i+1]):
            sorted = False;
            break
    return sorted
#11  ---------------> Merge Sort
#O(nlog(n))
def mergeSort(uArr):
    return mergeAndSort(uArr, 0, len(uArr)-1)

def mergeAndSort(uArr, lo, hi):

    if(len(uArr)==1):
        return uArr

    mid = (lo+hi)//2
    iArr = mergeAndSort(uArr[0:mid+1], 0, mid)
    jArr = mergeAndSort(uArr[mid+1:hi+1], 0, hi-mid-1)
 
    i = j = 0
    iLen = len(iArr)
    jLen = len(jArr)

    mergeArr = []
    while(len(mergeArr)<iLen+jLen):
        if(iArr[i]<jArr[j]):
            mergeArr.append(iArr[i])
            if(i+1<iLen):
                i=i+1
            else:
                mergeArr = mergeArr + jArr[j:jLen]
                
        else:
            mergeArr.append(jArr[j])
            if(j+1<jLen):
                j=j+1
            else:
                mergeArr = mergeArr + iArr[i:iLen]

    return mergeArr

#12  ---------------> Insertion Sort
def insertionSort(uArr):
    for i in range(1, len(uArr)):
        j = i
        while uArr[j-1] > uArr[j] and j>0:
            temp = uArr[j]
            uArr[j] = uArr[j-1]
            uArr[j-1] = temp
            j-=1


#13  ---------------> Print frequencies
def printFrequencies(_list):
    prev = _list[0]
    counter = 1
    for i in range(1, len(_list)):
        foll = _list[i]
        if(prev!=foll):
            print(prev, ' ', counter)
            counter  = 1
            prev = foll
            if(i+1==len(_list)):
                print(prev, ' ', counter)
        else:
            counter = counter + 1
            if(i+1==len(_list)):
                print(prev, ' ', counter)
                
        
#14  ---------------> Write document  
def writeFile():
    outfile = open("rainfallCm.txt", "w")
    fileref = open("rainfall.txt", "r")
    for line in fileref:
        values = line.split()
        outfile.write(values[0]+ " had "+ str(float(values[1])*2.54)+ "cms of rain \n")

    outfile.close()
    fileref.close()
            
#15  ---------------> First web scraping function
def countHeadAndPrintBodyAndSave(url, name):
    page = urllib.request.urlopen(url)
    numHeadLines = 0
    outfile = open(name+".txt", "w")

    line = page.readline().decode('utf-8')
    while '<head>' not in line:
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')
    while '</head>' not in line:
        numHeadLines = numHeadLines + 1
        line = page.readline().decode('utf-8')
        
    line = page.readline().decode('utf-8')
    
    while '<body>' not in line:
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')
    while '</body>' not in line and line != '' :
        print(line[:-1])
        outfile.write(line)
        line = page.readline().decode('utf-8')

    print('The number of lines of the header = ', numHeadLines)
    page.close()
    outfile.close()


#16  ---------------> Get links from a web
def getLinks(url):
    page = urllib.request.urlopen(url)
    line = page.readline().decode('utf-8')
    links = []

    while line != '':
        if 'href' in line:
            parts = line.split('href="')
            if len(parts) >1:
                link = parts[1].split('"')[0]
                links.append(link)    
        line = page.readline().decode('utf-8')
    return links

#17 ---------------> Image proccesing
def drawRandomColors(width,height):
    w = width
    h = height
    win = ImageWin(w,h,"RandomColors")
    img = EmptyImage(w,h)
    for i in range(h):
        for j in range(w):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            img.setPixel(i,j, Pixel(r,g,b))
    
            
    img.draw(win)
    img.save("RandomColors.gif")

#18 ---------------> Draw a circle
def drawCircle(diameter):

    width = diameter + 20
    center = width/2
    win = ImageWin(width,width,"Circle")
    img = EmptyImage(width,width)
    for i in range(width):
        for j in range(width):
          distance = math.sqrt((i-center)**2+(j-center)**2)
          
          if(distance<=(diameter/2)):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            img.setPixel(i,j, Pixel(r,g,b))
                  

    img.draw(win)
    img.save("RandomColors.gif")
            
    
#19 ---------------> Negative Images
def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    return Pixel(newRed, newGreen, newBlue)
    
#20 ---------------> makeNegative
def makeNegative(imageFile):
    
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    win = ImageWin(width*2,height, "Image Processing")
    oldImage.draw(win)
    newImage = EmptyImage(width, height)
    
    for i in range(height):
        for j in range(width):
            newPixel = negativePixel(oldImage.getPixel(j,i))
            newImage.setPixel(j,i, newPixel)

    newImage.setPosition(width+1,0)
    newImage.draw(win)
    win.exitOnClick()
    
