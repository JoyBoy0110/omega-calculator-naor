def menu():
    print("\n")
    print("          calculator")
    print("-------------------------------")
    print("\n")
    num1 = input("num1:                ")
    print("actions: 1.   add   2.  sub    3. mul ")
    print("         4.   div   5.  pow    6. end ")
    action = input("input")
    if(int(action) == 1):
        operator = '+'
    if(int(action) == 2):
        operator = '-'
    if (int(action) == 3):
        operator = '*'
    if (int(action) == 4):
        operator = '/'
    if (int(action) == 5):
        operator = '^'
    if(int(action) == 6):
        return
    print("\n")
    print(num1+operator)
    num2 = input("num2:                ")
    print("\n")
    print(num1+operator+num2)
    if (int(action) == 1):
        sumN(num1, num2)
    if (int(action) == 2):
        sumN(num1, num2)
    if (int(action) == 3):
        sumN(num1, num2)
    if (int(action) == 4):
        operator = '/'
    if (int(action) == 5):
        operator = '^'
    if (int(action) == 6):
        return