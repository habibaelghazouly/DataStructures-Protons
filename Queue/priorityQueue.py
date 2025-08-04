from queue import PriorityQueue
import time

print("--- Hospital ER---")

# Create a Priority Queue 
hospital_er=PriorityQueue()


#Add Patients to Priority Queue (priority, name)
hospital_er.put((1,"Alice"))
hospital_er.put((2,"Rowan"))
hospital_er.put((5,"Judy"))
hospital_er.put((3,"Omar"))

while not hospital_er.empty():
    prioity, name=hospital_er.get()
    print(f"Treating Patient ..{name} ")