string =input("Enter the message sent:")
new_string = ''
count = 0

for bit in string:
    new_string += bit  
    if bit == '1':
        count += 1  
    else:
        count = 0  

    
    if count == 5:
        new_string += '0'
        count = 0  

print(new_string)

