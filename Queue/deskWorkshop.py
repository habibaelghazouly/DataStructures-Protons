print("--- Customer Service Queue ---")


regular_queue = []
vip_queue = []

vip_queue.append("Alex")
regular_queue.append("Bob")
regular_queue.append("Sarah")
vip_queue.append("Maria")
regular_queue.append("Mike")

print(f"Initial Queues:")
print(f"  VIPs: {vip_queue}")
print(f"  Regulars: {regular_queue}\n")

#  Process customers as long as at least one queue has people
while regular_queue or vip_queue:
    # Check for VIPs first
    if vip_queue:
        customer = vip_queue.pop(0)
        print(f"Serving VIP customer: {customer}")
    elif regular_queue:
        customer = regular_queue.pop(0)
        print(f"Serving regular customer: {customer}")
    

print("\nAll customers have been served! The office is now empty.")

