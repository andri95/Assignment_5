# User inputs desired length of sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line

# Variables that hold initial 3 numbers of seq

num_one = 1
num_two = 2
num_three = 3

# Set counter as 3

counter = 3

# Print out initial numbers

print(num_one)
print(num_two)
print(num_three)

# While loop to print out n numbers of sequence

while counter < n:

    # sum of all 3 numbers
    sum_all = num_one + num_two + num_three

    print(sum_all)

    # Increment counter by one

    counter += 1

    # Rotate values of variables

    num_one = num_two
    num_two = num_three
    num_three = sum_all
