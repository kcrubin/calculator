from decimal import DivisionByZero


def welcome():
    print('''
    ***************Welcome to my calculator*******************
    ''')
def calculate():
    operation = input('''
    Please enter the type of operation you want to perform:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    #input two numbers from user
    number_1 = int(input("Enter the first number:"))
    number_2 = int(input("Enter the second number:"))

    if operation == '+':
        #add two numbers
        print('{} + {} = {}'.format(number_1, number_2, number_1 + number_2))
    elif operation == '-':
        #subtract two numbers
        print('{} - {} = {}'.format(number_1, number_2, number_1 - number_2))
    elif operation == '*':
        #multiply two numbers
        print('{} * {} = {}'.format(number_1, number_2, number_1 * number_2))
    elif operation == '/':
        try:
        #divide two numbers
            print('{} / {} = {}'.format(number_1, number_2, number_1 / number_2))
        except ZeroDivisionError:
            print('Divide by zero not allowed')
            again()
    else:
        print('You have entered the invalid operator. Please try again.')
    

def again():
    cal_again = input(''' Do you want to calculate again ?
    Press Y for Yes and N for No.''')

    # if user presses Y
    if cal_again.upper() == 'Y':
        calculate()
    # if user presses N
    elif cal_again.upper() == 'N':
        print('Goodbye')
    # if user presses any other key
    else:
        again()

welcome()
    # call calculation function 
calculate()
