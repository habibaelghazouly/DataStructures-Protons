# Step 1: Create an empty list for packing
packing_list = []

# Step 2: Ask John what he wants to pack
print("John is going on a trip! Let's help him pack.")
item_count = int(input("How many items does John want to pack? "))

for i in range(item_count):
    item = input(f"Enter item {i + 1}: ")
    packing_list.append(item)

# Step 3: Show the list before locking
print("\nPacking list before locking:")
print(packing_list)

# Step 4: Finalize and lock the suitcase as a tuple
locked_suitcase = tuple(packing_list)

print("\n🚨 Suitcase locked! 🚨")
print("Final contents (as a tuple):")
print(locked_suitcase)

# Step 5: Try modifying the locked suitcase
try:
    locked_suitcase[0] = "something else"
except TypeError as e:
    print("\033[91mERROR: YOU CANNOT MODIFY A LOCKED SUITCASE!!!!\033[0m")
