print_jobs=[]

print_jobs.append("DOC1")
print_jobs.append("DOC2")
print_jobs.append("DOC3")

while print_jobs:
    current_job = print_jobs.pop(0)
    print(f"Printing: {current_job}")