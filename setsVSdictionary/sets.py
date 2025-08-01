# Demonstration of using sets in Python
# Sets are unordered collections of unique elements     

# adding elements to a set
print("🔹 Adding elements to a set")
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}
print() 

# removing element from a set
print("🔹 Removing element from a set")
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

# trying to remove an element not present in the set
print("🔹 Trying to remove an element not present in the set")
s = {1, 2, 3}
try:
    s.remove(5)
except KeyError:
     print("\033[91m" + "ERROR: " + "Element not found".upper() + "\033[0m")
print()    

# discarding an element from a set
# Removes an element if present. No error if not found.
print("🔹 Discarding an element from a set")
s = {1, 2, 3}
s.discard(5)  # No error
print(s)  # {1, 2, 3}
print()

# popping an element from a set
print("🔹 Popping an element from a set")
s = {1, 2, 3}
elem = s.pop()
print(elem)  # Random element from the set
print(s)
print()

# clearing a set
print("🔹 Clearing a set")
s = {1, 2, 3}
s.clear()
print(s)  # set()
print()

# union of sets
print("🔹 Union of sets")
a = {1, 2}
b = {2, 3}
print(a.union(b))  # OR print(a | b)  # {1, 2, 3}
print()

# intersection of sets
print("🔹 Intersection of sets")
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # OR print(a & b)  # {2, 3}
print()

# difference of sets
print("🔹 Difference of sets")
a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))  # OR print(a - b) 
print()

# symmetric difference of sets
print("🔹 Symmetric difference of sets")
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))  # OR print(a ^ b)  
print()

# subset and superset checks
print("🔹 Subset and Superset checks")
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # returns boolean 
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # returns boolean
print()

# disjoint sets
print("🔹 Disjoint sets")
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # returns boolean
print()    

# frozen set
print("🔹 Frozen Set (Immutable Set)")
# frozenset is an immutable version of a set

# Creating a frozenset
fs = frozenset([1, 2, 3, 2])
print(fs)  # frozenset({1, 2, 3})

# frozen sets support set operations
fs2 = frozenset([3, 4])
print(fs.union(fs2))               # frozenset({1, 2, 3, 4})
print(fs.intersection(fs2))        # frozenset({3})
print(fs.difference(fs2))          # frozenset({1, 2})
print(fs.symmetric_difference(fs2))# frozenset({1, 2, 4})

# frozen sets cannot be modified
try:
    fs.add(5)
except AttributeError as e:
    print("\033[91m" + "ERROR: " + str(e).upper() + "\033[0m")
