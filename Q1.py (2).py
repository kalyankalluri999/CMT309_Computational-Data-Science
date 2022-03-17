# Studnet ID: 21109714

import re

# Below we used "def" keyword with do_arithmetic function which takes three input arguments: a number x, y, and a string op representing an operation.

def do_arithmetic(x,y,op='add'):
    '''
    "def":- In Python def is a keyword used to build or define a function. A function is a logical unit of code containing a sequence of statements indented 
     under a name given using the “def” keyword.

    "do_arithmetic":- We call this function "do_arithmetic" for performing opertaions. The function will perform the operation on the two numbers and
     return the result.
     '''
    
    operations = ['add','subtract','multiply','divide','+','-','*','/']
# I used a vaiable "operations" and called respective strings and arithematic operators in a list .

    ''' 
    Generally we use "if statement" for decision making. It contains a body of code which runs only when the given condition in the if statement is true. 
    If the condition is false, then the optional else statement runs which contains some code for the else condition.
    
    op.lower() :- It is a method which converts uppercase characters in a string into lowercase characters and we linked to operations.
    '''
    if op.lower() in operations:
        if op.lower() == 'add' or op.lower() == '+':
            return(float(x + y))
# We call the if statemnet with method op.lower, whenever we call a string "add" (or) calls the arithematic operator "+" it will performs addition operation.
# Also, we used return statement for printing respective operation.
        elif op.lower() == 'subtract' or op.lower() == '-':
            return(float(x - y))
# We use elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.
# We call the elif statemnet with method op.lower, whenever we call a string 'subtract' (or) calls the arithematic operator "-" it will perform subtraction operation.
        elif op.lower() == 'multiply' or op.lower() == '*':
            return(float(x * y))
# We call the elif statemnet with method op.lower, whenever we call a string 'multiply' (or) calls the arithematic operator "*" it will perform multiplication operation.
        elif op.lower() == 'divide' or op.lower() == '/':
            try:
                print(float(x / y))
            except ZeroDivisionError:
                print('Division by 0!')
    else: 
        print('Unknown operation')
# We call the if statemnet with method op.lower for performing division operation.
#If the elif statement is False or not satisified with the given condition, it will print result as "unknown operation".
        
############################################################ 1(b)#########################################################
def sum_of_digits(s):
    '''
    "def":- In Python def is a keyword used to build or define a function. A function is a logical unit of code containing a sequence of statements indented 
     under a name given using the “def” keyword.

     sum_of_digits - We used a function called sum_of_digits(s) which takes input a string that contains some numbers. 
     The function calculates the sum of all the digits in the string, ignoring any symbols that are not digits.
    ''' 
    sum = 0
    count = 0
    digits = []
    alphabets = []

    for ch in s:
        if(ch.isdigit()):
          # isdigit()is a built-in method used for string handling which returns "True" if all the characters are digits,otherwise False.
            digits.append(ch)
          # append() is a  method which adds a single item to the existing list. 
          #It doesn't return a new list of items but will modify the original list by adding the item to the end of the
            sum += int(ch)
            count = count+1
        else:
            alphabets.append(ch)

    updt_str = '+'.join(digits)
# Below we used if,elif and else statements for decision making for passed statements. 
    if count != 0:
        if s != '' and count !=0:
            print('The sum of digits operation performs ' + updt_str)
            print("The extracted non-digits are :",alphabets)
            return (sum)
    elif(s == ""):
            print("Empty string entered!")
            return(0)
    else:
           print("The sum of digits operation could not detect a digit!")
           print("The returned input letters are:",alphabets)
           return(sum)

#Studnet ID: 21109714