# Define a 2D tuple (tuple of tuples)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Traverse the 2D tuple using nested loops
for row in matrix:
    print(f"Row {row}:")
    for indx , item in enumerate(row):
        print(f"Element {indx}: {item}")