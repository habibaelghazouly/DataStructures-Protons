string = input("Enter String: ")

stack=[]

for i in string:
    stack.append(i)
    
reversed_input=""
while stack:
    reversed_input += stack.pop()
    
print('Input : ',string)
print('Reversed Input : ',reversed_input)
