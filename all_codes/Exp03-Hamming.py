code=input("Enter the code to be transmitted:")
c=list(code)
no_of_bits=len(code)

def paritybits():
    i=0
    while i<len(code):
        a=pow(2,i)
        b=no_of_bits+i+1
        if a>=b:
            break
        else:
            i+=1
    return i
    
no_of_paritybits=paritybits()


h=[]
count=0
index=no_of_bits-1
for i in range(no_of_bits+no_of_paritybits):
    a=pow(2,count)
    if (i+1)==a:
         h.append('')
         count+=1
    else:
        h.append(c[index])
        if index>=0:
            index-=1

for i in range(no_of_bits+no_of_paritybits):
    i1=list(format(i+1,'b'))
    length=len(i1)-1
    if h[i]=='':
        j=length
        m=[]
        for k in range(no_of_bits+no_of_paritybits):
            l=list(format(k+1,'b'))
            k_rev=list(reversed(l))
            if j<len(k_rev):
                if k_rev[j]=='1':
                    l1=''.join(l)
                    num=int(l1,2)
                    m.append(num)

        num1=0
        for re in range(len(m)):
            if h[m[re]-1]=='1':
                num1+=1
            else:
                num1==num1        
        if num1%2==0:
            h[i]='0'
        else:
            h[i]='1'    


result=''.join(h)
result1=''.join(reversed(result))
print("Code transmitted:"+result1)
            
received=input("Enter the code received:")
received1=''.join(reversed(received))
re=[]
c=[]

for i in received1:
    re.append(i)
for i in range(no_of_bits+no_of_paritybits):
    i1=list(format(i+1,'b'))
    length=len(i1)-1
    if (i + 1) & i == 0:
        j=length
        m=[]
        for k in range(no_of_bits+no_of_paritybits):
            l=list(format(k+1,'b'))
            k_rev=list(reversed(l))
            if j<len(k_rev):
                if k_rev[j]=='1':
                    l1=''.join(l)
                    num=int(l1,2)
                    m.append(num)
        num1=0
        for i2 in range(len(m)):
            if re[m[i2]-1]=='1':
                num1+=1
            else:
                num1==num1        
        if num1%2==0:
            c.append('0')
        else:
            c.append('1')   

c1=''.join(c)
c2=int(c1,2)
print(f"Error at position:{c2} from left")
        
    
