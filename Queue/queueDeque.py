from collections import deque

# Enqueue --> append(): add elements to the rear of the queue.
# Dequeue --> popleft(): remove elements from the front of the queue (FIFO order).
# Peek --> access the first element using index [0].

q = deque()

# Enqueue
q.append('a')
q.append('b')
q.append('c')

print("Initial Queue:", list(q))

# Dequeue
print("Dequeued:", q.popleft())
print("Dequeued:", q.popleft())

print("Queue After Dequeue:", list(q))

# Peek
if q:
    print("Front of Queue (peek):", q[0])
else:
    print("Queue is empty!")