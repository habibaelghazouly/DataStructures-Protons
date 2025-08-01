from collections import deque

""" 
Stacks using collections.deque

- Push --> append(x): Pushes element x onto the top of the stack
- Pop --> pop(): Removes and returns the top element (LIFO order)
- len(stack): Returns the number of elements in the stack
"""

# Create an empty deque to use as a stack
stack = deque()

print("Initial stack:", list(stack))
print("Is empty?", len(stack) == 0)

# Push elements onto the stack
stack.append('a')   # Stack: ['a']
stack.append('b')   # Stack: ['a', 'b']
stack.append('c')   # Stack: ['a', 'b', 'c']

print("\nAfter pushing elements:")
print('Stack: ',stack) # Top on right
print(list(stack))

print("Stack (top -> bottom):", list(reversed(stack)))  # To show top on the left


print("\nElements popped from the stack:")
print(stack.pop())  # Removes 'c'
print(stack.pop())  # Removes 'b'

# Check remaining stack
print("\nStack after popping:",list(stack))
print("Stack (top -> bottom):", list(reversed(stack)))

# Peek at top
top_item = stack[-1]  # this is peek
top_item_2=stack[len(stack)-1]

print("Peek:", top_item)
print("Peek using len:", top_item_2)

# Stack is unchanged
print("After peek:", list(reversed(stack)))

# Try to pop from empty stack with error handling
try:
    stack.pop()
except IndexError as e:
    print("\033[91mERROR POPPING FROM EMPTY STACK: " + str(e).upper() + "!!!!\033[0m")

# Final state
print("\nFinal stack:", stack)
print("Is empty?", len(stack) == 0)
