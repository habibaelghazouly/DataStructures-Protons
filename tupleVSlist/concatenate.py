# List Concatenation
a = [1, 2, 3]
b = [4, 5, 6]

print("Concatinated List of 'a + b' : " , a + b) # This will print the concatenated list [1, 2, 3, 4, 5, 6]

# Modifying the original list 'a' by concatenating 'b' to it
a += b  
print("List 'a' after modifying : " , a)  # This will print the modified list 'a'


# Tuple Concatenation
c = (7, 8, 9)
d = (10, 11, 12)
print("Concatinated Tuples of 'c + d' : " , c + d)

# Attempting to modify a tuple by concatenating another tuple to it
# This will raise a TypeError since tuples are immutable
# This will not raise an error, but it will not change 'c' since tuples are immutable and creates a new tuple
c += d  
print("New Tuple is created after attempting to modify 'c'  : " , c)  