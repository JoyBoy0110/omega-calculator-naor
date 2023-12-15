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
    num2 = 0
    answer = 0
    cont = 0
    while 1:
        printCalculator()
        if (answer*10) % 10 == 0:
            answer = int(answer)
        if cont != 0:
            print("last answer: ", str(answer))
        num1 = input("num1:                ")
        if str(num1) == "ans":
            num1 = answer
        else:
            num1 = int(num1)
        print("actions: 1.   add   2.  sub    3. mul ")
        print("         4.   div   5.  pow    6. equal ")
        print("         7. end                             ")
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
            operate = '='
        if int(action) == 7:
            return
        printCalculator()
        if int(action) != 6:
            print(str(num1) + operate)
            num2 = input("num2:                ")
        if str(num2) == "ans":
            num2 = answer
        else:
            num2 = int(num2)
        if int(action) == 1:
            answer = sumNums(num1, num2)
        if int(action) == 2:
            answer = subNums(num1, num2)
        if int(action) == 3:
            answer = mulNums(num1, num2)
        if int(action) == 4:
            answer = divNums(num1, num2)
        if int(action) == 5:
            answer = toPowerNums(num1, num2)
        if int(action) == 6:
            answer = num1
        if int(action) == 7:
            return
        printCalculator()
        if int(action) != 6:
            print(str(num1) + operate + str(num2), '=', str(answer))
        else:
            print(str(num1), "=", str(num1))
        print("options:")
        print("1. continue 2. end")
        cont = int(input())
        if cont == 2:
            return


menu()
