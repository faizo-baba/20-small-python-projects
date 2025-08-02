import art
from sympy import false, true
import os

def add (n1,n2):
    return n1+n2
def sub (n1,n2):
    return n1-n2
def multi (n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2

operations = {
    "+" : add, 
    "-" : sub,
    "*" : multi,
    "/" : divide,
}
def calculater ():
    print (art.logo)
    should_continue = true
    num1 = float(input("enter 1st number: "))

    while should_continue :

        for symbol in operations :
            print(symbol) 
        operands  = input("enter the operand: ")    
        num2 = float (input("enter 2nd number: "))

        answer = (operations[operands](num1,num2))
        print(answer)

        another_calcu= input(f"type y for another calculation with {answer}, N for new calculation: ")

        if another_calcu == "y" :
            num1 = answer
            
        else :
            should_continue = false 
            os.system("clear") 
            calculater()
            
calculater()
