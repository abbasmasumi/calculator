# This Project is first's my project in python language that I practiced

import re

print("If Want To Exit Type'x' ")
run = True
first_value = 0


def PerformMath():
    global run
    global first_value

    if first_value == 0:
        equalation = input("Please Enter Your Equation:")
    else:
        equalation = input(str(first_value))

    if equalation == 'x':
        run = False
        print("The last answer to the equation is ", first_value)
    else:
        equalation = re.sub('[a-zA-Z,.:" "(){}]', '', equalation)
        if first_value == 0:
            first_value = eval(equalation)
        else:
            first_value = eval(str(first_value) + equalation)


while run:
    PerformMath()
