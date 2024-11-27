generator=input("Enter the generator:")
string=input("Enter the string:")
d=list(generator)
s=list(string)
for i in range(1,len(d)):
    s.append('0')
count=0
d1=[]
result=[]
final=[]
def xor(a,b):
    if a==b:
        return '0'
    else:
        return '1'       
for i in range(len(d)):
    d1.append(s[count])
    count+=1    
if d1[0]=='1':
    for i in range(len(d1)):
        f=xor(d1[i],d[i])
        result.append(f)
else:
    for i in range(len(d1)):
        result.append(d1[i])

result=result[1:]
result.append(s[count])

while count<len(s):
    if result[0]=='1':
        for i in range(len(result)):
            q=xor(result[i],d[i])
            final.append(q)
    else:
        for i in range(len(result)):
            final.append(result[i])
    result=[]
    result=final[1:]
    count+=1
    if count<len(s):
        result.append(s[count])
    final=[]
result=''.join(result)
stuffed_str=string+result    
print(stuffed_str)
