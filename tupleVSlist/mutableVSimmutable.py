# Demonstrating the difference between lists (mutable) and tuples (immutable)
# when trying to modify their values.

# Define a list and a tuple with the same elements
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("Original list:", my_list)
print("Original tuple:", my_tuple)

# Attempt to delete the first element of the list
try:
    del my_list[0]
    print("List after deletion:", my_list)
except TypeError as e:
    print("\033[91mERROR DELETING FROM LIST: " + str(e).upper() + "!!!!\033[0m")

# Attempt to delete the first element of the tuple
try:
    del my_tuple[0]
    print("Tuple after deletion:", my_tuple)
except TypeError as e:
    print("\033[91mERROR DELETING FROM TUPLE: " + str(e).upper() + "!!!!\033[0m")

# Attempt to modify the first element of the list
try:
    my_list[0] = 10
    print("Modified list:", my_list)
except TypeError as e:
    print("\033[91mERROR MODIFYING LIST: " + str(e).upper() + "!!!!\033[0m")

# Attempt to modify the first element of the tuple
try:
    my_tuple[0] = 10
    print("Modified tuple:", my_tuple)
except TypeError as e:
    print("\033[91mERROR MODIFYING TUPLE: " + str(e).upper() + "!!!!\033[0m")
