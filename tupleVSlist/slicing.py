# Demonstrating slicing of lists and tuples

# List slicing
my_list = [10, 20, 30, 40, 50, 60]
print("Original list:", my_list)
print("my_list[1:4]:", my_list[1:4])      # [20, 30, 40]
print("my_list[:3]:", my_list[:3])        # [10, 20, 30]
print("my_list[3:]:", my_list[3:])        # [40, 50, 60]
print("my_list[::-1]:", my_list[::-1])    # [60, 50, 40, 30, 20, 10]

# Tuple slicing
my_tuple = (100, 200, 300, 400, 500, 600)
print("\nOriginal tuple:", my_tuple)
print("my_tuple[1:4]:", my_tuple[1:4])    # (200, 300, 400)
print("my_tuple[:3]:", my_tuple[:3])      # (100, 200, 300)
print("my_tuple[3:]:", my_tuple[3:])      # (400, 500, 600)
print("my_tuple[::-1]:", my_tuple[::-1])  # (600, 500, 400, 300, 200, 100)