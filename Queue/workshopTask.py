from queue import PriorityQueue
import time

print("--- Task Scheduler (using PriorityQueue) ---")

# (priority, execution_time, order_added, task_name)
tasks = [
    (2, 10, "Backup"),
    (1, 5, "Update"),
    (3, 2, "Email Sync"),
    (1, 5, "Antivirus"),
    (2, 3, "Disk Check")
]

pq = PriorityQueue()
order = 0

# Enqueue all tasks
for priority, exec_time, name in tasks:
    pq.put((priority, exec_time, order, name))
    order += 1

# Process tasks in order of priority
while not pq.empty():
    priority, exec_time, order, name = pq.get()
    print(f"Running: {name} (Priority: {priority}, Time: {exec_time}s)")

print("\nAll tasks completed.")
