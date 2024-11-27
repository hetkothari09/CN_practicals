string=input("Enter the message to be sent:")
start=input("Enter the start flag:")
end=input("Enter the end flag:")
esc=input("Enter the escape character:")
a=list(string)
b=[]
for i in a:
    if i==start or i==end:
        i=esc+i
        b.append(i)
    else:
        b.append(i)        
new_str=''.join(b)
result=start+new_str+end
print("stuffed String:"+result)

    
