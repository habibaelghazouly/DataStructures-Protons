""" Stacks using List """

# Push --> append() : add elements to the top of the stack.
# Pop --> pop() : removes the element in LIFO order.
# Peek --> stack[-1] : looks at the top element without removing it.

stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack (top -> bottom):', list(reversed(stack)))

# Peek at the top of the stack
try:
    print('Peek (top element):', stack[-1])
except IndexError:
    print("\033[93mCANNOT PEEK: STACK IS EMPTY\033[0m")

# Pop elements
print('Popped:', stack.pop())  
print('Popped:', stack.pop())  

print('Stack after popping (top -> bottom):', list(reversed(stack)))

# Another pop
element = stack.pop()
print('Popped:', element)

# Try peeking again
try:
    print('Peek (top element):', stack[-1])
except IndexError:
    print("\033[93mCANNOT PEEK: STACK IS EMPTY\033[0m")

# Try popping from an empty stack
try:
    print('Popped:', stack.pop())
except IndexError as e:
    print("\033[91mERROR POPPING FROM EMPTY STACK: " + str(e).upper() + "!!!!\033[0m")
