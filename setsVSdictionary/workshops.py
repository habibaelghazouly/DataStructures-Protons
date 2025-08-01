# workshop 1

wallet1 = [10, 20, 50, 100]
wallet2 = [5, 10, 20, 200]

common = set(wallet1).intersection(wallet2)
print("Common denominations:", common)


# workshop 2

# Prompt the user to input a number and store it in the variable 'n'.
n = int(input("Input a number "))

# Create an empty dictionary 'd' to store the square of numbers.
d = dict()

# Iterate through numbers from 1 to n
for x in range(1, n):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x * x

# Print the dictionary 'd' containing the squares of numbers from 1 to 'n'.
print(d) 
