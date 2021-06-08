# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

def calculator(op, n1, n2):
    if op == "+":
        print("adding...")
        return (addition(n1,n2))

    elif op == "-":
        print ("subtracting...")
        return (subtraction(n1,n2))

    elif op == "x":
        print ("multiplying...")
        return (multiplication(n1,n2))

    elif op == "/":
        print ("divinding...")
        return (division(n1,n2))

    else:
        print("incorrect operation")

    # Use a breakpoint in the code line below to debug your script.

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    operation = raw_input("what operation would you like to do?[+, -, x, /] : ")
    number1 = int(raw_input("enter your first number : "))
    number2 = int(raw_input("entre your second number : "))
    result = calculator(operation,number1,number2)
    print ("result = " + str(result))


