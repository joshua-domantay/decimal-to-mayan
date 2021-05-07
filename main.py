# Decimal to Mayan
# By Joshua Anthony Domantay
# 6 May 2021

def getDigits(n, arr):
    while(n != 0):
        arr.append(int(n % 20))
        n = int(n / 20)
    
    i = 0
    j = len(arr) - 1
    while(j > i):
        x = arr[j]
        arr[j] = arr[i]
        arr[i] = x
        j -= 1
        i += 1
    return arr

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
    printTopBottom(arr)
    printMid(arr)
    printTopBottom(arr)

digit = input("Enter decimal digit: ")
try:
    digit = int(digit)
    if(digit > 0):
        x = convert(digit)
    else:
        print("Digit must be greater than 0")
except:
    print("ERROR: Input cannot be converted to integer")
