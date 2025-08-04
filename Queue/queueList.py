""" Queue using List """

# Enqueue --> append() : add elements to end of queue
# Dequeue --> pop(0) : removes from the front (FIFO)
# Peek --> stack[-1] : looks at the top element without removing it.

queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial Queue:", queue)

print("Dequeued:", queue.pop(0))
print("Dequeued:", queue.pop(0))


# Peek at the front (next to be removed)
if queue:
    print("Front of Queue (peek):", queue[0])
else:
    print("Queue is empty!")

# Dequeue remaining and handle empty queue
queue.pop()
try:
    queue.pop()
except IndexError as e:
    print("\033[91mERROR: Cannot dequeue from empty queue!\033[0m")