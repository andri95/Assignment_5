# User inputs desired length of sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line

# Empty variable to hold numbers of sequence

number = 1

# for loop starts as 1, ends as n
for x in range(1, n + 1):

    # Print out result

    print(number)

    # Add x to number variable

    number += x