# Decimal to Mayan
# By Joshua Anthony Domantay
# 6 May 2021

def getDigits(n, arr):
    pass

def printTopBottom(arr):
    for i in range(len(arr)):
        print("+----", end="")
    print("+")

def printMid(arr):
    x = 15
    for i in range(4):
        print("|", end="")
        for j in range(len(arr)):
            y = arr[j] - x
            if(y == 5):
                print("----", end="")
                arr[j] -= 5
            elif(y == 4):
                print("....", end="")
                arr[j] -= 4
            elif(y == 3):
                print("... ", end="")
                arr[j] -= 3
            elif(y == 2):
                print(" .. ", end="")
                arr[j] -= 2
            elif(y == 1):
                print(" .  ", end="")
                arr[j] -= 1
            else:
                if(i != 3):
                    print("    ", end="")
                else:
                    print(" @  ", end="")
            print("|", end="")
        print()
        x -= 5
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
