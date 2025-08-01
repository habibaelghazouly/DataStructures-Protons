string_input= input("\n\nEnter Sentence to reverse:")
reversed_string_input=""

my_stack=[]

for i in string_input:
    if i !=' ':
        my_stack.append(i)
    else:
        while my_stack:
            reversed_string_input += my_stack.pop()
        reversed_string_input +=' '


print('Input : ',string_input)
print('Reversed Input : ',reversed_string_input) # what about last word??/

while my_stack:
    reversed_string_input += my_stack.pop()
    
print('Input : ',string_input)
print('Reversed Input : ',reversed_string_input) 