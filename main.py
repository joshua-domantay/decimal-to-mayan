# Decimal to Mayan
# By Joshua Anthony Domantay
# 6 May 2021

def getDigits(n, arr):
    pass

def printTopBottom(arr):
    for i in range(len(arr)):
        print("+----", end="")
    print("+\n")

def printMid(arr):
    pass

def convert(n):
    arr = []
    arr = getDigits(n, arr)
    return "x"

digit = input("Enter decimal digit: ")
try:
    digit = int(digit)
    if(digit > 0):
        x = convert(digit)
        print(x)
    else:
        print("Digit must be greater than 0")
except:
    print("ERROR: Input cannot be converted to integer")
