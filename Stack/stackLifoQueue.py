from queue import LifoQueue

""" Stacks using Lifo Queue """

# Push --> put() : add elements to the top of the stack.
# Pop --> get() :  removes the element in LIFO order. 

# More Useful methods 
# full()
# qsize() show the number of elements currently in stack
# empty()

stack=LifoQueue(maxsize=5)

print('Before Adding Size of Stack: ',stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print('Stack',stack) # can't print directly the contents of a LifoQueue 
print('Size of Stack: ',stack.qsize())
print("is Full ? ",stack.full())

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())


    
print('Size of Stack: ',stack.qsize())
print("is Empty ? ", stack.empty())