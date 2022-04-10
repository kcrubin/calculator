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
        #divide two numbers
        print('{} / {} = {}'.format(number_1, number_2, number_1 / number_2))
    else:
        print('You have entered the invalid operator. Please try again.')

    # call calculation function 
calculate()

def again():
    cal_again = input(''' Do you want to calculate again ?
    Press Y for Yes and N for No.''')

    # if user presses Y
    if cal_again == 'Y' or 'y':
        calculate()
    # if user presses N
    elif cal_again == 'N' or 'n':
        print('Goodbye')
    # if user presses any other key
    else:
        again()