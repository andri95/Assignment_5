
# Empty variable to hold largest number

max_int = 0

# Set flag as true to make shure while loop runs at least once

flag = True
while flag:

    # User input
    num_int = int(input("Input a number: "))    # Do not change this line

    # Check if number is positive

    if num_int >= 0:

        # Check if number is larger than max_int

        if num_int >= max_int:
            max_int = num_int

    # If user inputs negative number, print out result, flag becomes false and loop stops running

    else:

        print("The maximum is", max_int)  # Do not change this line
        flag = False
