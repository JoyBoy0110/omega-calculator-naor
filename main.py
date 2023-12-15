import os


# actions functions
def sumNums(num1, num2):
    return num1 + num2


def subNums(num1, num2):
    return num1 - num2


def mulNums(num1, num2):
    return num1 * num2


def divNums(num1, num2):
    return num1 / num2


def toPowerNums(num1, num2):
    return num1 ** num2


# print calculator configuration
def printCalculator():
    os.system('cls')
    print("\n")
    print("          calculator")
    print("-------------------------------")
    print("\n")


# menu function
def menu():
    operate = ''
    num1 = 0
    num2 = 0
    printCalculator()
    num1 = input("num1:                ")
    num1 = int(num1)
    print("actions: 1.   add   2.  sub    3. mul ")
    print("         4.   div   5.  pow    6. end ")
    action = input("input:")
    if int(action) == 1:
        operate = '+'
    if int(action) == 2:
        operate = '-'
    if int(action) == 3:
        operate = '*'
    if int(action) == 4:
        operate = '/'
    if int(action) == 5:
        operate = '^'
    if int(action) == 6:
        return
    printCalculator()
    print(str(num1)+operate)
    num2 = input("num2:                ")
    num2 = int(num2)
    printCalculator()
    print(str(num1)+operate+str(num2))
    if int(action) == 1:
        sumNums(num1, num2)
    if int(action) == 2:
        subNums(num1, num2)
    if int(action) == 3:
        mulNums(num1, num2)
    if int(action) == 4:
        divNums(num1, num2)
    if int(action) == 5:
        toPowerNums(num1, num2)
    if int(action) == 6:
        return


menu()