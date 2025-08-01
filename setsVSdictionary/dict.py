# Demonstration of using dictionaries in Python
# Dictionaries are unordered collections of key-value pairs (keys unique and hashable)

# creating and accessing a dictionary
print("🔹 Creating and accessing a dictionary")
d = {"name": "Alice", "age": 25}
print(d["name"])  # Alice
print()

# adding or updating key-value pairs
print("🔹 Adding or updating key-value pairs")
d["city"] = "New York"  # Add new key
d["age"] = 26           # Update existing key
print(d)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}
print()

# removing a key using del
print("🔹 Removing a key using del")
del d["city"]
print(d)  # {'name': 'Alice', 'age': 26}
print()

# removing a key using pop()
print("🔹 Removing a key using pop()")
age = d.pop("age")
print("Popped age:", age)
print(d)  # {'name': 'Alice'}
print()

# safely accessing keys with get()
print("🔹 Safely accessing keys with get()")
print(d.get("name" , "Not Found"))  # Alice
print(d.get("city", "Not Found"))  # Not Found
print()

# looping through dictionary items
print("🔹 Looping through dictionary items")
d = {"a": 1, "b": 2, "c": 3}
for key, value in d.items():
    print(f"{key}: {value}")
print()

# checking if a key exists
print("🔹 Checking if a key exists")
print("a" in d)  # True
print("z" in d)  # False
print()

# clearing the dictionary
print("🔹 Clearing the dictionary")
d.clear()
print(d)  # {}
print()

# nested dictionary example
print("🔹 Nested dictionary example")
student = {
    "name": "Bob",
    "grades": {
        "math": 90,
        "science": 85
    }
}
print(student["grades"]["math"])  # 90
print()

# using dict.fromkeys()
print("🔹 Using dict.fromkeys()")
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # {'a': 0, 'b': 0, 'c': 0}
print()
