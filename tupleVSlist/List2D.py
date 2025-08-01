# Example of a 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Traversing each element:")
# Traverse and print each element
for i in range(len(matrix)):  #NOTE!!! len(matrix) returns the number of rows
    print(f"Row {i}:")
    for j in range(len(matrix[i])):
        print(f"Element at ({i}, {j}):", matrix[i][j])
       